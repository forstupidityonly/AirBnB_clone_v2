#!/usr/bin/python3
'''Module creates and distributes an archive to your web servers,
using the function deploy:'''

from datetime import datetime
from fabric.api import local, env, put, sudo
import os
'''
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
'''

env.user = 'ubuntu'
env.hosts = ['34.75.36.193', '3.94.194.152']


def do_deploy(archive_path):
    '''Method to deploy archive'''

    if os.path.exists(archive_path) is False:
        return False

    arch = archive_path.split("/", 2)[1]
    new_file = '/data/web_static/releases/{}'.format(
        arch.split(".", 1)[0])
    tmp_file = '/tmp/{}'.format(arch)
    cur = '/data/web_static/current'

    '''
    archive_path = versions/web_static_20210415160740.tgz
    arch = web_static_20210415160740.tgz
    new_file = /data/web_static/releases/web_static_20210415160740
    tmp_file = /tmp/web_static_20210415160740.tgz
    cur = /data/web_static/current
    '''

    try:
        put(archive_path, '/tmp/')
        sudo("mkdir -p {}/".format(new_file))
        sudo("tar -xzf {} -C {}/".format(tmp_file, new_file))
        sudo("rm {}".format(tmp_file))
        sudo("mv {}/web_static/* {}".format(new_file, new_file))
        sudo("rm -rf {}/web_static".format(new_file))
        sudo("rm -rf {}".format(cur))
        sudo("ln -s {}/ {}".format(new_file, cur))
        print("YAY! LOVE YOU!")
        return(True)
    except BaseException:
        print("KEEP TRYING! :)")
        return(False)


def do_pack():
    '''Method to generate .tgz archive'''
    local("mkdir -p versions")
    timeStr = datetime.now().strftime('%Y%m%d%H%M%S')
    tgzName = "versions/web_static_{}.tgz".format(timeStr)
    local("tar -cvzf {} web_static".format(tgzName))
    return (tgzName)


def deploy():
    '''Method that creates and distributes an archive to servers'''
    newArc = do_pack()
    if newArc is None:
        return(False)
    return(do_deploy(newArc))
