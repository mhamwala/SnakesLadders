#variable strings which are called when needed
win_game=("congratulations you have won the game and sank all the battleships")
instruction_rules=("The aim of the game is to sink the computer's battleships there are 10 individual battleships to hit in total")
missed=('you missed,please try again')
you_hit=('congratulations you hit a battleship')
again=('you have already hit this')

#board settings and rules
rows=11
cols=11
board=[]
hit ='X'
miss='M'
try_again= 'T'
play_game=True
game_won= False
player_turn=1
content=[]
x = 0
for i in range(100):
    content.append (0)


def main():#this function calls all the functions below in order.As well as this they are then reset after the player has sunk all the battleships in order to play again.
    player_one=player_names()
    print(player_one)
    instructions()
    playing=True
    while playing:
        board=create_board()
        player_move(board)
        win_condition()
    game_loop()
    play_game=True     
    
        
 
def player_names():#calls the player's name, 
    player_one=input ('player one what is your name').upper()
    return player_one

def instructions(): #briefs player on how to play game
    instructions=input('press any button to display rules')
    print (instruction_rules)

def play_again():#this function allows the player to either exit the game or allow the game to be played again.when they press 'y' all the variables are reset so that they can play again.
    again=input("would you like to play again y/n: ")
    if again == "n":
        print("thanks for playing")
        quit()

    elif again == "y":
        for i in range(100):
            content[i] = 0
        user_input = 0
        play_game=True
        game_won= False
          
        main()
            

       
        

def game_loop():#this tests the game to see if all the battleships have been taken, if not it carries on until they have all been found
    if game_won == False:
        player_move(board)
        win_condition()
        game_loop()
    else:
        play_again()
        print(win_game)

#This allows the board to be numbered 1-99 and for a zero to appear which changes dependent on a hit or miss
def board_one(row,col):
    number=(row-1)*10+(col-1)
    if number <10:
        number= str(0)+ str(number)
    return number    

    
    
def create_board(rows = 11, cols = 11):    #this create the board and immunerates it 
    for row in range (1,rows):
        ui_line = "|----------" #helps to print and display the board
        ui_blank = "|        "
        print(ui_line * 10 + "|")
        for col in range (1,11):
            print(ui_blank +" " + (str (content[(row-1)*10+(col-1)])  ), end='')
        print("| ")
        for col in range (1,11):
            print(ui_blank + ('  '), end='')
        print("| ")
        for col in range (1,cols):
            print(ui_blank   + str(board_one(row,col)), end='')
        print ("| ")
    print(ui_line*10+"|")



for row in range(rows):
        for num in range(0,100):
            board.append(str(num).center(2," "))




#this sets where the ships are, and they are predetermined
ships = [[1,15,26,42,57,63,70,77,93,98]]


        
        
    

def player_move(board): ##asks for player input and move
    global x #after the player has successfully hit a target a number is produced to show how many battleships have been hit.It allows you to see how many more you need to hit
    user_input=int(input('please enter a posisition you would like to attack'))
    for i in range (len(ships)): #this searches the board and looks to see if any ships have been hit, if so it calls the loops and displays the variable you_hit
        if user_input in ships[i]:
            content[user_input]=hit #this variable here changes the 0 to a H,to show that it has been hit
            x += 1
            print(x)
            print(you_hit)
        elif user_input not in ships[i]: #if player misses it displays the miss varaible
            content[user_input]=miss#This does exactly the same  as the previous variable  in that here it notifies you that when you miss it changes the 0 to m
            print(missed)

def win_condition():#this tells the board that when all 10 have been hit to call play again and tell them that they have won
    global x
    if x == 10:
        print(win_game)
        play_again()            

        

     
        
main()                 
