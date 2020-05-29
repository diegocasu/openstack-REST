import connexion
import six

from swagger_server import util

import openstack

def get_networks():  # noqa: E501
    """Get networks

    Get all networks # noqa: E501


    :rtype: None
    """
    conn = openstack.connect()
    networks = [network for network in conn.network.networks()]
    return networks
