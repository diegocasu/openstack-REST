import connexion
import six

from swagger_server.models.schedule import Schedule  # noqa: E501
from swagger_server.models.peak_interval import PeakInterval
from swagger_server.models.server import Server
from swagger_server import util

from datetime import datetime
import uuid

from crontab import CronTab
import openstack

def add_schedule(body):  # noqa: E501
    """Create a new schedule

     # noqa: E501

    :param body: Schedule data
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Schedule.from_dict(connexion.request.get_json())  # noqa: E501

        conn = openstack.connect()

        try:
            PEAK_START = datetime.strptime(body.peak_interval['start'], '%H:%M')
            PEAK_END = datetime.strptime(body.peak_interval['end'], '%H:%M')

            SERVER_IMAGE = body.server['image']
            SERVER_FLAVOR = body.server['flavor']
            SERVER_NETWORK = body.server['network']
            SERVER_COUNT = body.server['count']

            # Check if the selected resources actually are present in the system
            image = conn.compute.find_image(SERVER_IMAGE)
            flavor = conn.compute.find_flavor(SERVER_FLAVOR)
            network = conn.network.find_network(SERVER_NETWORK)
            count = int(SERVER_COUNT)

            if image is None:
                return 'No image found for {}'.format(SERVER_IMAGE), 400

            if flavor is None:
                return 'No flavor found for {}'.format(SERVER_FLAVOR), 400

            if network is None:
                return 'No network found for {}'.format(SERVER_NETWORK), 400

            if count <= 0:
                return 'Count must be greater than 0', 400

            # Install task on crontab file
            cron = CronTab(user=True)
            ID = uuid.uuid1()
            CREATE_CMD = 'python /usr/src/app/instances/create.py --image {} --flavor {} --network {} --count {}'.format(image.name, flavor.name, network.name, count)
            DELETE_CMD = 'python /usr/src/app/instances/delete.py'

            # Create VM task
            create = cron.new(command=CREATE_CMD, comment=str(ID))
            create.hour.on(PEAK_START.strftime('%H'))
            create.minute.on(PEAK_START.strftime('%M'))

            # Delete VM task
            delete = cron.new(command=DELETE_CMD, comment=str(ID))
            delete.hour.on(PEAK_END.strftime('%H'))
            delete.minute.on(PEAK_END.strftime('%M'))

            cron.write()

            return ID, 201
                
        except Exception as e:
            return str(e), 400

def delete_schedule(scheduleId):  # noqa: E501
    """Deletes a schedule

     # noqa: E501

    :param scheduleId: Schedule ID to delete
    :type scheduleId: str

    :rtype: None
    """
    return 'do some magic!'


def get_schedules():  # noqa: E501
    """Get schedules

    Returns all schedules # noqa: E501


    :rtype: Schedule
    """
    return 'do some magic!'

