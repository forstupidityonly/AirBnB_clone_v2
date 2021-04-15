#!/usr/bin/python3
'''Module distributes an archive to your web servers
using the function do_deploy'''
from datetime import datetime
from fabric.api import local, env, put, sudo
import os


env.user = 'ubuntu'
env.hosts = ['34.75.36.193', '3.94.194.152']

def do_deploy(archive_path):
    '''Method to deploy archive'''

    newFile = "/data/web_static/releases/{}".format(
        archive_path.split(".", 1)[0])
    tmpFile = "/tmp/{}".format(archive_path)
    cur = "/data/web_static/current"

    if os.path.exists(archive_path) is False:
        return False

    try:
        put("{}, '/tmp/'".format(archive_path))
        sudo("mkdir -p {}".format(newFile))
        sudo("tar -xzf {} -C {}/".format(tmpFile, newFile))
        sudo("rm {}".format(tmpFile))
        sudo("mv {}/web_static/* {}/".format(newFile, newFile))
        sudo("rm -rf {}/web_static".format(newFile))
        sudo("rm -rf {}".format(cur))
        sudo("ln -s {} {}".format(newFile, cur))
        return(True)
    except:
        return(False)
