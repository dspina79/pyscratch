class Account:
    def __init__(self, firstName, lastName, emailAddress, age):
        super().__init__()
        self.age = age
        self.firstname = firstName
        self.lastname = lastName
        self.email = emailAddress

    def reset(self, firstName, lastName, emailAddress, age):
        self.age = age
        self.firstname = firstName
        self.lastname = lastName
        self.email = emailAddress

class AccountManager:
    def __init__(self):
        super().__init__()
        self.accounts = []
    
    def append(self, acct):
        self.accounts.append(acct)