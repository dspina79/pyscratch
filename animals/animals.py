class Person:
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return 'Person Name: ' + self.name


p1 = Person('Dean')
print(p1)