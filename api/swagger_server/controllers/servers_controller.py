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
    servers = [server.to_dict() for server in conn.compute.servers()]
    return servers
