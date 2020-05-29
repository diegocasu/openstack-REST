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

    def test_delete_employee(self):
        """Test case for delete_employee

        Deletes an employee
        """
        response = self.client.open(
            '/v1/schedules/{scheduleId}'.format(scheduleId=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_schedule_by_id(self):
        """Test case for get_schedule_by_id

        Find schedule by ID
        """
        response = self.client.open(
            '/v1/schedules/{scheduleId}'.format(scheduleId=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_employee_with_form(self):
        """Test case for update_employee_with_form

        Updates an employee in the store with form data
        """
        data = dict(name='name_example',
                    status='status_example')
        response = self.client.open(
            '/v1/schedules/{scheduleId}'.format(scheduleId=789),
            method='POST',
            data=data,
            content_type='application/x-www-form-urlencoded')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_schedule(self):
        """Test case for update_schedule

        Update an existing schedule
        """
        body = Schedule()
        response = self.client.open(
            '/v1/schedules',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
