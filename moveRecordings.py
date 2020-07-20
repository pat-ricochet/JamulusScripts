#!/bin/python

import sys
from os import walk
from os import path
import shutil
import logging
import time
import subprocess
from zipfile import ZipFile
logging.basicConfig(filename='getRecordings.log',level=logging.DEBUG)
#logging.debug('This message should go to the log file')
#logging.info('So should this')
#logging.warning('And this, too')

args=sys.argv
subdir=args[1]
dir = "/jamulus/recordings/"+subdir
dest = "/var/www/"+subdir
while True:
    recordZip = False
    for (dirpath, dirnames, filenames) in walk(dir):
        hasRppFile = any(".rpp" in file for file in filenames)
        if hasRppFile:
            recordZip = dirpath+".zip"
            zipName = path.basename(dirpath)+".zip" 
            z = subprocess.Popen(['zip', '-r', recordZip, dirpath])
            n = subprocess.Popen(['renice', '+19', str(z.pid)])
            zStatus = z.wait()
            m = subprocess.Popen(['mv', recordZip, dest])
            mStatus = m.wait()
            logging.info("Successfully moved "+recordZip+" to "+dest)
            shutil.rmtree(dirpath)
            logging.info("Successfully removed "+dirpath)
    time.sleep(1)
