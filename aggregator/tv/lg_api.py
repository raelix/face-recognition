# this is an example...up to now there are no good sdk for webos
import os

LG_TV_ADDRESS = '192.168.1.3'


def is_tv_on():
    return ping(LG_TV_ADDRESS)


def ping(ip_address):
    response = os.system("ping -c 1 %s > /dev/null" % ip_address)
    if response == 0:
        return True
    else:
        return False
