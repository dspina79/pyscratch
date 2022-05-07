# Partial functions allow for 
# fixing parameters
from functools import partial

def greet(greeting, name):
    print(greeting, name)


hellogreet = partial(greet, 'Hello')

greet('Buenos dias', 'Dean')
hellogreet('Don')

# outputs
#Buenos dias Dean
#Hello Don