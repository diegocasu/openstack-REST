import connexion
import six

from swagger_server.models.schedule import Schedule  # noqa: E501
from swagger_server import util


def add_schedule(body):  # noqa: E501
    """Create a new schedule

     # noqa: E501

    :param body: Schedule data
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Schedule.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_employee(scheduleId):  # noqa: E501
    """Deletes an employee

     # noqa: E501

    :param scheduleId: Employee id to delete
    :type scheduleId: int

    :rtype: None
    """
    return 'do some magic!'


def get_schedule_by_id(scheduleId):  # noqa: E501
    """Find schedule by ID

    Returns a single schedule # noqa: E501

    :param scheduleId: ID of Schedule to return
    :type scheduleId: int

    :rtype: Schedule
    """
    return 'do some magic!'


def update_employee_with_form(scheduleId, name=None, status=None):  # noqa: E501
    """Updates an employee in the store with form data

     # noqa: E501

    :param scheduleId: ID of employe that needs to be updated
    :type scheduleId: int
    :param name: Updated name of the employee
    :type name: str
    :param status: Updated status of the employee
    :type status: str

    :rtype: None
    """
    return 'do some magic!'


def update_schedule(body):  # noqa: E501
    """Update an existing schedule

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Schedule.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
