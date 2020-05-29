import connexion
import six

from swagger_server import util

import openstack

def get_flavors():  # noqa: E501
    """Get flavors

    Get all flavors available in the system # noqa: E501


    :rtype: None
    """
    conn = openstack.connect()
    flavors = [flavor for flavor in conn.compute.flavors()]
    return flavors
