#MUSA HAMWALA ~ 08.05.2016

import random
counter_pos_x = 0
counter_pos_previous_x = 0
counter_pos_y = 0
counter_pos_previous_y = 0
counter_x  = '{:<4}'.format('{x}')
counter_y  = '{:<4}'.format('{y}')
player_one_roll = 0
player_two_roll = 0
player_1 = 0
player_2 = 0
user_input = 0
user_input_2 = 0
player_1_points = 0
player_2_points = 0
game_rules = ('''Take it in turns to roll the dice. Your counter will move forward the number of spaces shown on the dice.
If your counter lands at the bottom of a ladder, you will move up to the top of the ladder.
If your counter lands on the head of a snake, you must slide down to the bottom of the snake.
The ladders are respresented on the board as 1's and the snakes are represented on the board as 2's \n''')
game_won =  False
print('''                            Welcome to Snakes and Ladders
                                By. MUSA HAMWALA\n
''')



#>------------------------------------------
#First board - using the board index
board = [100,99,98,97,96,95,94,93,92,91,
         81,82,83,84,85,86,87,88,89,90,
         80,79,78,77,76,75,74,73,72,71,
         61,62,63,64,65,66,67,68,69,70,
         60,59,58,57,56,55,54,53,52,51,
         41,42,43,44,45,46,47,48,49,50,
         40,39,38,37,36,35,34,33,32,31,
         21,22,23,24,25,26,27,28,29,30,
         20,19,18,17,16,15,14,13,12,11,
         1,2,3,4,5,6,7,8,9,10]

#Snakes and ladders board
s_l =   ['',2,'','','','',1,'','',2,
         '','','','','','','','','','',
         '','',1,'','','','','','','',
         '','','',1,'',2,'','','','',
         '','','','','','','',2,'',1,
         '','','','','','','','','','',
         '','','','','','',1,'','','',
         '',2,'','',1,'','','','','',
         '','','',1,'','','',2,'','',
         '','','','','','','','','',1]

#player_1 board                
board_x = []
for r in range(100):
        board_x.append(' ')

#player_2 board
board_y = []
for r in range(100):
        board_y.append(' ')

#>------------------------------------------
def game_setup():
        #Main menu of the game
        while True:
                print("1.  Play game \n2.  Options \n3.  Reset game \n4.  Exit \n")
                try:
                        menu = int(input("Choose an option: "))
                        if menu == 1:
                                print('')
                                break                               
                        if menu == 2:
                                options()
                        if menu == 3:
                                restart()
                        if menu == 4:
                                quit()
                        else:
                                True
                except:
                        pass

#>------------------------------------------
#Get the player names
player_1 = input('Player 1, enter your name?    :').upper()
player_2 = input('Player 2, enter your name?    :').upper()
player_names = print('\n',player_1,'is {X}\n', player_2,'is {Y}\n')

def options():
        print("1.  See rules \n2.  Play with AI \n3.  Menu \n")
        while True:
                try:
                        menu = int(input("Choose an option: "))
                        if menu == 1:
                                print(game_rules)
                                break                               
                        if menu == 2:
                                AI()
                        if menu == 3:
                                game_setup()
                        else:
                                True
                except:
                        pass
         
#>------------------------------------------
def show_board(rows = 10, cols = 10):
    for row in range(rows):
        ui_line = "|---------"
        ui_blank = "|"
        print(ui_line * cols + "|")
        for col in range(cols):
              print(ui_blank + str(board[row*rows+col]).ljust(9,' '),end='')
        print("|")
        
        for col in range(cols):
              print(ui_blank + str(s_l[row*rows+col]).center(9,' '),end='')
        print("|")
        
        for col in range(cols):
            print(ui_blank + str(board_x[row*rows+col]).center(9,' '),end='')
        print("|")

        for col in range(cols):
            print(ui_blank + str(board_y[row*rows+col]).center(9,' '),end='')
        print("|")
    print(ui_line*10+"|")

