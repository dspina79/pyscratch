class Queue:
    def __init__(self):
        super().__init__()
        self.arr = []
    
    def add(self, item):
        self.arr.append(item)
    
    def pop(self):
        if self.arr.__len__() > 0:
            return self.arr.pop(0)
        else:
            return None

    def count(self):
        return self.arr.__len__()

    def print(self):
        print("There are", self.arr.__len__(), "items in the queue.")
        print(self.arr)

q = Queue()
q.add("Ted")
q.add("Carmen")
q.add("Steve")
q.add("Linda")
q.add("Bryce")

q.print()
while q.count() > 0:
    item = q.pop()
    print(item, "came off the queue")
    q.print()

