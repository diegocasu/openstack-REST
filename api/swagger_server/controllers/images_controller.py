import connexion
import six

from swagger_server import util

import openstack

def get_images():  # noqa: E501
    """Get images

    Get all images available in the system # noqa: E501

    :rtype: None
    """
    conn = openstack.connect()
    images = [image.to_dict() for image in conn.compute.images()]

    return images
