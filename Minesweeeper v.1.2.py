#Daniel Harding, 23rd February 2016
#Minesweeper

import copy
import random
from time import sleep

global WDT, LNG, MINE

def set_globals ():
    with open ("options.txt",mode = "r") as settings:
        for line in settings:
            if "0000" in line:
                global WDT
                WDT = line.lstrip("0000:WDT:")
                WDT = WDT.rstrip("\n")
                WDT = int(WDT)
            if "0001" in line:
                global LNG
                LNG = line.lstrip("0001")
                LNG = LNG.lstrip(":LNG:")
                LNG = LNG.rstrip("\n")
                LNG = int(LNG)
            if "0002" in line:
                global MINE
                MINE = line.lstrip("0002")
                MINE = MINE.lstrip(":MINE:")
                MINE = MINE.rstrip("\n")
                MINE = int(MINE)

                

#Create board defaults to a 10x10 board with "0" being the default filler
#just pass arguments to the function to change board size

def create_board(wdt=10,lng=10,default=0):
    line = []
    for x in range(wdt):
        line.append(default)
    board = []
    for x in range(lng):
        board.append(copy.copy(line))
    return board



#display_board will put each of the board data's elements into its own square.
#if it gets an out of range error, try swapping the wdt and lng values you pass
#to it

def display_board(board_data,board_los,wdt,lng):

    ui_part = ("|---")
#edit this dictionary to change what each integer in the list "board_data" represents
    sub = {0:"0",
           1:"1",
           2:"2",
           3:"3",
           4:"4",
           5:"5",
           6:"6",
           7:"7",
           8:"8",
           9:"M",
           10:"F",
           11:" "}
    
    def ui_line (ui_part = "|---") :
        part = ""
        for x in range(wdt):
            part += ui_part
        part += "|" + "\n"
        return part
     
    display = "\n"
    display += "Collumn (x)\n\t "
    for x in range(wdt):
        display += str(x+1).center(4," ")
        
    display += "\n"
    display += "Row  (y)" + ui_line()
    
    for x in range(lng):
        display += str(x+1).rjust(8," ")
        for y in range(wdt):
            display += "|"
            if board_los[x][y] == 0 or board_los[x][y] == 11 or board_los[x][y] == 10:
                display += sub[board_los[x][y]].center(3," ")
            if board_los[x][y] == 1:
                display += sub[board_data[x][y]].center(3," ")
        display += "|"
        display += "\n\t" + ui_line()

    print(display)

#places mines upon the board randomly, also checks to see if there is a mine
#already placed on the co ordinates to prevent too few mines being on the board

def seed_board (difficulty,board_data,wdt,lng):
    number_of_mines = {0:10,
                       1:15,
                       2:20,
                       3:30}

    check = 0
    while check < number_of_mines[difficulty]:
        x = random.randint(0,lng-1)
        y = random.randint(0,wdt-1)
        if board_data[x][y] == MINE :
            continue
        else:
            board_data[x][y] = MINE
            check += 1
            
            
        

#searches through the board and adds 1 to all surrounding tiles if it finds a mine
#also uses its own function definition for when it finds a mine, mine value = 9

def enumerate_board(board_data,wdt,lng):
    
    def place_check(x,y):
        for a in range(-1,2):
            if x+a > lng-1 or x+a <0 :
                continue
            for b in range(-1,2) :
                if y+b > wdt-1 or board_data[x+a][y+b] == MINE or y+b <0 :
                    continue
                board_data[x+a][y+b] += 1
                
    for y in range(wdt):
        for x in range(lng):
            if board_data[x][y] == MINE:
                place_check(x,y)

#x and y are the player's inputs for x collumn and y collumn respectivly
#Checks to see if the tile flipped is a 0 and flips all tiles around it if its True
#Also checks to see if there are any 0's around a numbered tile and reveals those too
                
def flip_tile(x,y,wdt,lng,board_los,board_data,flaged,counter=0):
    
    if flaged.casefold() == "f" :
        board_los = flag(board_los,x,y)
    else:
        board_los[x-1][y-1] = 1

        if board_data[x-1][y-1] != 9 and board_data[x-1][y-1] != 0:
            for a in range(-2,1):
                if x+a > wdt-1 or x+a < 0:
                    continue
                for b in range(-2,1):
                    if y+b >lng-1 or y+b < 0:
                        continue
                    if board_data[x+a][y+b] in [0] :
                        board_los[x+a][y+b] = 1
                        
        elif board_data[x-1][y-1] == 9:
            for a in range(lng):
                for b in range(wdt):
                    if board_data[a][b] == 9:
                        board_los[a][b] == 1
        
        else:
            for a in range(-2,1):
                if x+a > wdt-1 or x+a < 0:
                    continue
                for b in range(-2,1):
                    if y+b >lng-1 or y+b < 0:
                        continue
                    board_los[x+a][y+b] = 1

                        
    return board_los

