import sys
import openstack

conn = openstack.connect()

SERVER_NAME = 'mr-robot'
IMAGE_NAME = sys.argv[sys.argv.index('--image') + 1]
FLAVOR_NAME = sys.argv[sys.argv.index('--flavor') + 1]
NETWORK_NAME = sys.argv[sys.argv.index('--network') + 1]
COUNT = int(sys.argv[sys.argv.index('--count') + 1])

image = conn.compute.find_image(IMAGE_NAME)
flavor = conn.compute.find_flavor(FLAVOR_NAME)
network = conn.network.find_network(NETWORK_NAME)

server = conn.compute.create_server(
        name=SERVER_NAME, image_id=image.id, flavor_id=flavor.id,
        networks=[{"uuid": network.id}], min_count=COUNT, max_count=COUNT)

server = conn.compute.wait_for_server(server)
