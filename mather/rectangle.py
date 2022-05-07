class Rectangle:
    def __init__(self, width, height):
        super().__init__()
        self.height = height
        self.width = width
    
    def isSquare(self):
        return self.width == self.height
    
    def area(self):
        return self.width * self.height
    
    def gitter(self):
        return 2 * self.width + self.height


s = Rectangle(4, 4)
r = Rectangle(3, 4)

print("s.isSquare:", s.isSquare())
print("s.area:", s.area())
print("s.perimter:", s.perimeter())

print("r.isSquare:", r.isSquare())
print("r.area:", r.area())
print("r.perimter:", r.perimeter())