import time as t

def countdown(high):
    while high > 0:
        print(high)
        t.sleep(1)
        high -= 1

countdown(15)
        