#Creating Players for game
#change any attributes of the class to store the variables you need
#for each player.
class player ():
    def __init__ (self,name,difficulty):
        self.name = name
        self.difficulty = difficulty


#use this function to create any amount of players that you need and return
#them in a list.

def create_players(number_of_players):
    list_of_players = []
    for y in range(number_of_players):
        print("Please enter player",y+1,"name :", end="")
        player_name = input()

        print("\nPlease enter your difficulty:")
        print("0)Begginer 1)Normal 2)Hard 3)Expert")
        checking = True
        while checking:
            player_challenge = input("Difficulty level :")
            if player_challenge.isdigit():
                player_challenge = int(player_challenge)
                if player_challenge < 0 or player_challenge > 3:
                    print("Try again!")
                    continue
                else:
                    y = player(player_name,player_challenge)
                    checking = False
            else:
                print("Try again")
                continue
        list_of_players.append(y)
    return list_of_players


#Win condition
#Checks the number of correctly flagged mines against the amount
#of mines on the board


def victory_check (board_data,board_los,difficulty):
    
    number_of_mines = {0:10,
                       1:15,
                       2:20,
                       3:30}
    
    mines_found = 0
    for x in range(LNG):
        for y in range(WDT):
            if board_data[x][y] == 9 and board_los[x][y] == 10:
                mines_found += 1
                
    if mines_found >= number_of_mines[difficulty]:
        print("You have founf all the mines, congratulations!")
        return False
    else:
        print(mines_found)
        return True


#function to flag the board.
#adds or removes a flag if the co ordinates already have one
def flag (board_los,x,y):

    if board_los[x-1][y-1] == 10:
        board_los[x-1][y-1] = 11
    else:
        board_los[x-1][y-1] = 10

    return board_los



#Getting and sanitising the players input
#Users input is seperated with spaces so that it can be split into a list

def player_input():
    prompt = "please enter the collumn then the row co-ordinates \n"
    prompt +="Followed by an 'f' if you would like to place a flag\n"
    prompt +="Please seperate your entries with a space\n:"

    checking = True
    while checking :
        parts = []
        user_input = input(prompt).split()

        for part in user_input:
            parts.append(part)
        #adding an empty string to the end of the users input so that they
        #can enter 2 numbers with no str to reveal a square
        parts.append(" ")
        #making sure the user enters thier input in the following format
        #(int) (int) (str)
        if parts[0].isdigit and parts[1].isdigit() and isinstance(parts[2],str):
            parts[0]= int(parts[0])
            parts[1]= int(parts[1])
            #Making sure the user hasnt entered anything silly into the digit values
            if parts[0] < 0 or parts[1] < 0 or parts[0] > WDT or parts[1] > LNG:
                print("Try again with an aproptiate value")
                continue
                        
            return parts
           
        else:
            print("Try Again with the following format 0 0 or 0 0 f to flag")
            continue



#Setting the loss condition
#checking to see if the tile revealed is a mine
#returns True if the tile is not a mine so as not to break the game loop
def stepped_on_mine(x,y,board_data):
    
    if board_data[x-1][y-1] == 9:
        print("BOOM! You stepped on a mine... Game over")
        return False
    else:
        return True

#Concatenated welcome text to improve performance
def welcome():
    intro = ""
    intro += "Welcome to Minesweeper" + "\n"
    intro += "Try to flag all the mines without stepping on one" + "\n"
    intro += "Good Luck!"

    print(intro)


#Main menu hub which will call the player's choice of function.
def main_menu ():
    
    welcome()
    menu = "\nPlease enter your selection\n"
    menu += "1) Play Game 2)Instructions\n"
    menu += "3) Options   4)Exit Game"
    

    running = True
    while running:
        print(menu)
        not_sanitised = True
        while not_sanitised:
            user_input = input(":")
            if user_input.isdigit():
                user_input = int(user_input)
                if user_input < 1 or user_input > 4:
                    print("Try again!")
                    continue
                else:
                    not_sanitised = False
            else:
                print("Try again!")

        menu_items = {1:play_game,
                      2:instructions,
                      3:options,
                      4:exit_game}


        running = menu_items[user_input]()

    else:
        input("Thank you for playing, goodbye!")

