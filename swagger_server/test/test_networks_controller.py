# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestNetworksController(BaseTestCase):
    """NetworksController integration test stubs"""

    def test_get_networks(self):
        """Test case for get_networks

        Get networks
        """
        response = self.client.open(
            '/v1/networks',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
