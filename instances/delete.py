import openstack

conn = openstack.connect()

SERVER_NAME = 'mr-robot'

for server in conn.compute.servers(name=SERVER_NAME):
    print(server.id)
    conn.compute.delete_server(server)
