import _sha256 as h
import json as j

class Person:
    def __init__(self, first_name, last_name, email):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    
    def my_hash(self):
        self_val = j.dumps(self.__dict__, sort_keys=True)
        return h.sha256(self_val.encode()).hexdigest()

p = Person('Dean', 'Smith', 'dsmith@nowhere.net')
print(p.my_hash())