import time as t
import os

def cls():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        comamnd = 'cls'
    os.system(command)

def countdown(high):
    while high > 0:
        cls() # clear the console
        print(high)
        t.sleep(1)
        high -= 1

countdown(15)
        