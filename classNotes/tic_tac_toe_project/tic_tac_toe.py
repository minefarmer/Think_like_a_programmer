'''         TicTacToe   Intro
Working with board.  line 25
Marking a board with X and O.  line 50
Setting up Winning Conditions  line 80
Checking a tie condition       line 200
Who goes first(A Toss)         line 200 




Website of the tic-tac-toe-game.

    https://www.calculatorcat.com/games/tic_tac_toe.phtml

+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+
|   |   |   |
+---+---+---+


'''
# def showBoard():
#     print("+---+---+---+")
#     print("|",board[0],  "|",board[1], "|",board[2], "|")
#     print("+---+---+---+")
#     print("|",board[3],  "|",board[4], "|",board[5], "|")
#     print("+---+---+---+")
#     print("|",board[6],  "|",board[7], "|",board[8], "|")
#     print("+---+---+---+")
    
    
# board = [ ' ', ' ', ' ',
#           ' ', ' ', ' ',
#           ' ', ' ', ' ']
# showBoard()  # board = [' '] * 9
            # +---+---+---+
            # |   |   |   |
            # +---+---+---+
            # |   |   |   |
            # +---+---+---+
            # |   |   |   |
            # +---+---+---+




# Marking a board with X and O. *****************************************************






# while True:
#     while True:
#         X = int(input('Please enter the position (0-9): '))
#         if board[X] == ' ':
#             board[X] = 'X'
#             break
#         else:
#             print("Position is already taken")

#     showBoard()
    
#     while True:
#         O = int(input('Please enter the position (0-9): '))
#         if board[O] == ' ':
#             board[O] = 'O'
#             break
#         else:
#             print("Position is already taken")
            
#     showBoard()
    





    
# Setting up Winning Conditions


# def showBoard():
#     print("+---+---+---+")
#     print("|",board[0],  "|",board[1], "|",board[2], "|")
#     print("+---+---+---+")
#     print("|",board[3],  "|",board[4], "|",board[5], "|")
#     print("+---+---+---+")
#     print("|",board[6],  "|",board[7], "|",board[8], "|")
#     print("+---+---+---+")

# def isWinner(char):
    
#     if board[0] == char and board[1] == char and board[2] == char:
#         return True    
#     elif board[3] == char and board[4] == char and board[5] == char:
#         return True    
#     elif board[6] == char and board[7] == char and board[8] == char:
#         return True
#     print("+---+---+---+")

# def isWinner(char):
    
#     if board[0] == char and board[3] == char and board[6] == char:
#         return True    
#     elif board[1] == char and board[4] == char and board[7] == char:
#         return True    
#     elif board[2] == char and board[5] == char and board[8] == char:
#         return True
        
#     elif board[0] == char and board[4] == char and board[8] == char:
#         return True    
#     elif board[2] == char and board[4] == char and board[6] == char:
#         return True
#     else:
#         return False
    
# board = [ ' ', ' ', ' ',
#           ' ', ' ', ' ',
#           ' ', ' ', ' ']
# showBoard() 














# while True:
#     while True:
#         X = int(input('Player # 1: Please enter the position (0-9): '))
#         if board[X] == ' ':
#             board[X] = 'X'
#             break
#         else:
#             print("Position is already taken")

#     showBoard()
    
#     if isWinner('X'):
#         print("X has won")
#         break
    
#     while True:
#         O = int(input('Player # 2: Please enter the position (0-9): '))
#         if board[O] == ' ':
#             board[O] = 'O'
#             break
#         else:
#             print("Position is already taken")
            
#     showBoard()
    
#     if isWinner('O'):
#         print("O has won")
#         break
    
    
#  Checking a tie condition


























# Checking a tie condition


def showBoard():
    print("+---+---+---+")
    print("|",board[0],  "|",board[1], "|",board[2], "|")
    print("+---+---+---+")
    print("|",board[3],  "|",board[4], "|",board[5], "|")
    print("+---+---+---+")
    print("|",board[6],  "|",board[7], "|",board[8], "|")
    print("+---+---+---+")

def isWinner(char):
    
    if board[0] == char and board[1] == char and board[2] == char:
        return True    
    elif board[3] == char and board[4] == char and board[5] == char:
        return True    
    elif board[6] == char and board[7] == char and board[8] == char:
        return True
    print("+---+---+---+")

def isWinner(char):
    
    if board[0] == char and board[3] == char and board[6] == char:
        return True    
    elif board[1] == char and board[4] == char and board[7] == char:
        return True    
    elif board[2] == char and board[5] == char and board[8] == char:
        return True
        
    elif board[0] == char and board[4] == char and board[8] == char:
        return True    
    elif board[2] == char and board[4] == char and board[6] == char:
        return True
    else:
        return False
    
def isFull():
    if board.count(' ') == 0:
        return True
    else:
        return False
    
    def selectLetter():
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print("Do you want to be x or O?")
            letter = input().upper()
        return letter
    
    def Toss():
        if random.randinet(0, 1) == 0:
            return 'X'
        else:
            return 'O'
        
board = [ ' ', ' ', ' ',
          ' ', ' ', ' ',
          ' ', ' ', ' ']


if selectLetter() == 'X':
    print("You are X")
else:
    print("You are O")

player = []
if Toss() == 'X':
    print("X has won the toss")
    player = ['X', 'O']
else:
    player = ['O', 'X']
    print(('O has won the toss'))
showBoard()

while True:
    while True:
        print(player[0],"\'s turn", end=' ')
        p1 = int(input('Please enter the position (0-9): '))
        if board[p1] == ' ':
            board[p1] = player[0]
            break
        else:
            print("Position is already taken")

    showBoard()
    
    if isWinner(player[O]):
        print("player[O], has won")
        break
    
    if isFull():
        print("Match Tied! ")
        break
    
    while True:
        print(player[0],"\'s turn", end=' ')
        O = int(input('Please enter the position (0-9): '))
        if board[O] == ' ':
            board[O] = [1]
            break
        else:
            print("Position is already taken")
            
    showBoard()
    
    if isWinner(player[1]):
        print("O has won")
        break
    if isFull():
        print("'Match Tied !")
        break
