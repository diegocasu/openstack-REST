#!/bin/sh

source admin-openrc.sh
crond
python3 -m swagger_server
