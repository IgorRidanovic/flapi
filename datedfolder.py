#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
Create a Baselight folder with current date and time stamp.
You must refresh the Job Manager after running the script.
Copyright (c) 2020 Igor Riđanović, Igor [at] hdhead.com, www.metafide.com
'''

import flapi
from getflapi import getflapi
from datetime import datetime

def make_dated_folder(ip, scene, foldername):
    conn, msg = getflapi()
    jobman = conn.JobManager

    stamp = datetime.now().strftime('_%d-%b-%Y_%H.%M.%S')

    try:
        jobman.create_folder(ip, scene, foldername + stamp)

    except flapi.FLAPIException:
        print 'Could not create a folder.'
        return False

    # Cleanup
    conn.close()

if __name__=='__main__':
    conn, msg = getflapi()
    print msg + '\n'

    ip           = 'localhost'
    currentScene = 'Test01'
    folderName   = 'MyFolder'
    make_dated_folder(ip, currentScene, folderName)
