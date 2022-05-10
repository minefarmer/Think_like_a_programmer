import random
# The Game Board
def showBoard():
    print("+---+---+---+")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("+---+---+---+")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("+---+---+---+")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("+---+---+---+")

def isWinner(char):
    #horizental check
   if board[0] == char and board[1] == char and board[2] == char:
       return True
   elif board[3] == char and board[4] == char and board[5] == char:
       return True
   elif board[6] == char and board[7] == char and board[8] == char:
       return True

   # vertical check
   if board[0] == char and board[3] == char and board[6] == char:
       return True
   elif board[1] == char and board[4] == char and board[7] == char:
       return True
   elif board[2] == char and board[5] == char and board[8] == char:
       return True

   # diagonal check
   if board[0] == char and board[4] == char and board[8] == char:
       return True
   elif board[2] == char and board[4] == char and board[6] == char:
       return True

#to check if the board has been filled or not
def isFull():
    if board.count(' ') == 0:
        return True
    else:
        return False

def selectLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    return letter

def toss(char):
    if random.randint(0, 1) == char:
        return 0
    else:
        return 1

#Main program start here
done = False
while not done:
    board = [' '] * 9

# choosing letter for players
    player = []
    player1, player2 = '', ''
    if selectLetter() == 'X':
        player = ['X', 'O']
    else:
        player = ['O', 'X']

# Toss
    print('*'*5, 'TOSS', '*'*5)
    print(player[0], 'please type 1 for head or 0 for tail')
    x = int(input('>>> '))
    if toss(x) == x:
        print(player[0], 'won the toss')
        player1 = player[0]
        player2 = player[1]
    else:
        print(player[1], 'won the toss')
        player1 = player[1]
        player2 = player[0]

    while True:  #inner game loop
        showBoard()
        while True:
            print(player1,'\'s turn. ', end = '')
            X = int(input("Please Enter position: "))
            if board[X] != 'X' and board[X] != 'O':
                board[X] = player1
                break
            else:
                print('Already Taken')

        #check whether X Wins
        if isWinner(player1):
            showBoard()
            print(player1, 'Won!')
            break

        if isFull():
            showBoard()
            print('Board is full..No one wins')
            break

        showBoard()

        while True:
            print(player2,'\'s turn. ', end = '')
            O = int(input("Please Enter position: "))
            if board[O] != 'X' and board[O] != 'O':
                board[O] = player2
                break
            else:
                print('Already Taken!')

        if isWinner(player2):
            showBoard()
            print(player2, 'won!')
            break

        if isFull():
            showBoard()
            print('Board is full..No one wins')
            break


    option = input('Do you want to continue? (y/n)')

    if option.lower() == 'y':
        continue
    else:
        print('Thank you for playing Tic Tac Toe. See you again :)')
        break