#function for allowing the user to change the dimentions of the board stored in the options.txt folder

def options():
    file_format = {0:"0000:WDT:",
                   1:"0001:LNG:",
                   2:"0002:MINE:"}

    options_menu = "Please select the value you would like to change:\n"
    options_menu +="1) Width of board: " + "\n"
    options_menu +="2) Lenght of Board: " + "\n"
    options_menu +="3) Exit to menu" + "\n"

    user_input = get_sani_input(1,3,
                                options_menu)
    if user_input == 3:
        return True

    options_menu = "Please enter an integer value for the option selected\n"
    options_menu +="Value must be greater than 6 but less than 20\n:"

    user_input2 = get_sani_input(6,20,options_menu)
    
    file_list = []
    
    with open ("options.txt", mode = "r") as settings_to_edit:
        for item in settings_to_edit:
            file_list.append(item.rstrip("\n"))
            
    file_list[user_input -1] = file_format[user_input -1]+ str(user_input2)
    
    with open ("options.txt", mode = "w") as settings:
        for item in file_list:
            settings.write(item +"\n")
            print(item)
        
#Returns True so as not to break out of the game loop    
    return True

def first_time_setup():
    
    file_format = {0:"0000:WDT:",
                   1:"0001:LNG:",
                   2:"0002:MINE:"}
    try:
        with open("options.txt",mode="r") as settings:
            print("Searching for Options File")
            
    except:
        with open("options.txt",mode="w") as settings:
            print("Creating Options File")
            file_list =[]
            for item in range(2):
                file_list.append(file_format[item] + "10")
            file_list.append(file_format[2] + "9")
            
            for item in file_list:
                settings.write(item +"\n")
            
            

#generalised function for getting a sanitized integer from the user between the 2 arguments
#also allows the use of a custom prompt, defaults to blank/no prompt
    
def get_sani_input(min,max,prompt=""):
    
    not_sanitised = True
    while not_sanitised:
        user_input = input(prompt)
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input > max or user_input < min:
                print("Try again!")
                continue
            else:
                return user_input
        else:
            print("Try again!")
            continue

        


def exit_game():
    #returns a value of false so as to break out of the game loop
    return False




#asking the pplayer for an imput of 1 or 2 to make comparison easier
#returns true or false depending on user input
def play_again():
    
    prompt = "\nWould you like to play again?\n"
    prompt += "1)Yes   2)No\n:"

    user_input = get_sani_input(1,2,prompt)
    
    if user_input == 1:
        return True
    else:
        return False
                
#Basic outline of the games instructions
def instructions():
    text = "\nMinesweeper is about finding the mines on the baord\n"
    text+= "To find a mine, you need to enter co-ordinates like the following:5 5\n"
    text+= "If these co-ordinates are not a mine, they will reveal a number,\n"
    text+= "This number will tell you how many mines are next to this tile.\n"
    text+= "Once you think you have found a mine, enter its co-ordinates and\n"
    text+= "add the letter f befor pressing enter to flag the tile as a mine eg:5 5 f\n"
    text+= "\nOnce you have flagged all the mines on the board you win!"

    print (text)
    #returns true so as not to break the game loop
    return True
    
#Actual game loop, called from the main menu.

def play_game ():
    set_globals()
    first_time_setup()
    
    playing = True
    while playing:
    #initial setup of the game

        player = create_players(1)
        board = create_board(wdt=WDT,lng=LNG)
        board_los = create_board(wdt=WDT,lng=LNG,default=11)
        seed_board(player[0].difficulty,board,WDT,LNG)
        enumerate_board(board,WDT,LNG)

    #main game loop
        
        still_playing = True
        
        while still_playing:
            display_board(board,board_los,WDT,LNG)
            player_move = player_input()
            board_los = flip_tile(player_move[1],player_move[0],WDT,LNG,board_los,board,player_move[2])
            still_playing = victory_check(board,board_los,player[0].difficulty)
            if player_move[2].casefold() != "f":
                still_playing = stepped_on_mine(player_move[1],player_move[0],board)
            
        else:
            display_board(board,board_los,WDT,LNG)

        return play_again()

if __name__ == "__main__" :
    first_time_setup()
    main_menu()
