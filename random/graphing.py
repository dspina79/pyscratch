import random as r

MAX_INT = 10
numbs = {}

for i in range(1, MAX_INT + 1):
    numbs[i] = 0

for i in range(0, 10000):
    x = r.randint(1, MAX_INT)
    n = numbs.get(x, 0)
    n += 1
    numbs[x] = n

print(numbs)