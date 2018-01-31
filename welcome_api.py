#!/usr/bin/python
import requests
import json
import datetime

def find_user(user='Gianmarco', body={}):
    if body:
        try:
            home = body['homes'][0]
            events_list = home['events']
            for event in events_list:
                #print(event)
                #print(event["time"])
                if event['person_id'] == '187e30ee-2316-4e2b-90fd-07a29e3fe5ed':
                 print(datetime.datetime.fromtimestamp(int(event["time"])).strftime('%Y-%m-%d %H:%M:%S'))
            for person in home['persons']:
                if person['id'] == '187e30ee-2316-4e2b-90fd-07a29e3fe5ed':
                 print(datetime.datetime.fromtimestamp(int(person['last_seen'])).strftime('%Y-%m-%d %H:%M:%S'))
                #print(event['message'].decode('ascii'))
#                if event.has_key("message"):
#                    print(event["message"])
                #print(event.has_key("message"))
                #ev_str = event['message'].decode('ascii')
                #if ev_str.startswith("<b>"+user):
                #    id_p=event['message']['person_id']
                #    print(id_p)
                #    return id_p
        except Exception, e:
            print(e)
            pass
    
	

payload = {'grant_type': 'password',
           'username': "gianmarco.ascenzo@gmail.com",
           'password': "Hmr_Admin",
           'client_id':"5a668173923dfefa918b58cd",
           'client_secret': "7GjlMgfslsBr30TrCnXnHE6m9q",
	    'scope': 'read_camera access_camera'}
try:
    headers= {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post("https://api.netatmo.com/oauth2/token", data=payload)
    response.raise_for_status()
    access_token=response.json()["access_token"]
    refresh_token=response.json()["refresh_token"]
    scope=response.json()["scope"]
    print("Your access token is:", access_token)
    print("Your refresh token is:", refresh_token)
    print("Your scopes are:", scope)
except requests.exceptions.HTTPError as error:
    print (error)
    print(error.response.status_code, error.response.text)

params = {
	'access_token':access_token
}

try:
    response = requests.post("https://api.netatmo.com/api/gethomedata", params=params)
    response.raise_for_status()
    data = response.json()["body"]
    find_user("Gianmarco",data)
except requests.exceptions.HTTPError as error:
    print(error.response.status_code, error.response.text)


