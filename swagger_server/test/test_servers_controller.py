# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.server import Server  # noqa: E501
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

    def test_servers_post(self):
        """Test case for servers_post

        Create new server
        """
        body = Server()
        response = self.client.open(
            '/v1/servers',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
