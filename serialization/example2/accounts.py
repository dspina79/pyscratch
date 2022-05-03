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

    def write_out(self):
        return self.lastname + ', ' + self.firstname

class AccountManager:
    def __init__(self):
        super().__init__()
        self.accounts = []
    
    def append(self, acct):
        self.accounts.append(acct)
    
    def write_summary(self):
        print('Contains ', self.accounts.__len__(), ' records:')
        for acct in self.accounts:
            print('\t', acct.write_out())