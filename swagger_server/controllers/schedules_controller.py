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


def delete_schedule(scheduleId):  # noqa: E501
    """Deletes a schedule

     # noqa: E501

    :param scheduleId: Schedule ID to delete
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
