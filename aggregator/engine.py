#!/usr/bin/python

import os
import requests
import json
import subprocess
from subprocess import call

LG_TV_ADDRESS='192.168.1.3'
HUB_ADDRESS='http://192.168.1.4/api/40j7Sjw5zpf11DdS4IQfza39nqbZUKEGmX0WeIsb/'
SENSOR_ADDRESS=HUB_ADDRESS+'sensors/23'
MAIN_LIGHT_STATUS=HUB_ADDRESS+'lights/2'
SECONDARY_LIGHT_STATUS=HUB_ADDRESS+'lights/1'

CHECK_WINDOWS_SCREEN_ON='''sshpass -p 'Enrico!Enrico52' ssh -o StrictHostKeyChecking=no raelix@192.168.1.20 'wmic path win32_desktopmonitor GET Availability' | grep 3 '''

def is_motion_detected():
	sensor_state=do_get(SENSOR_ADDRESS)
	presence=sensor_state['state']['presence']
        return presence

def get_n_persons():
	pass

def get_main_light_status():
        status=do_get(MAIN_LIGHT_STATUS)
        if status:
                #print(status['state'])
                return status['state']

def get_secondary_light_status():
	status=do_get(SECONDARY_LIGHT_STATUS)
	if status:
		#print(status['state'])
		return status['state']

def are_screens_on():
	return_code=run_command(CHECK_WINDOWS_SCREEN_ON)
	if return_code is None or return_code not in (0,1):
		print('error during screen status check')
		return False
	if return_code is not None and return_code==0:
		return True
	else:
		return False	

def is_tv_on():
	return ping(LG_TV_ADDRESS)

def ping(ip_address):
	response = os.system("ping -c 1 %s > /dev/null" % ip_address)
	if response == 0:
		return True
	else:
		return False

def run_command(cmd):
	pipes = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	std_out, std_err = pipes.communicate()
	return pipes.returncode

def run_command_old(cmd):
	try:
		return subprocess.call(cmd, shell=True)
	except:
		pass

def do_get(address):
	response=requests.get(url=address)
	if response.text:
		try:
			return json.loads(response.text)
		except:
			pass
	


def __main__():
	print 'motion detected: %s' % is_motion_detected()
	print '      screen on: %s' % are_screens_on()
	print '   2nd light on: %s' % get_secondary_light_status()['on']
	print '   1st light on: %s' % get_main_light_status()['on']
	print '          TV on: %s' % is_tv_on()
__main__()
