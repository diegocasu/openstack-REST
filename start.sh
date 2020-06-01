#!/bin/sh

# Activate the authentication file
source admin-openrc.sh

# Add job for cron
echo "* * * * * python /usr/src/app/cron/cron.py >> /usr/src/app/cron/cron.log" >> /etc/crontabs/root
# Start cron deamon for running scheduled tasks
crond

# Create two flavors for requirements:
# 1) Standard
openstack flavor create --public standard --id auto --ram 128 --disk 1 --vcpus 2
# 2) Large
openstack flavor create --public large --id auto --ram 256 --disk 1 --vcpus 4

# Start the REST server
python3 -m swagger_server
