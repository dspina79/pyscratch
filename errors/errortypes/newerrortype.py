class MyError(Exception):
    def __init__(self):
        super().__init__()


try:
    x = 10
    if x < 20:
        raise MyError
    else:
        print('My error was not raised.')
except MyError:
    print('My Error was raised')