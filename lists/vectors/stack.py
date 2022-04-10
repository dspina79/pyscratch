class Stack:
    def __init__(self):
        super().__init__()
        self.arr = []
    
    def add(self, item):
        self.arr.insert(0, item)

    def pop(self):
        if self.arr.__len__() > 0:
            return self.arr.pop(0)
        else:
            return None
    
    def stacktrace(self):
        print("Stack Tace")
        for i in range(0, self.arr.__len__()):
            print(self.arr[i])


s = Stack()
s.add("One")
s.add("Two")
s.add("Three")
s.add("Four")

s.stacktrace()

popped_item = s.pop()
print("Popped", popped_item)
s.stacktrace()