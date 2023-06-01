from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for index in range(3):
        print('+'+'-'*7+'+'+'-'*7+'+'+'-'*7+'+')
        print('|' +' '*7+'|'+' '*7+'|'+' '*7+'|')
        print('|' +' '*3+f'{board[index][0]}'+' '*3+'|',end="")
        print(' '*3+f'{board[index][1]}'+' '*3+'|',end="")
        print(' '*3+f'{board[index][2]}'+' '*3+'|')
        print('|' +' '*7+'|'+' '*7+'|'+' '*7+'|')
    print('+'+'-'*7+'+'+'-'*7+'+'+'-'*7+'+')


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    freeSquares=[]
    index2 = 0
    for index in range(0,9,1):
        if board[index2][index % 3].isdigit():
            freeSquares.append((index2,index%3))
        if index % 3 == 2:
            index2 += 1
    return freeSquares

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    moves = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
    while True:
        #print(board[moves[user][0]][moves[user][1]])
        user=int(input("Enter your move: "))
        if board[moves[user][0]][moves[user][1]].isdigit():
            board[moves[user][0]][moves[user][1]] = 'O'
            break
        else:
            print("Celda ocupada, intenta de nuevo")
    #print(make_list_of_free_fields(board))


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    #continue, tie, you win, or the computer wins
    #Rows
    moves = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
    if (board[0][0] == board[0][1]  == board[0][2]):
        sign=board[0][0]
    elif (board[1][0] == board[1][1]  == board[1][2]):
        sign=board[1][0]
    elif (board[2][0] == board[2][1]  == board[2][2]):
        sign=board[2][0]
    #Columns
    elif (board[0][0] == board[1][0]  == board[2][0]):
        sign=board[0][0]
    elif (board[0][1] == board[1][1]  == board[2][1]):
        sign=board[0][1]
    elif (board[2][0] == board[1][1]  == board[2][2]):
        sign=board[2][0]
    #diagonales
    elif (board[0][0] == board[1][1]  == board[2][2]):
        sign=board[0][0]
    elif (board[0][2] == board[1][1]  == board[2][0]):
        sign=board[0][2]
    #print (f"Winning so far {sign}")
    return sign


def draw_move(board):
    # The function draws the computer's move and updates the board.
    moves = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
    while True:
        game=randrange(1,10)
        #print(board[moves[user][0]][moves[user][1]])
        if board[moves[game][0]][moves[game][1]].isdigit():
            board[moves[game][0]][moves[game][1]] = 'X'
            break
    #print(make_list_of_free_fields(board))


def init_board():
    #Function initialize board variable with numbers
    board = [[0 for col in range(3)] for row in range(3)]
    index2 = 0
    for index in range(0,9,1):
        board[index2][index % 3] = str(index+1)
        if index % 3 == 2:
            index2 += 1
    board[1][1] = 'X'
    #print(board)
    return board

board = init_board()
turnos = 0
sign = "continue"
display_board(board)
while turnos < 8 and sign == "continue":
    #print (f"turno {turnos} y version {turnos%2}")
    if turnos %2 == 0: #user
        enter_move(board)
    elif turnos %2 == 1:
        draw_move(board)
    turnos += 1
    display_board(board)
    if turnos > 3:
        sign = victory_for(board, sign)
    if sign != "continue":
        break    
if turnos == 8 and sign == "continue":
    print("The game has tied")
elif sign == "X":
    print("The computer wins")
elif sign == "O":
    print("You win")

#Cisco Academy version
'''
from random import randrange


def display_board(board):
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")


def enter_move(board):
	ok = False	# fake assumption - we need it to enter the loop
	while not ok:
		move = input("Enter your move: ") 
		ok = len(move) == 1 and move >= '1' and move <= '9' # is user's input valid?
		if not ok:
			print("Bad move - repeat your input!") # no, it isn't - do the input again
			continue
		move = int(move) - 1 	# cell's number from 0 to 8
		row = move // 3 	# cell's row
		col = move % 3		# cell's column
		sign = board[row][col]	# check the selected square
		ok = sign not in ['O','X'] 
		if not ok:	# it's occupied - to the input again
			print("Field already occupied - repeat your input!")
			continue
	board[row][col] = 'O' 	# set '0' at the selected square


def make_list_of_free_fields(board):
	free = []	# the list is empty initially
	for row in range(3): # iterate through rows
		for col in range(3): # iterate through columns
			if board[row][col] not in ['O','X']: # is the cell free?
				free.append((row,col)) # yes, it is - append new tuple to the list
	return free


def victory_for(board,sgn):
	if sgn == "X":	# are we looking for X?
		who = 'me'	# yes - it's computer's side
	elif sgn == "O": # ... or for O?
		who = 'you'	# yes - it's our side
	else:
		who = None	# we should not fall here!
	cross1 = cross2 = True  # for diagonals
	for rc in range(3):
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# check row rc
			return who
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc
			return who
		if board[rc][rc] != sgn: # check 1st diagonal
			cross1 = False
		if board[2 - rc][2 - rc] != sgn: # check 2nd diagonal
			cross2 = False
	if cross1 or cross2:
		return who
	return None


def draw_move(board):
	free = make_list_of_free_fields(board) # make a list of free fields
	cnt = len(free)
	if cnt > 0:	# if the list is not empty, choose a place for 'X' and set it
		this = randrange(cnt)
		row, col = free[this]
		board[row][col] = 'X'


board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # make an empty board
board[1][1] = 'X' # set first 'X' in the middle
free = make_list_of_free_fields(board)
human_turn = True # which turn is it now?
while len(free):
	display_board(board)
	if human_turn:
		enter_move(board)
		victor = victory_for(board,'O')
	else:	
		draw_move(board)
		victor = victory_for(board,'X')
	if victor != None:
		break
	human_turn = not human_turn		
	free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
	print("You won!")
elif victor == 'me':
	print("I won")
else:
	print("Tie!")
'''