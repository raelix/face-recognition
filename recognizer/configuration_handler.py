import time
import fcntl
import os
import signal
from os.path import exists

listener = None

directory = '/root/recognizer_configuration/'
configuration_file_name='recognizer.json'

class configuration_handler(object):

   def callback(self):
      print('Event detected')

   def load_configuration(self, attach_listener_on_file_change=True):

      if not os.path.exists(directory):
         os.makedirs(directory)

      if not exists(directory + configuration_file_name):
         touch(directory + configuration_file_name)

      if attach_listener_on_file_change:
         self.add_event_on_file_change(directory)

   def handler(self, signum, frame):
      self.callback()

   def add_event_on_file_change(self, directory):
      signal.signal(signal.SIGIO, self.handler)
      fd = os.open(directory,  os.O_RDONLY)
      fcntl.fcntl(fd, fcntl.F_SETSIG, 0)
      fcntl.fcntl(fd, fcntl.F_NOTIFY, fcntl.DN_MODIFY )


def touch(fname):
   if os.path.exists(fname):
      os.utime(fname, None)
   else:
      open(fname, 'a').close()

