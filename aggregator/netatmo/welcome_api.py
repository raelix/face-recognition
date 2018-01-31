#!/usr/bin/python

import requests
import json
import datetime
import logging
from welcome_credential import payload, __produce_getlasteventofParams


def __get_token():
    try:
        response = requests.post("https://api.netatmo.com/oauth2/token", data=payload)
        response.raise_for_status()
        access_token = response.json()["access_token"]
        return access_token
    except requests.exceptions.HTTPError as error:
        logging.error(error.response.status_code, error.response.text)

def is_user_present(user='Gianmarco'):
    try:
        response = requests.post("https://api.netatmo.com/api/getlasteventof",
                                 params=__produce_getlasteventofParams(__get_token()))
        response.raise_for_status()
        events = response.json()['body']['events_list']
        for event in events:
            if user in event['message']:
                return True
    except requests.exceptions.HTTPError as error:
        logging.error(error.response.status_code, error.response.text)
    return False

def get_number_of_people():
    try:
        response = requests.post("https://api.netatmo.com/api/getlasteventof",
                                 params=__produce_getlasteventofParams(__get_token()))
        response.raise_for_status()
        return len(response.json()['body']['events_list'])
    except requests.exceptions.HTTPError as error:
        logging.error(error.response.status_code, error.response.text)


