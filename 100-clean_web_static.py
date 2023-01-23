#!/usr/bin/python3
'''
    Performs cleanup of old versions of `web_static`.
'''

from fabric.api import *
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


def do_deploy(archive_path):
    '''
        Deploys archive to web server.
    '''
    if not os.path.exists(archive_path):
        return False

    pathName = os.path.splitext(archive_path)[0]
    pathName = pathName.split('/')[-1]
    pathNew = pathName + '.tgz'

    try:
        put(archive_path, "/tmp/")

        run('mkdir -p /data/web_static/releases/{:s}'.format(pathName))
        run('tar -xzf /tmp/{:s} -C /data/web_static/releases/{:s}'.
            format(pathNew, pathName))

        run('rm /tmp/{:s}'.format(pathNew))
        run('mv /data/web_static/releases/{:s}/web_static/*'
            ' /data/web_static/releases/{:s}'.
            format(pathName, pathName))

        run('rm -rf /data/web_static/releases/{:s}/web_static'.
            format(pathName))

        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{:s} /data/web_static/current'.
            format(pathName))

        print("New version successfuly deployed!")
        return True

    except Exception:
        return False


def deploy():
    '''
        Creates and deploys archive.
    '''
    archive_path = do_pack()
    if not archive_path:
        return False

    return do_deploy(archive_path)


def do_clean(number=0):
    '''
        Deletes outdated archives.
    '''

    try:
        number = int(number)
    except Exception:
        return None

    if number < 0:
        return None

    number = 2 if (number == 0 or number == 1) else (number + 1)

    with lcd("./versions"):
        local('ls -t | tail -n +{:d} | xargs rm -rf --'.
              format(number))

    with cd("/data/web_static/releases"):
        run('ls -t | tail -n +{:d} | xargs rm -rf --'.
            format(number))
