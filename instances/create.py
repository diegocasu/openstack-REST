import sys
import subprocess

try:
    SERVER_NAME = 'mr-robot'
    image = sys.argv[sys.argv.index('--image') + 1]
    flavor = sys.argv[sys.argv.index('--flavor') + 1]
    network = sys.argv[sys.argv.index('--network') + 1]
    min = int(sys.argv[sys.argv.index('--count') + 1])

    CMD = 'openstack server create --image {0} --flavor {1} --network {2} --min {3} --max {3} {4}'.format(image, flavor, network, min, SERVER_NAME)

    result = subprocess.check_output(CMD, shell=True)
    print(CMD)
    print(result)

except:
    print('python create.py --image <image> --flavor <flavor> --network <network> --count <count>')
    exit(1)
