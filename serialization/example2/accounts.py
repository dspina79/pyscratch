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
    
    def matchex(self):
        return self.firstname + "-" + self.lastname + "_" + self.email

    def write_out(self):
        return self.lastname + ', ' + self.firstname

class AccountManager:
    def __init__(self):
        super().__init__()
        self.accounts = []
    
    def find_index_of(self, firstName, lastName):
        index = -1
        for i in range(0, self.accounts.__len__()):
            acct = self.accounts[i]
            if acct.firstname == firstName and acct.lastname == lastName:
                index = i
                break
        return index
    
    def get_index_of(self, searchAcct):
        index = -1

        for i in range(0, self.accounts.__len__()):
            if searchAcct.matchex() == self.accounts[i].matchex():
                index = i
                break
        
        return index

    def append(self, acct):
        self.accounts.append(acct)
    
    def write_summary(self):
        print('Contains ', self.accounts.__len__(), ' records:')
        for acct in self.accounts:
            print('\t', acct.write_out())