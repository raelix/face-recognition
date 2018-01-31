import json
import requests

HUB_ADDRESS = 'http://192.168.1.4/api/40j7Sjw5zpf11DdS4IQfza39nqbZUKEGmX0WeIsb/'
SENSOR_ADDRESS = HUB_ADDRESS + 'sensors/23'
MAIN_LIGHT_STATUS = HUB_ADDRESS + 'lights/2'
SECONDARY_LIGHT_STATUS = HUB_ADDRESS + 'lights/1'


def get_main_light_status():
    status = do_get(MAIN_LIGHT_STATUS)
    if status:
        return '%s-%s-%s-%s' % (
            status['state']['hue'], status['state']['bri'], status['state']['ct'],
            status['state']['sat'])


def is_main_light_on():
    status = do_get(MAIN_LIGHT_STATUS)
    if status:
        return status['state']['on']


def get_secondary_light_status():
    status = do_get(SECONDARY_LIGHT_STATUS)
    if status:
        return '%s-%s-%s-%s' % (
            status['state']['hue'], status['state']['bri'], status['state']['ct'],
            status['state']['sat'])


def is_secondary_light_on():
    status = do_get(SECONDARY_LIGHT_STATUS)
    if status:
        return status['state']['on']


def is_motion_detected():
    sensor_state = do_get(SENSOR_ADDRESS)
    presence = sensor_state['state']['presence']
    return presence


def do_get(address):
    response = requests.get(url=address)
    if response.text:
        try:
            return json.loads(response.text)
        except:
            pass
