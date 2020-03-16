#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
Create sequentially numbered Baselight folders.
You must refresh the Job Manager after running the script.
Copyright (c) 2020 Igor Riđanović, Igor [at] hdhead.com, www.metafide.com
'''

import flapi
from getflapi import getflapi

def make_seq_folder(ip, scene, foldername, count):
    conn, msg = getflapi()
    jobman = conn.JobManager

    try:
        for seq in range(count):
            f = foldername + '_' + str(seq).zfill(3)
            jobman.create_folder(ip, scene, f)

    except flapi.FLAPIException:
        print 'Could not create folders.'
        return False

    # Cleanup
    conn.close()

if __name__=='__main__':
    conn, msg = getflapi()
    print msg + '\n'

    ip           = 'localhost'
    currentScene = 'Test01'
    folderName   = 'MyFolder'
    count        = 3

    make_seq_folder(ip, currentScene, folderName, count)
