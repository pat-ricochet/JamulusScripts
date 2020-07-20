# JamulusScripts

## moveRecordings.py
* Dependencies (python and zip)

Daemon to monitor for Jamulus recording completion (checks for creation of reaper file (.rpp), zips (with low priority) and publishes to apache httpd doc root.
Assumes recordings are created in /jamulus/recordings/$subdirectory (the script takes one argument $subdirectory)
Assumes apache httpd doc root is /var/www/$subdirectory
The script is intended to be run as a background process
```moverecordings.py mysubdirectory &```
it is a good idea to run a cron job to clean up the apache doc root periodically to save space
I run the following cron job
```0 4 * * * find /var/www/mysubdirectory -mtime +1 -delete```
