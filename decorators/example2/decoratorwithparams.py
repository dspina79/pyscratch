import functools

def param_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting function", func.__name__)
        rv = func(*args, **kwargs)
        print("Ending function with result ", rv)
    return wrapper

@param_decorator
def square(a):
    return a * a

@param_decorator
def add(a, b):
    return a + b

square(14)
add(10, 20)