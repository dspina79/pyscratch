class Circle:
    PI = 3.14159
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def area(self):
        return self.radius * self.radius * self.PI
    
    def circumference(self):
        return self.radius * 2.0 * self.PI

c = Circle(2.234)
print("The area of the circle is ", c.area())
print("The circumference of the cirlce is", c.circumference())
