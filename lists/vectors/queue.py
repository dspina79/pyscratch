class Queue:
    def __init__(self):
        super().__init__()
        self.arr = []
    
    def add(self, item):
        self.arr.append(item)
    
    def pop(self):
        if self.arr.count() > 0:
            return self.arr.pop(0)
        else:
            return None

    def count(self):
        return self.arr.count()

    def print(self):
        print("There are", self.arr.count(), "items in the queue.")
        print(self.arr)

