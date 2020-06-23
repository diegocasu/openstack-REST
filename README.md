# OpenStack REST

This is a project developed for the Cloud Computing course of Master Degree in Computer Engineering.

## Requirements

The application must allow to schedule the automatic creation of an additional set of VMs of a certain type at peak hours.
The following functionalities must be implemented:

- At initialization, the application should create two new flavors on the platform, one _standard_ flavor and a _large_ flavor with more resources;
- At scheduled times, the application should trigger the creation of new VMs, based on an existing image;
- At the end of the scheduled peak period, the application should destroy the additional VMs.

In order to allow system administrator to schedule for the creation of new VMs, the application must expose a REST interface to schedule the peak period and select the flavor and the image for the VMs to be created.

## Repository

The repository is organized in this way:

- _api_ directory contains the implementation of the API server
- _web_ directory containes the implementation of the web server

## API server

The API server communicates with the OpenStack instance through the [openstacksdk](https://github.com/openstack/openstacksdk) python library and exposes the following endpoints:

- `GET /images`: returns all the images available on the system
- `GET /flavors`: returns all the flavors available on the system
- `GET /networks`: returns all the networks available on the system
- `GET /schedules`: returns all the schedules programmed by the user
- `POST /schedules`: creates a new schedule
- `DELETE /schedules/<scheduleId>`: deletes the schedule identified by `scheduleId`

It has been implemented using [Swagger](https://swagger.io).

## Web server

The web server offers a GUI for managing the creation and deletion of schedules interacting with the API server. It has been implemented using [Flask](https://flask.palletsprojects.com/en/1.1.x/).

## Usage

The deployment of both services can be done by:

```bash
docker-compose up
```

which starts the API service on port `8080` and the web serice on port `5000`.

## Contributors
F. Barbarulo, D. Casu, B.T. Gurmesa, G.B. Rolandi 