#>------------------------------------------
def dice_roll(num_of_dice = 1, sides_of_dice = 10):
    x = 0
    dice = 0
    while x != num_of_dice:
        dice += random.randint(1,sides_of_dice)
        x += 1
    return dice

#>------------------------------------------
def player_one_move():
    global counter_pos_x, counter_pos_previous_x, user_input, counter_x
    x = dice_roll()
    blank = " "*43
    user_input += x
    check_winner()
    X_POS = board.index(user_input)

#board_x positions for the ladders
    if X_POS == 99:
            user_input += 7
            board_x[user_input] = counter_x

    if X_POS == 66:
            user_input += 17
            board_x[user_input] = counter_x

    if X_POS == 74:
            user_input += 53
            board_x[user_input] = counter_x

    if X_POS == 22:
            user_input += 16
            board_x[user_input] = counter_x

#board_x positions for the snakes
    if X_POS == 1:
            user_input -= 33
            board_x[user_input] = counter_x

    if X_POS == 9:
            user_input -= 38
            board_x[user_input] = counter_x

    if X_POS == 71:
            user_input -= 9
            board_x[user_input] = counter_x


    ##  remove old counter
    for i in range(100):
                board_x[i] = " "
            
                
    X_POS = board.index(user_input)
        
    board_x[X_POS] = counter_x
        
    print("\n",blank,"***",player_1,"***\n")
    print("You are currently on space",user_input - x)
    input("Press {enter} to roll the dice: ")
    print("You rolled",x)
    print("Move to space",user_input, "\n""\n")

    show_board() 

    ##      check to see if won
    if counter_pos_x == 99:
        global game_won
        game_won = True
        play_again()
      
    return X_POS        

    
#>------------------------------------------       
def player_two_move(): #asks for player two input
    """Ask's for player two's input so that the board can take the counter and move it to it's new posistion"""
    global counter_pos_y, counter_pos_previous_y,user_input_2, player_2
    y = dice_roll()
    blank = " "*43
    user_input_2 += y
    check_winner()
    Y_POS = board.index(user_input_2)
    
    #board_y positions for the ladders
    if Y_POS == 99:
            user_input_2 += 7
            board_y[user_input_2] = counter_y

    if Y_POS == 66:
            user_input_2 += 17
            board_y[user_input_2] = counter_y

    if Y_POS == 74:
            user_input_2 += 53
            board_y[user_input_2] = counter_y

    if Y_POS == 22:
            user_input_2 += 16
            board_y[user_input_2] = counter_y

    #board_y positions for the snakes
    if Y_POS == 1:
            user_input_2 -= 33
            board_x[user_input_2] = counter_y

    if Y_POS == 9:
            user_input_2 -= 38
            board_y[user_input_2] = counter_y

    if Y_POS == 71:
            user_input_2 -= 9
            board_y[user_input_2] = counter_y


    ##      remove old counter
    for i in range(100):
                board_y[i] = " "
                
    Y_POS = board.index(user_input_2)
    board_y[Y_POS] = counter_y

    print("\n",blank,"***",player_2,"***\n")
    print("You are currently on space",user_input_2 - y)
    input("Press {enter} to roll the dice: ")
    print("You rolled",y)
    print("Move to space",user_input_2,"\n")

    show_board() 

    ##      check to see if won
    if counter_pos_y >=100:
        global game_won
        game_won = True
        play_again()
    return Y_POS    

