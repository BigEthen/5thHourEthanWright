#name Ethan Wright
#Class 5 hour
#playground

user =  input('are you ready for the test')
print("ok")
for i in range(10):
    print('bob')
user = input('how many bob?')

print("yes" , 10)
print("give me a number")
x= input (" ")
print("give me another number")
y= input("")
sum = int(x) * int(y)
print(sum)

print('tic tac toe pick a person to play with')

class Board:
    def __init__(self):
        self.board = [[' ', '1', '2', '3'],
                      ['a', '-', '-', '-'],
                      ['b', '-', '-', '-'],
                      ['c', '-', '-', '-']]

    def place_marker(self, row, col, marker):
        row = ord(row) - ord('a') + 1
        col = int(col)
        if self.board[row][col] != '-':
            raise ValueError('Non empty board position')
        self.board[row][col] = marker

    def check_winner(self):
        if ((self.board[1][1] == self.board[1][2] == self.board[1][3] != '-') or
            (self.board[2][1] == self.board[2][2] == self.board[2][3] != '-') or
            (self.board[3][1] == self.board[3][2] == self.board[3][3] != '-') or
            (self.board[1][1] == self.board[2][1] == self.board[3][1] != '-') or
            (self.board[1][2] == self.board[2][2] == self.board[3][2] != '-') or
            (self.board[1][3] == self.board[2][3] == self.board[3][3] != '-') or
            (self.board[1][1] == self.board[2][2] == self.board[3][3] != '-') or
            (self.board[1][3] == self.board[2][2] == self.board[3][1] != '-')):
            return True
        return False

    def __str__(self):
        return '\n'.join(str(row) for row in self.board)

class TicTacToe:
    def __init__(self):
        self.turn = 0
        self.board = Board()

    def which_player(self):
        return 'x' if self.turn % 2 == 0 else 'o'

    def execute_turn(self, row, col):
        marker = self.which_player()
        self.board.place_marker(row, col, marker)
        self.turn += 1
        return self.board.check_winner()

def run_game():
    ttt = TicTacToe()
    print(ttt.board)
    while True:   # should check to see if the board is full
        row, col = input('Where would you like to place your marker? Enter as coordinates (ex. a1.)')
        try:
            if ttt.execute_turn(row, col) == True:
                break
        except ValueError as e:
            print(e)
            print("Try again!!")
        print(ttt.board)
    print("!!!!!!!!!!!!!!!!!!!!!!!WINNER!!!!!!!!!!!!!!!!!!!!!!!")

run_game()


