#!/usr/bin/python

import requests,json
resp=requests.get(url='http://192.168.1.4/api/40j7Sjw5zpf11DdS4IQfza39nqbZUKEGmX0WeIsb/sensors/23')
res=json.loads(resp.text)
print res['state']['presence']

# Specify the number of consumer and producer threads
numconsumers = 2
numproducers = 4
nummessages = 4
 
import thread as thread, Queue as queue, time
 
# Create a lock so that only one thread writes to the console at a time
safeprint = thread.allocate_lock()
 
# Create a queue object
dataQueue = queue.Queue()
 
 
# Function called by the producer thread
def producer(idnum):
    # Produce 4 messages to place on the queue
    for msgnum in range(nummessages):
        # Simulate a delay
        time.sleep(idnum)
 
        # Put a String on the queue
        dataQueue.put('[producer id={}, count={}]'.format(idnum, msgnum))
 
 
# Function called by the consumer threads
def consumer(idnum):
    # Create an infinite loop
    while True:
        # Simulate a delay
        time.sleep(0.1)
        try:
            # Attempt to get data from the queue. Note that
            # dataQueue.get() will block this thread's execution
            # until data is available
            data = dataQueue.get()
        except queue.Empty:
            pass
        else:
            # Acquire a lock on the console
            with safeprint:
                # Print the data created by the producer thread
                print('consumer ', idnum, ' got => ', data)
 
 
if __name__ == '__main__':
    # Create consumers
    for i in range(numconsumers):
        thread.start_new_thread(consumer, (i,))
         
    # Create producers
    for i in range(numproducers):
        thread.start_new_thread(producer, (i,))
         
    # Simulate a delay
    time.sleep(((numproducers - 1) * nummessages) + 1)
     
    # Exit the program
    print('Main thread exit')
