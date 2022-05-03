import accounts as a
import pickle

class DatabaseManager:
    def __init__(self, dbpath):
        super().__init__()
        self.path = dbpath
        self.manager = a.AccountManager()

    def refresh_data(self):
        f = open(self.path, 'rb')
        self.manager = pickle.load(f)
        f.close()
        return manager
    
    def write_data(self):
        if self.manager != None:
            f = open(self.path, 'wb')
            pickle.dump(self.manager, f)
            f.close()


dmgr = DatabaseManager('serialization/example2/maindata.txt')
acctmgr = dmgr.manager
acct1 = a.Account('Dean', 'Williams', 'dwilliams@nowhere.net', 53)
acct2 = a.Account('Sharon', 'Folsom', 'sforlsm@nowhere.net', 23)
acctmgr.append(acct1)
acctmgr.append(acct2)
dmgr.write_data()        