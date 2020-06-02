# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestServersController(BaseTestCase):
    """ServersController integration test stubs"""

    def test_get_servers(self):
        """Test case for get_servers

        Get servers
        """
        response = self.client.open(
            '/v1/servers',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
