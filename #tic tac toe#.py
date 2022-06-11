#tic tac toe#

import random

def main():

    wl = False
    #creating player
    
    # print('what color do you want to be?')
    # try:
    #     answer = input('X or O')
    #     assert answer.lower == 'x' or answer.lower == 'o'
    # except:
    #     print('please enter an X or an O')

    #player = answer.lower()

    player = 'x'

    if player == 'x':
        ai = 'o'
    else:
        ai = 'x'

    #creating board
    nine = create_9()

    if player == 'x':
        count = 1
    else:
        count = 2
    
    

    while wl == False:
        create_board(nine)
        if count == 1:
            player = 'x'
            nine, count = make_move(nine, player, count)
        else:
            player = 'o'
            nine, count = make_move(nine, player, count)
        # else:
        #     nine, count = AI_move(nine, ai, player, count)
        result = win_scenerio(nine)
        if result == True:
            wl = True
    if count == 2:
        print (' X has won!!')
    else:
        print ('O has won!!!')







    
    
    
def create_9():
    nine = []
    con = 1
    for i in range(9):
        nine.append(con)
        con += 1
    return nine





def make_move(nine1, player, count):
    moved = False
    print ('please make a move')
    def inputing():
        try:
            move = int(input('--'))
        except:
            print ('please enter a number between 1 and 9')

        return move
    
    while moved == False:
        move = inputing()
        check = isitclear(move, nine1)
        if check == True:
            nine1[move - 1] = player
            if count == 1:
                count = 2
            elif count == 2:
                count = 1
            return nine1 , count
        else:
            print('spot already taken')    
    for item in nine:
        if item == move:
            item = player

    
def next_player(player):
    if player == "" or player == 'o':
        player = "x"
    elif player == 'x':
        player == "o"

def chooseRandomMoveFromList(nine, movesList):

    possibleMoves = []
    for i in movesList:
        if isitclear(i, nine)== True:
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def create_board(nine):
    print (f'{nine[0]} | {nine[1]} | {nine[2]}')
    print (f'{nine[3]} | {nine[4]} | {nine[5]}')
    print (f'{nine[6]} | {nine[7]} | {nine[8]}')

def getcopy(nine):
    list = nine
    return list

def isitclear(move, nine):
    if nine[int(move)-1] == 'x' or nine[int(move)-1] == 'o':
        return False
    else:
        return True

def isitclear_AI(move, nine):
    if nine[int(move)] == 'x' or nine[int(move)] == 'o':
        return False
    else:
        return True

def win_scenerio(nine):

    # for item in nine:
    #     # if item != 

    if (nine[0] == nine[1] == nine[2]):
        return True
    elif (nine[3] == nine[4] == nine[5]):
        return True
    elif (nine[6] == nine[7] == nine[8]):
        return True
    elif (nine[0] == nine[3] == nine[6]):
        return True
    elif (nine[1] == nine[4] == nine[7]):
        return True
    elif (nine[2] == nine[5] == nine[8]):
        return True
    elif (nine[0] == nine[4] == nine[8]):
        return True
    elif (nine[2] == nine[4] == nine[6]):
        return True        
    else:
        return False

def AI_move(nine, ai, player, count):

    move = ''

    def make_move_ai(board,num, AI):
        board[int(num)] = AI
        return board

    def could_win(nine, ai):

        for i in range(9):
            copy = getcopy(nine)
            if isitclear_AI(i, copy) == True:
               
                copy = make_move_ai(copy, i, ai)
                if win_scenerio(copy) == True:
                    return i
                    break

    def could_lose(nine, player):
        for i in range(9):
            copy = getcopy(nine)
            if isitclear_AI(i, nine) == True:
                copy = make_move_ai(copy, i, player)
                if win_scenerio(copy) == True:
                    return i

    def checkcorner(nine):
        move = chooseRandomMoveFromList(nine, [0,2,6,8])
        if move != None:
            return move  

    def pickmiddle(nine):
        if isitclear_AI(4, nine) == True:
            return 4
            

    def checkside(nine):
        move = chooseRandomMoveFromList(nine, [1,3,5,7])
        if move != None:
            return move 


    def AI_main(nine, ai, move):
        if move == '':
            move = could_win(nine, ai)
            if move != None:
                next = make_move_ai(nine, move, ai)
                count = 1
                return next
                
        if move == '':
            move = could_lose(nine, player)
            if move != None:
                next = make_move_ai(nine, move, ai)
                count = 1
                return next
        if move == '':        
            move = checkcorner(nine)
            if move != None:
                next = make_move_ai(nine, move, ai)
                count = 1
                return next
        if move == '':
            move = pickmiddle(nine)
            if move != None:
                next = make_move_ai(nine, move, ai)
                count = 1
                return next
        if move == '':
            move = checkside(nine)
            if move != None:
                next = make_move_ai(nine, move, ai)
                count = 1
                return next
    nine = AI_main(nine, ai, move)
    count = 1

    return nine, count
    
    

    

if __name__ == "__main__":
    main()