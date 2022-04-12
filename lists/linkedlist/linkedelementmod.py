class ListElement:
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.next_item = None
    
    def setItem(self, item):
        self.next_item = item
    
    def disentangle(self):
        self.next_item = None

    def printList(self):
        print("Current ID: ", self.id)
        current_item = self.next_item
        while current_item != None:
            print("Next Link: ", current_item.id)
            current_item = current_item.next_item
    