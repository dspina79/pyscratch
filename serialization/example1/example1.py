import pickle

class User:
    def __init__(self, firstname, lastname, username):
        super().__init__()
        self.firstname = firstname
        self.lastname = lastname
        self.username = username

# serialization
f = open('serialization/example1/userinfo.txt', 'wb')
u = User('Dean', 'Smith', 'dsmith')

pickle.dump(u, f)

f.close()

# deserialization

f2 = open('serialization/example1/userinfo.txt', 'rb')
u2 = pickle.load(f2)
print(u2.lastname)

f2.close()