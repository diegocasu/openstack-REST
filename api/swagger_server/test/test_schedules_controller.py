# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.schedule import Schedule  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSchedulesController(BaseTestCase):
    """SchedulesController integration test stubs"""

    def test_add_schedule(self):
        """Test case for add_schedule

        Create a new schedule
        """
        body = Schedule()
        response = self.client.open(
            '/v1/schedules',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_schedule(self):
        """Test case for delete_schedule

        Deletes a schedule
        """
        response = self.client.open(
            '/v1/schedules/{scheduleId}'.format(scheduleId='scheduleId_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_schedules(self):
        """Test case for get_schedules

        Get schedules
        """
        response = self.client.open(
            '/v1/schedules',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
