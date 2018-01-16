import logging

from configuration_handler import configuration_handler



#Code

loader = configuration_handler()

loader.load_configuration()

print("Hello")


for i in xrange(1000):
 pass
