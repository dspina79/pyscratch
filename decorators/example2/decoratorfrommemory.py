import functools

def my_wrapper(func):
    @functools.wraps(func)
    def wrapper(*args, **kargs):
        print("Running", func.__name__)
        retval = func(*args, **kargs)
        print("The result is", retval)
    return wrapper

@my_wrapper
def add(x, y):
    return x + y

add(10, 20)