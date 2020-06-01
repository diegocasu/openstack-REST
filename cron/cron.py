import openstack
import pickle
from datetime import datetime

SERVER_NAME = 'mr-robot'
SCHEDULE_DATABASE = '/usr/src/app/schedule.pickle.db'

current_time_string = (datetime.now()).strftime('%H:%M')
try:
    database = pickle.load(open(SCHEDULE_DATABASE, 'rb'))
except FileNotFoundError:
    print('no database')
    exit(0)

conn = openstack.connect()

for index, schedule in enumerate(database):
    print('[{}] probing {} ({}-{})\t'.format(current_time_string, schedule['id'], schedule['peak_interval']['start'], schedule['peak_interval']['end']), end='')

    if schedule['peak_interval']['start'] == current_time_string:
        print('starting vm')
        IMAGE_NAME = schedule['server']['image']
        FLAVOR_NAME = schedule['server']['flavor']
        NETWORK_NAME = schedule['server']['network']
        COUNT = schedule['server']['count']

        image = conn.compute.find_image(IMAGE_NAME)
        flavor = conn.compute.find_flavor(FLAVOR_NAME)
        network = conn.network.find_network(NETWORK_NAME)
        
        ids = []
        for i in range(COUNT):
            server = conn.compute.create_server(
                name=SERVER_NAME, image_id=image.id, flavor_id=flavor.id,
                networks=[{"uuid": network.id}])

            server = conn.compute.wait_for_server(server)
            ids.append(server.id)
            
        schedule['server']['ids'] = ids
        database[index] = schedule

        print(database)
        
        try:
            pickle.dump(database, open(SCHEDULE_DATABASE, 'wb'))
        except:
            print('unable to update database')


    elif schedule['peak_interval']['end'] == current_time_string:
        print('stopping vm ', end='')
        for id in schedule['server']['ids']:
            server = conn.compute.find_server(id)
            conn.compute.delete_server(server)

        del schedule['server']['ids']
        database[index] = schedule

        try:
            pickle.dump(database, open(SCHEDULE_DATABASE, 'wb'))
        except:
            print('unable to update database')

    else:
        print('nothing to do')

