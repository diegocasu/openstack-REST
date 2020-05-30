import sys
import subprocess

try:
    SERVER_NAME = 'mr-robot'
    count = int(sys.argv[sys.argv.index('--count') + 1])

    for i in range(1, count + 1):
        CMD = 'openstack server delete {}'.format(SERVER_NAME + '-' + str(i))
        result = subprocess.check_output(CMD, shell=True)
        print(CMD)
        print(result)

except:
    print('python delete.py --count <count>')
    exit(1)