def computer():
    """Ask's for player two's input so that the board can take the counter and move it to it's new posistion"""
    global counter_pos_y, counter_pos_previous_y,user_input_2, player_2
    y = dice_roll()
    blank = " "*43
    user_input_2 += y
    player_2 = "Computer"
    check_winner()
    Y_POS = board.index(user_input_2)
    
    #board_y positions for the ladders
    if Y_POS == 99:
            user_input_2 += 7
            board_y[user_input_2] = counter_y

    if Y_POS == 66:
            user_input_2 += 17
            board_y[user_input_2] = counter_y

    if Y_POS == 74:
            user_input_2 += 53
            board_y[user_input_2] = counter_y

    if Y_POS == 22:
            user_input_2 += 16
            board_y[user_input_2] = counter_y

    #board_y positions for the snakes
    if Y_POS == 1:
            user_input_2 -= 33
            board_x[user_input_2] = counter_y

    if Y_POS == 9:
            user_input_2 -= 38
            board_y[user_input_2] = counter_y

    if Y_POS == 71:
            user_input_2 -= 9
            board_y[user_input_2] = counter_y

    ##      remove old counter
    for i in range(100):
                board_y[i] = " "
                
    Y_POS = board.index(user_input_2)
    board_y[Y_POS] = counter_y

    print("\n",blank,"*** Computer ***\n")
    print("Computer is currently on space",user_input_2 - y)
    print("Computer rolled",y)
    print("Computer moves to space",user_input_2,"\n")

    show_board() 

    ##      check to see if won
    if counter_pos_y >=100:
        global game_won
        game_won = True
        play_again()
    return Y_POS
        
#>------------------------------------------
def adding_score():
    global game_won, player_1_points, player_2_points
    if game_won == True:
        if player_1:
            player_1_points += 1
        elif player_2:
            player_2_points += 1
        print(player_1, ' has won ', player_1_points, ' time(s)')
        print(player_2, ' has won ', player_2_points, ' time(s)\n')
          
        
#>------------------------------------------
def check_winner():
    global user_input, user_input_2
    #checks board and compares it with player 1 and 2 total
    if user_input_2 or user_input >= 100:
            
        if user_input >= 100:
                print('Game over!: ', player_1, 'Wins\n')
                entry = input('Would you like to play again? (Y/N): ').upper()
                if entry == "Y":
                    print('lets play again!!\n')
                    adding_score()
                    restart()
                elif entry == "N":
                    print('Thanks for playing!!\n')
                    adding_score()
                    quit()
                elif entry != "n" or "y":
                    print('Please enter "Y" for yes or "N" for no!')
                    check_winner()
        elif user_input_2 >= 100:
                print('Game over!: ', player_2, 'Wins\n')
                entry = input('Would you like to play again? (Y/N): ').upper()
                if entry == "Y":
                    print('lets play again!!\n')
                    adding_score()
                    restart()
                elif entry == "N":
                    print('Thanks for playing!!\n')
                    adding_score()
                    quit()
                elif entry != "n" or "y":
                    print('Please enter "Y" for yes or "N" for no!')
                    check_winner()
            
#>------------------------------------------
def restart():
        global game_won, user_input, user_input_2, X_POS, x, board_x, board_y
        game_won = False
        user_input = 0
        user_input_2 = 0
        X_POS = 0
        x = 0
        board_x = []
        for r in range(100):
                board_x.append(' ')

        #player_2 board
        board_y = []
        for r in range(100):
                board_y.append(' ')
                
        show_board()
        if game_won == False:
                X_POS = board.index(user_input)
                board_x[X_POS] = counter_x
                Y_POS = board.index(user_input_2)
                board_y[Y_POS] = counter_y
                player_one_move()
                print(user_input, 'Testing1')
                player_two_move()
                print(user_input_2)

game_won = False              
def AI():
#This function allows both players to switch turns in order to play the game, so that eventually a winner can be found and the play_again variable can be actioned""" 
    if game_won == False:
        player_one_move()
        computer()
        AI()
        AI()
        
        
#>------------------------------------------
game_won = False
game_setup()

def game_loop():
#This function allows both players to switch turns in order to play the game, so that eventually a winner can be found and the play_again variable can be actioned""" 
    if game_won == False:
        player_one_move()
        player_two_move()
        game_loop()
    

game_loop()
#>------------------------------------------   
