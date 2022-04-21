class Board:
    def __init__(self):
        super().__init__()
        self.boardArray = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.gameWon = False

    def reset(self):
        self.boardArray = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.gameWon = False
        
    def set_demo(self):
        for i in range(0, self.boardArray.__len__()):
            self.boardArray[i] = 'X'
        
    def print_board(self):
        print(self.boardArray[0], "|", self.boardArray[1], "|", self.boardArray[2])
        print("_________")
        print(self.boardArray[3], "|", self.boardArray[4], "|", self.boardArray[5])
        print("_________")
        print(self.boardArray[6], "|", self.boardArray[7], "|", self.boardArray[8])
        
    def check_win(self, player):
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
        return w1 or w2 or w3 or w4 or w5 or w6 or w7 or w8

    def enter_element(self, player, position):
        self.boardArray[position] = player
        self.print_board()
        if self.check_win(player):
            print("Plaer", player, "wins!!")
            self.reset()
            self.gameWon = True

    def determine_next_best_move(self):
        # for now, just pick a random entry
        if self.boardArray[4] == ' ':
            return 4
        else:
            next_place = -1
            for i in range(0, 8):
                if self.boardArray[i] == ' ':
                    next_place = i
                    break
            return next_place

    def play_round(self):
        players = ["X", "O"]
        positionIndex = 0
        while not self.gameWon:
            player = players[positionIndex % 2]
            pos = int(input("Player " + player + " enter position: "))
            while pos < 0 or pos > 8 or self.boardArray[pos] != ' ':
                print("Invalid choice")
                pos = int(input("Player " + player + " enter position: "))
                
            self.enter_element(player, pos)
            positionIndex += 1

b = Board()
b.play_round()