import random as r

def is_prime(x):
    isprime = True
    if x >= 2:
        if x == 2:
            return True
        elif x % 2 == 1:
            for i in range(2, x-1):
                if x % i == 0:
                    isprime = False
        else:
            isprime = False    
    return isprime
# generate the sequences x times and find out when the 
# first prime is generated
sum_lengths = 0
total_iterations = 2000
for i in range(0, total_iterations):
    sequence = []
    sequence.append(r.randint(1, 10000))
    while not is_prime(sequence[-1]):
        sequence.append(r.randint(1, 10000))

    print("There were:", sequence.__len__(), "iterations before a prime was found: ", sequence[-1])
    sum_lengths += sequence.__len__()

average = sum_lengths / total_iterations
print("The average was:", average)