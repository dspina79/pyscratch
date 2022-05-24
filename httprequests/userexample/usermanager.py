import pip._vendor.requests as requests

class User:
    def __init__(self, firstName, lastName):
        super().__init__()
        self.firstName = firstName
        self.lastName = lastName
        self.id = None
        self.emailAddres = ""
        self.address1 = ""
        self.city = ""
        self.state = ""
        self.postalCode = ""

    def printout(self):
        print(self.lastName, ",", self.firstName, "(", self.emailAddres, ")")


