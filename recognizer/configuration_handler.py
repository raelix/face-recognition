import time
import fcntl
import os
import signal
from os.path import exists

listener = None

class configuration_handler(object):

   configuration_file_path = '/root/test.txt'

   def callback(self):
      print('Event detected')

   def load_configuration(self):
      if exists(self.configuration_file_path):
         add_event_on_file_change(self.configuration_file_path, self)
      else:
         print("Configuration file not found! %s...abort!" % self.configuration_file_path)


def handler(signum, frame):
   if listener:
      listener.callback()

def add_event_on_file_change(filename, in_listener):
   if in_listener:
      listener = in_listener
      signal.signal(signal.SIGIO, handler)
      fd = os.open(filename,  os.O_RDONLY)
      fcntl.fcntl(fd, fcntl.F_SETSIG, 0)
      fcntl.fcntl(fd, fcntl.F_NOTIFY, fcntl.DN_MODIFY )

