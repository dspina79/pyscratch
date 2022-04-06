# Life of Pi

class LivingThing:
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def speak(self):
        print(self.name, "says hello in its own way.")

class Monera(LivingThing):
    def __init__(self, name):
        super().__init__(name)
        self.cells = 1
    
    def divide(self):
        kid_name = self.name + "'s kid"
        print("Dividing and creating", kid_name)
        return Monera(kid_name)

class Animal(LivingThing):
    def __init__(self, name):
        super().__init__(name)

    def locomote(self):
        print(self.name, "moves")

imp = LivingThing("Ted")
imp.speak()

monte = Monera("Monte")
monte.speak()
child_1 = monte.divide()
child_1.speak()

sebastian = Animal("Sebastian")
sebastian.speak()
sebastian.locomote()