import time

def countdown(sec):
    while sec:
        print(sec, end="\r")
        time.sleep(1)
        sec -= 1


t = input("Enter the time in seconds")
countdown(int(t))