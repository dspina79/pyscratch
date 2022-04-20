class Board:
    def __init__(self):
        super().__init__()
        self.boardArray = ['', '', '', '', '', '', '', '', '']
    
    def set_demo(self):
        for i in range(0, self.boardArray.__len__()):
            self.boardArray[i] = 'X'
        
    def print_board(self):
        print(self.boardArray[0], "|", self.boardArray[1], "|", self.boardArray[2])
        print("_________")
        print(self.boardArray[3], "|", self.boardArray[4], "|", self.boardArray[5])
        print("_________")
        print(self.boardArray[6], "|", self.boardArray[7], "|", self.boardArray[8])
        

b = Board()
b.print_board()