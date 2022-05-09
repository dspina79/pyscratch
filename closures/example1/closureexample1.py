def print_message(msg):
    def printer():
        print(msg)
    
    return printer

def other_greeter(greeting):
    def greet(name):
        print(greeting, name)
    return greet

print_dean = print_message("Dean")
print_dean() # outputs Dean


greeter1 = other_greeter("Hola")
greeter2 = other_greeter("Hello")

greeter1("Dean") # outputs Hola Dean
greeter2("Dean") # outputs Hello Dean
