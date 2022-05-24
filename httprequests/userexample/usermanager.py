import pip._vendor.requests as requests

class User:
    def __init__(self, name, username):
        super().__init__()
        self.username = username
        self.name = name
        self.id = None
        self.emailAddres = ""
        self.address1 = ""
        self.city = ""
        self.state = ""
        self.postalCode = ""

    def printout(self):
        print(self.name, "(", self.emailAddres, ")")


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
        
mgr = UserManager()
mgr.get_user(1).printout()
mgr.get_user(2).printout()