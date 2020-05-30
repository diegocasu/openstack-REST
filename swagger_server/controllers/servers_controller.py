import connexion
import six

from swagger_server.models.server import Server  # noqa: E501
from swagger_server import util

import openstack

def get_servers():  # noqa: E501
    """Get servers

    Get all servers running in the system # noqa: E501


    :rtype: None
    """
    conn = openstack.connect()
    servers = [server for server in conn.compute.servers()]
    return servers


def servers_post(body):  # noqa: E501
    """Create new server

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Server
    """
    if connexion.request.is_json:
        body = Server.from_dict(connexion.request.get_json())  # noqa: E501
        
        conn = openstack.connect()

        if body.name is None or body.image is None or body.flavor is None or body.network is None:
            return 'name, image, flavor, network are required', 400

        name = body.name
        image = conn.compute.find_image(body.image)
        flavor = conn.compute.find_flavor(body.flavor)
        network = conn.network.find_network(body.network)

        if image is None:
            return 'Cannot find image {}'.format(body.image), 400

        if flavor is None:
            return 'Cannot find flavor {}'.format(body.flavor), 400

        if network is None:
            return 'Cannot find network {}'.format(body.network), 400

        print('Create server with:\nname: {}\nimage: {}\nflavor: {}\nnetwork: {}'.format(name, image.id, flavor.id, network.id))
    
        server = conn.compute.create_server(
                name=name, image_id=image.id, flavor_id=flavor.id,
                networks=[{"uuid": network.id}])

        server = conn.compute.wait_for_server(server)
    
    return server.id
