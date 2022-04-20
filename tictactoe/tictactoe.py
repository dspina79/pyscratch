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
        
    def determine_win(self):
        return False
    
    def checkWin(self, player):
        # win opportunities
        w1 = (self.boardArray[0] == player and self.boardArray[1] == player and self.boardArray[2] == player)
        w2 = (self.boardArray[3] == player and self.boardArray[4] == player and self.boardArray[5] == player)
        w3 = (self.boardArray[6] == player and self.boardArray[7] == player and self.boardArray[6] == player)
        w4 = (self.boardArray[0] == player and self.boardArray[3] == player and self.boardArray[6] == player)
        w5 = (self.boardArray[1] == player and self.boardArray[4] == player and self.boardArray[7] == player)
        w6 = (self.boardArray[2] == player and self.boardArray[5] == player and self.boardArray[8] == player)
        # diagonals
        w7 = (self.boardArray[0] == player and self.boardArray[4] == player and self.boardArray[8] == player)
        w8 = (self.boardArray[2] == player and self.boardArray[4] == player and self.boardArray[6] == player)

b = Board()
b.print_board()