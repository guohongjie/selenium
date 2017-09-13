#-*-coding:utf-8 -*-
import zipfile
import os.path
import os
def addfile(zipname,dir):
    f = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)
    startdir = dir
    for dirpath, dirnames, filenames in os.walk(startdir):
        for filename in filenames:
            f.write(os.path.join(dirpath, filename))
    f.close()