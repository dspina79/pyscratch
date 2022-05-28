import pip._vendor.requests as requests

class Address:
    def __init__(self, street = "", city = "", state = "", postal = ""):
        self.street = street
        self.city = city
        self.stateProvince = state
        self.postalCode = postal


class User:
    def __init__(self, name, username):
        super().__init__()
        self.username = username
        self.name = name
        self.id = None
        self.emailAddres = ""
        self.address = Address()

    def printout(self):
        print(self.name, "(", self.emailAddres, ")")

    def to_json(self):
        # TODO: Implement
        return {
                "name": self.name,
                "username": self.username,
                "email": self.emailAddres,
                "address": {
                    "street": self.address.street,
                    "suite": "",
                    "city": self.address.city,
                    "zipcode": self.address.postalCode,
                    "geo": {
                        "lat": "",
                        "lng": ""
                    }
                },
                "phone": "",
                "website": "",
                "company": {
                    "name": "",
                    "catchPhrase": "",
                    "bs": ""
                }
            }
    

class UserManager:
    def __init__(self):
        super().__init__()
        self.baseUrl = "https://jsonplaceholder.typicode.com/users"

    def get_user(self, id):
        url = self.baseUrl + "/" + str(id)
        resp = requests.get(url)
        data = resp.json()
        u = User(data["name"], data["username"])
        u.emailAddres = data["email"]
        return u

    def get_all_users(self):
        url = self.baseUrl
        resp = requests.get(url)
        data = resp.json()
        return data

    def create_user(self, usr):
        resp = requests.post(self.baseUrl, json = usr.to_json())
        return resp.json()

mgr = UserManager()
mgr.get_user(1).printout()
mgr.get_user(2).printout()

u = User("Dean Smith", "dsmith")
u.address = Address("123 Anywhere Drive", "Anywhere", "TX", "12345")
u.emailAddres = "dsmith@nowhere.net"
print(mgr.create_user(u))