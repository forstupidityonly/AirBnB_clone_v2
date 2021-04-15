#!/usr/bin/python3
'''Module creates and distributes an archive to your web servers,
using the function deploy:'''

from datetime import datetime
from fabric.api import local, env, put, sudo
import os
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


env.user = 'ubuntu'
env.hosts = ['34.75.36.193', '3.94.194.152']


def deploy():
    '''Method that creates and distributes an archive to servers'''
    try:
        newArc = do_pack()
        return(do_deploy(newArc))
    except:
        return(False)
