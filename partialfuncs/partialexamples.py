# Partial functions allow for 
# fixing parameters
from functools import partial

def greet(greeting, name):
    print(greeting, name)

# define a partial on the greet
# function and fix the first param
hellogreet = partial(greet, 'Hello')

greet('Buenos dias', 'Dean')
hellogreet('Don')

# outputs
#Buenos dias Dean
#Hello Don