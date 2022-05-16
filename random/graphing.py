import random as r

numbs = {}
for i in range(0, 100):
    x = r.randint(1, 10)
    n = numbs.get(x, 0)
    n += 1

    numbs[x] = n

print(numbs)