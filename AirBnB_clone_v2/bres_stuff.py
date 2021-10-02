import os
from fabric.api import env, run
'''Module with commands to run on both web-01 web-02'''


env.hosts = ['34.75.36.193', '3.94.194.152']
env.user = "ubuntu"

def remove(path):
    '''Method to remove from 2 servers''' 
    if os.path.isdir(path):
        run('sudo rm -rf {}'.format(path))
        print("DIRECTORY REMOVED: {}".format(path))
    elif os.path.isfile(path):
        run('sudo rm {}'.format(path))
        print("FILE REMOVED: {}".format(path))
    else:
        print("PLEASE CHECK PATH AND TRY AGAIN! LOVE YOU!")
