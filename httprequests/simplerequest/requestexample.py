import pip._vendor.requests as requests

def get_toto(id):
    url = "https://jsonplaceholder.typicode.com/todos/" + str(id)
    resp = requests.get(url)
    print(resp.json())


get_toto(2)