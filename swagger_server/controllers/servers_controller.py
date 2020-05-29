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
    return body
