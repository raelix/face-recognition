#!/usr/bin/python

import datetime
from populate_table import insert_data,read_data
from netatmo.welcome_api import get_number_of_people, is_user_present
from tv.lg_api import is_tv_on
from hue.hue_api import get_main_light_status, get_secondary_light_status, is_main_light_on, is_secondary_light_on, \
    is_motion_detected


def get_day_of_week():
    return datetime.datetime.now().strftime('%A')


def get_hour():
    return datetime.datetime.now().hour


def get_dictionary():
    return {
        'is_user_at_home': is_user_present('Gianmarco'),
        'n_of_people': get_number_of_people(),
        'light_1_status': is_main_light_on(),
        'light_1_color': get_main_light_status(),
        'light_2_status': is_secondary_light_on(),
        'light_2_color': get_secondary_light_status(),
        'tv_status': is_tv_on(),
        'day': get_day_of_week(),
        'hour': get_hour(),
    }


def __main__():
    print 'is user present: %s' % is_user_present('Gianmarco')
    print '    n of people: %s' % get_number_of_people()
    print 'motion detected: %s' % is_motion_detected()
    print '   1nd light on: %s' % is_main_light_on()
    print '   light status: %s' % get_main_light_status()
    print '   2nd light on: %s' % is_secondary_light_on()
    print '   light status: %s' % get_secondary_light_status()
    print '          TV on: %s' % is_tv_on()
    print '            Day: %s' % get_day_of_week()
    print '           Hour: %s' % get_hour()
    insert_data(get_dictionary())
__main__()
