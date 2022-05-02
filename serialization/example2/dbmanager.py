import accounts
import pickle

class DatabaseManager:
    def __init__(self, dbpath):
        super().__init__()
        self.path = dbpath
        self.manager = None

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


        