import time
import random as r

def phrase_match(phrase):
    iteration = 0
    l = phrase.__len__()
    found = False

    while not found:
        iteration += 1
        test_phrase = ''
        for x in range(0, l):
            rcn = r.randint(0, 27)
            c = chr(97 + rcn)
            if rcn >= 26:
                c = ' '
            test_phrase += c
        if test_phrase == phrase:
            print('This worked after', iteration, 'iterations')
            found = True


phrase_match('to be') # took 9,592,920 iterations on first

# to be or not to be (n=18) would have a possible value of 5.8 x 10^25
# or 58,000,000,000,000,000,000,000,000
# 58 septillion?