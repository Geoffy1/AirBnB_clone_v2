#!/usr/bin/python3
'''
    Generates .tgz archive from `web_static`.
'''
from fabric.api import local, hide
from datetime import datetime
import os.path


def do_pack():
    '''
        Packs web_static.
    '''
    timePacked = datetime.now().strftime('%Y%m%d%H%M%S')
    packPath = "versions/web_static_{:s}.tgz".format(timePacked)

    firstMSG = "Packing web_static to {:s}".format(packPath)
    print(firstMSG)

    if os.path.isdir("versions") is False:
        local('mkdir versions')

    local('tar -cvzf {:s} web_static'.format(packPath))

    with hide('running'):
        size = local('wc -c < {:s}'.format(packPath), capture=True)

    secondMSG = "web_static packed: {:s} -> {:s}".format(packPath, size)
    print(secondMSG)

    if os.path.exists(packPath):
        return packPath
    return None
