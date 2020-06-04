from flask import current_app
import requests
from datetime import timedelta


def get_resource(resource):
    url = 'http://{}:{}/v1/{}'.format(current_app.config['CONTROLLER_IP'], current_app.config['CONTROLLER_PORT'], resource)
    resp = requests.get(url)
    if resp.status_code != 200:
        return []

    resources = [resource for resource in resp.json()]
    return resources


def post_resource(resource, data):
    url = 'http://{}:{}/v1/{}'.format(current_app.config['CONTROLLER_IP'], current_app.config['CONTROLLER_PORT'], resource)
    resp = requests.post(url, json=data)
    if resp.status_code != 201:
        return None

    return resp.text

def delete_resource(resource, id):
    url = 'http://{}:{}/v1/{}/{}'.format(current_app.config['CONTROLLER_IP'], current_app.config['CONTROLLER_PORT'],
                                      resource, id)
    resp = requests.delete(url)
    if resp.status_code != 200:
        return False

    return True

def convert_to_utc(localtime, timezone):
    delta = timedelta(hours=timezone)
    return localtime - delta

def convert_from_utc(utctime, timezone):
    delta = timedelta(hours=timezone)
    return utctime + delta