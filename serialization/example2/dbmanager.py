import accounts as a
import pickle

class DatabaseManager:
    def __init__(self, dbpath):
        super().__init__()
        self.path = dbpath
        self.refresh_data()

    def quick_add(self, acct):
        self.manager.append(acct)
        self.write_data()
        self.refresh_data()

    def refresh_data(self):
        try:
            f = open(self.path, 'rb')
            self.manager = pickle.load(f)
            f.close()
        except FileNotFoundError:
            self.manager = a.AccountManager()

        return self.manager
    
    def write_data(self):
        if self.manager != None:
            f = open(self.path, 'wb')
            pickle.dump(self.manager, f)
            f.close()


dmgr = DatabaseManager('serialization/example2/maindata.txt')
acctmgr = dmgr.manager
acct1 = a.Account('Dean', 'Williams', 'dwilliams@nowhere.net', 53)
acct2 = a.Account('Sharon', 'Folsom', 'sforlsm@nowhere.net', 23)
acct3 = a.Account('Ted', 'Quinn', 'tquinn@nowhere.net', 32)
acctmgr.append(acct1)
acctmgr.append(acct2)
dmgr.write_data()

acctmgr.append(acct3)
acctmgr.write_summary()

acctmgr = dmgr.refresh_data()
acctmgr.write_summary()
