#!/usr/bin/python

import psycopg2
from psycopg2 import connect

__QUERY = '''insert into data (hour,day,is_user_at_home,n_of_people,tv_status,light_1_status,light_2_status,light_1_color,light_2_color) " \
    "values(%s,%s,%s,%s);'''


def insert_data(data):
    c = connect(database='home', user='postgres', host="recognizer_db", port=5432)
    c.cursor()
    query = c.mogrify(__QUERY, (
    data['hour'], data['day'], data['is_user_at_home'], data['n_of_people'], data['tv_status'], data['light_1_status'],
    data['light_2_status'], data['light_1_color'], data['light_2_color'],))
    c.execute(query)

    # CREATE TABLE IF NOT EXISTS data (
    #   id SERIAL,
    #   hour               integer       not null,
    #   day                varchar       not null,
    #   is_user_at_home    boolean       not null,
    #   n_of_people        integer       not null,
    #   tv_status          boolean       not null,
    #   light_1_status     boolean       not null,
    #   light_2_status     boolean       not null,
    #   light_1_color      varchar       not null,
    #   light_2_color      varchar       not null
    # );
