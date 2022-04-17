class Environment:
    def __init__(self, lifeElements, initialFood):
        self.elements = lifeElements
        self.food = initialFood
        self.deadElements = 0

    def print_status(self):
        if self.elements.__len__ == 0:
            print("Complete extinction")
        else:
            print("There are", self.elements.__len__, "living things with", self.food , "food resources available.")
    
    def add_food(self, food):
        self.food += food
