# Imports
from smart_queue import *
from random import randint
from time import sleep

# Create SmartQueue instance
queue = SmartQueue()

# Define our function
def SomeLongCalculation():
    sleep(1)
    return randint(100, 999)

# Create 5 tasks, add callback that will print results when done
for i in range(5):
    queue.push(Task(SomeLongCalculation, lambda x: print('Calculation done:', x)))

# Start loop
print('Starting loop')
queue.start()
print('Started')

# Wait some time
sleep(3.5)

# Stop loop
print('Stopping loop')
queue.stop(True)  # `block` is set to True, to wait for current task to finish executing
print('Done')