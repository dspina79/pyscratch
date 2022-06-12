class Person:
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.rank = 0

    def __str__(self):
        return 'Person Name: ' + self.name

    def __eq__(self, value):
        return self.name == value.name and self.rank == value.rank
    
    def __gt__(self, value):
        return self.rank < value.rank

p1 = Person('Dean')
p1.rank = 5

p2 = Person('Dean')
p2.rank = 5

p3 = Person('Janice')
p3.rank = 40

print(p1)
print("Is P1 = P2?", p1 == p2)
print("Is P1 > P3?", p1 > p3)


