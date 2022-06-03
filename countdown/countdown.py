import time

def countdown(totalsec):
    while totalsec:
        min, sec = divmod(totalsec, 60)
        timer = "{:02d}:{:02d}".format(min, sec)
        print(timer, end="\r")
        time.sleep(1)
        totalsec -= 1
    print("BEEP BEEP")

t = input("Enter the time in seconds: ")
countdown(int(t))