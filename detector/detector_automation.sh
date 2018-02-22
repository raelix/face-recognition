#!/bin/bash

#source /usr/local/bin/virtualenvwrapper.sh 
#workon facecourse-py3
url=$(cat ip_camera_url )
python detector.py "$url"
