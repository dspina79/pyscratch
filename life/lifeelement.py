class Life:
    def __init__(self):
        super().__init__()
        self.complexity = 1
        self.lifespan = 0.01
    
    def foodRequirement(self):
        return self.complexity * 1.63 

    def eat(self, amt):
        self.foodAmount += amt

    def metabolize(self):
        self.foodAmount -= self.foodRequirement()
        self.age += 0.001

    def is_living(self):
        return (self.age < self.lifespan) and self.foodAmount > (self.foodRequirement * -2)

    def reproduce(self):
        return Life()

    def pulse(self, foodAmt):
        if (self.is_living()):
            self.eat(foodAmt)
            self.metabolize()
            return 0
        else:
            return self.foodAmount



