def simple_decorator(func):
    def wrapper():
        print("Calling the function")
        func()
        print("The function has been called")
    return wrapper

@simple_decorator
def print_something():
    print("Something")

print_something()