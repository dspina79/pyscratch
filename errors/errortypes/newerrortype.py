class MyError(Exception):
    def __init__(self):
        super().__init__()


class InvalidNameError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
        raise InvalidNameError("You cannot use a name linke that.")
    else:
        print("Welcome aboard")
except InvalidNameError:
    print(InvalidNameError.args)