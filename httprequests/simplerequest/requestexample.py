import pip._vendor.requests as requests

class Todo:
    def __init__(self):
        super().__init__()
        self.userId = 0
        self.title = ""
        self.completed = False

def get_todo(id):
    url = "https://jsonplaceholder.typicode.com/todos/" + str(id)
    resp = requests.get(url)
    print(resp.json())
    data = resp.json()
    print(data['title'])

def get_all():
    url = "https://jsonplaceholder.typicode.com/todos/"
    resp = requests.get(url)
    data = resp.json()
    print("Returned", data.__len__(), "records")

def make_todo(userid, title, completed):
    body = {"userId": userid, "title": title, "completed": completed}
    url = "https://jsonplaceholder.typicode.com/todos"
    resp = requests.post(url, data = body)
    data = resp.json()
    return data["id"]

# get_todo(2)
# result = make_todo(1, "Another Test", False)
# print(result)

get_all()