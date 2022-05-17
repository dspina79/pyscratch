class MyError(Exception):
    def __init__(self):
        super().__init__()


class InvalidNameError(Exception):
    def __init__(self, message):
        self.message = message
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if args.__len__() > 0:
            self.message = args[0]
        else:
            self.message = "Unknown details"
try:
    x = 10
    if x < 20:
        raise MyError
    else:
        print('My error was not raised.')
except MyError:
    print('My Error was raised')


try:
    inpropername = 'Divad'
    if inpropername != 'David':
        raise InvalidNameError("You cannot use a name like that.")
    else:
        print("Welcome aboard")
except InvalidNameError as err:
    print("The error was thrown")
    print(err.message)