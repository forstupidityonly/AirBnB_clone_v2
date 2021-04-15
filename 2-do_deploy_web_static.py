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

    if os.path.exists(archive_path) is False:
        return False
    
    arch = archive_path.split("/", 2)[1]
    new_file = "/data/web_static/releases/{}".format(
        arch.split(".", 1)[0])
    tmp_file = "/tmp/{}".format(arch)
    cur = "/data/web_static/current"

    '''
    archive_path = versions/web_static_20210415041353.tgz
    arch = web_static_20210415041353.tgz
    new_file = /data/web_static/releases/web_static_20210415041353
    tmp_file = /tmp/web_static_20210415041353.tgz
    cur = /data/web_static/current
    '''

    try:
        put(archive_path, '/tmp/')
        run("mkdir -p {}/".format(new_file))
        print(made it passed mkdir!!)
        run("tar -xzf {} -C {}/".format(tmp_file, new_file))
        run("rm {}".format(tmp_file))
        run("mv {}/web_static/ {}".format(new_file, new_file))
        run("rm -rf {}/web_static".format(new_file))
        run("rm -rf {}".format(cur))
        run("ln -s {} {}".format(new_file, cur))
        print("YAY! LOVE YOU!")
        return(True)
    except:
        print("KEEP TRYING! :)")
        return(False)
