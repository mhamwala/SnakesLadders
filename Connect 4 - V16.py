#Kyle Nicol- Connect 4

#Default Values for Connect 4, Every time the game starts these values will be used 
Height = 6
Width = 7
Connect = 4

import sys
import copy

def get_players():
    global Player1
    global Player2
    Player1 = input("Player 1, Please enter your name: ")
    Player2 = input("Player 2, Please enter your name: ")
#>----------------------------------------------------------------------    
def create_board(wdt=10,lng=10):
    line = []
    for x in range(wdt):
        line.append(0)
    board = []
    for x in range(lng):
        board.append(copy.copy(line))
    return board
#>----------------------------------------------------------------------
def display_board(board_data,wdt,lng):
    ui_part = ("|---")
    sub = {0:" ",
           1:"X",
           2:"O"}
#>----------------------------------------------------------------------    
    def ui_line (ui_part = "|---") :
        part = ""
        for x in range(wdt):
            part += ui_part
        part += "|" + "\n"
        return part
    display = "\n"
    for x in range(lng):
        display += "\n"
        display += ui_line()
        for y in range(wdt):
            display += "|"
            display += sub[board_data[x][y]].center(3," ")
        display += "|"
    display += "\n" + ui_line()
    print(display)
global Player    
Player = 1
#>----------------------------------------------------------------------
def ReplayGame():
    while True:
        try:
            GameReplay = int(input ("""
Would you like to play again?

1. Yes
2. No

"""))
            if GameReplay == 1:
                print("")
            if GameReplay == 2:
                sys.exit(0)
            else:
                True
        except:
            True
#>----------------------------------------------------------------------
#From the main menu the player will be able to navigate through the games menu
def MainMenu():
    print ("""    Connect 4    """)
    print ("1.  Play Game \n2.  Options \n3.  Exit ")
    while True:
        try:
            MenuSelection = (int(input("Please select an option: ")))
            if MenuSelection == 1:
                print("")
                break
            if MenuSelection == 2:
                Options()
                break
            if MenuSelection == 3:
                sys.exit(0)
                break
            else:
                True
        except:
            pass
def BoardReset():
    for x in range (Width):
        for y in range(Height):
            board[x][y] = 0
#>----------------------------------------------------------------------    
#Options Menu, this is designed to make the game more customisable and allow the players to directly control the rules of the game
#Throught this menu the players will be able to control the board size and connect ammount
def Options():
    global Width
    global Height
    global Connect
    print ("Current Height - ", Height, "\nCurrent Width - ", Width,"\nConnect Amount - ", Connect)
    while True:
        try:
            OptionsMenu= int(input ("\nWhat would you like to change? \n 1. Height \n 2. Width \n 3. Connect amount \n 4. Play Game \n 5. Exit to menu \n Please select an option: "))
    #>----------------------------------------------------------------------
            if OptionsMenu == 1:
                Height = int(input("Please enter a suitable height under 21: "))
                while Height > 20:
                    Height =int(input ("Please enter a height under 21: "))
            if OptionsMenu == 2:
                Width = int(input("Please enter a suitable Width under 21: "))
                while Width > 20:
                    Width = int(input("Please enter a suitable Width under 21: "))  
            if OptionsMenu == 3:
                print ("NOTE: Connect amount must be less than 10 but greater than 2")
                Connect = int(input("Please enter how many tokens in a row you would like to use: "))
                while Connect > 10 or Connect < 3 or Connect > Width or Connect > Height:
                    Connect= int(input("Please enter a value less than 10 and less than the Width and Height"))
            if OptionsMenu == 4:
                print("")
                break
            if OptionsMenu == 5:
                MainMenu()
            else:
                True
        except:
            pass
#>----------------------------------------------------------------------
def playgame():
    global Player
    global game_over
    global Player1
    global Player2
    Row = Height
    game_over == "No"
    while game_over == "No":
        Player = 1
#>----------------------------------------------------------------------
#       Loop to make sure its player 1's turn unitl he enters a valid move
        while Player == 1:
            try:
                Row = Height - 1
                Move = int(input("Player 1, Select a column"))
                Move -= 1
