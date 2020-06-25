#!/bin/sh

# Activate the authentication file
source admin-openrc.sh

# Add job for cron
exists=$(crontab -l | grep cron.py)
if [ -z $exists ]; then
	echo "* * * * * python /usr/src/app/cron/cron.py >> /usr/src/app/cron/cron.log" >> /etc/crontabs/root
fi
# Start cron deamon for running scheduled tasks
crond

# Create two flavors for requirements:
# 1) Standard
openstack flavor create --public standard --id auto --ram 64 --disk 1 --vcpus 1
# 2) Large
openstack flavor create --public large --id auto --ram 128 --disk 1 --vcpus 2

# Start the REST server
python3 -m swagger_server
