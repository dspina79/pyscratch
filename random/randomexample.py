import random as r

LOWER_BOUND = -10
UPPER_BOUND = 10

iteration = 0
items = []
items.append(0)
while iteration < 10:
    internal_check = 0
    item_check = items[-1]
    x = r.randint(LOWER_BOUND, UPPER_BOUND)
    y = r.randint(LOWER_BOUND, UPPER_BOUND)
    internal_check += 1
    while x + y != item_check:
        x = r.randint(LOWER_BOUND, UPPER_BOUND)
        y = r.randint(LOWER_BOUND, UPPER_BOUND)
        internal_check += 1
    print(iteration, internal_check)
    items.append(x)
    items.append(y)
    iteration += 1

print(items)