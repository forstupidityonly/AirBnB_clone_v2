#!/usr/bin/python3
'''Module to generat .tgz archive from contents of web_static'''
from datetime import datetime
from fabric.api import local


def do_pack():
    '''Method to generate .tgz archive'''
    local("sudo mkdir -p versions")
    timeStr = datetime.now().strftime('%Y%m%d%H%M%S')
    tgzName = "versions/web_static_{}.tgz".format(timeStr)
    local("sudo tar -cvzf {} web_static".format(tgzName))
    return (tgzName)