#               This while condition checks to see if a counter is already on the row selected
#               if there is a counter it will start moving it up the board until theres a free space
#               if it gets to the top of the board and theres no free space it will then ask the user to
#               select another position
                while board[Row][Move] == 1 or board[Row][Move] == 2:
                    Row -= 1
                    while Row < 0:
                         Move = int(input("Player 1, Select a column"))
                         Move -= 1
                         Row = Height - 1
            except:
                print ("Please enter a value between 1 and", Width)
            else:
                break
            
#       Updates the board
        board[Row][Move] = 1
        display_board(board,Width,Height)
        WinCondition(board,Width,Height)
#       win condition will return the game over value 
        if game_over == "yes":
            break
        
        Player = 2
#>----------------------------------------------------------------------
        while Player == 2:
            try:
                Row = Height - 1
                Move = int(input("Player 2, Select a column"))
                Move -= 1
                while board[Row][Move] == 1 or board[Row][Move] == 2:
                    Row -= 1
                    while Row < 0:
                         Move = int(input("Player 2, Select a column"))
                         Move -= 1
                         Row = Height - 1
            except:
                print ("Please enter a value between 1 and", Width)
            else:
                break
             
        board[Row][Move] = 2
        display_board(board,Width,Height)
        WinCondition(board,Width,Height)
        if game_over == "yes":
            break
        Player = 1
            
    if Player == 1:
        print (Player1, "Wins the game!")
    else:
        print (Player2, "Wins the game!")

#>----------------------------------------------------------------------
def WinCondition(board,wdt,lng):
    global game_over 
    #PLAYER 1 CHECK
    
    for y in range(Width):
        for x in range(Height):
            WinCheck = 0
            for z in range (Connect):
                if board[x-z][y] == 1 and x > 0:
                    WinCheck += 1
                if WinCheck == Connect:
                     game_over = "yes"
                     return game_over
        
    for y in range(Width):
        for x in range(Height):
            WinCheck = 0
            for z in range (4):
                if board[x][y-z] == 1 and y > 0 and y < 7:
                    WinCheck += 1
                if WinCheck == Connect:
                    game_over = "yes"
                    return game_over
        
    for y in range(Width):
        for x in range(Height):
            WinCheck = 0
            for z in range (4):
                if board[x-z][y-z] == 1 and x > 0 and y > 0:
                    WinCheck += 1
                if WinCheck == Connect:
                    game_over = "yes"
                    return game_over
           

    for y in range(Width):
        for x in range(Height - 3):
            WinCheck = 0
            for z in range(4):             
                if board[x+z][y-z] == 1 and x > 0 and y > 0:
                    WinCheck += 1
                if WinCheck == Connect:
                    game_over = "yes"
                    return game_over

    #PLAYER 2 CHECK
#>----------------------------------------------------------------------
    for y in range(Width):
        for x in range(Height):
            WinCheck = 0
            for z in range (4):
                if board[x-z][y] == 2 and x > 0:
                    WinCheck += 1
                if WinCheck == Connect:
                     game_over = "yes"
                     return game_over
        
    for y in range(Width):
        for x in range(Height):
            WinCheck = 0
            for z in range (4):
                if board[x][y-z] == 2 and y > 0 and y < 0:
                    WinCheck += 1
                if WinCheck == Connect:
                    game_over = "yes"
                    return game_over
        
    for y in range(Width):
        for x in range(Height):
            WinCheck = 0
            for z in range (4):
                if board[x-z][y-z] == 2 and x > 0 and y > 0:
                    WinCheck += 1
                if WinCheck == Connect:
                    game_over = "yes"
                    return game_over
           

    for y in range(Width):
        for x in range(Height - 3):
            WinCheck = 0
            for z in range(4):             
                if board[x+z][y-z] == 2 and x > 0 and y > 0:
                    WinCheck += 1
                if WinCheck == Connect:
                    game_over = "yes"
                    return game_over
                     
StartGame = "YES"
#>----------------------------------------------------------------------

while StartGame == "YES":
    MainMenu()
    get_players()
    board = create_board(Width,Height)
    display_board(board,Width,Height)
    game_over = "No"
    playgame()
    ReplayGame()

