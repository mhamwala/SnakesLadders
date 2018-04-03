#Kyle Nicol- Tic Tac Toe
Height = 3
Width = 3
connect = 4


import copy
def get_players():
    global Player1
    global Player2
    Player1 = input("Player 1, Please enter your name: ")
    Player2 = input("Player 2, Please enter your name: ")
    
def create_board(wdt=10,lng=10):
    line = []
    for x in range(wdt):
        line.append(0)
    board = []
    for x in range(lng):
        board.append(copy.copy(line))
    return board

def display_board(board_data,wdt,lng):
    ui_part = ("|---")
    sub = {0:" ",
           1:"X",
           2:"O"}
    
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
game_over = "No"
def ReplayGame():
    GameReplay = int(input ("""
Would you like to play again?

1. Yes
2. No

"""))
    if GameReplay == 1:
        print("")
    if GameReplay == 2:
        sys.exit(0)

def playgame():
    global Player
    global amount_connected
    global game_over
    global Player1
    global Player2
    RMove = 0
    CMove = 0
    Row = Height
    while game_over == "No":
        while Player == 1:
            try:
                Row = Height - 1
                RMove = int(input("Player 1, Select a Row "))
                CMove = int(input("Player 1, Select a column "))
                RMove -= 1
                CMove -= 1
                while board[RMove][CMove] == 1 or board[RMove][CMove] == 2:
                    RMove = int(input("Player 1, Select a column "))
                    CMove = int(input("Player 1, Select a Row "))
                    RMove -= 1
                    CMove -= 1
            except ValueError:
                print ("Please enter a valid move")
            else:
                break

        board[RMove][CMove] = 1
        display_board(board,Width,Height)
        WinCondition(board,Width,Height)
        if game_over == "yes":
            break
        
        Player = 2

        while Player == 2:
            try:
                Row = Height - 1
                RMove = int(input("Player 2, Select a Row "))
                CMove = int(input("Player 2, Select a Column "))
                RMove -= 1
                CMove -= 1
                while board[RMove][CMove] == 1 or board[RMove][CMove] == 2:
                    RMove = int(input("Player 2, Select a column "))
                    CMove = int(input("Player 2, Select a Row "))
                    RMove -= 1
                    CMove -= 1
            except ValueError:
                print ("Place enter a valid move")
            else:
                break

        board[RMove][CMove] = 2
        display_board(board,Width,Height)
        WinCondition(board,Width,Height)
        if game_over == "yes":
            break
        Player = 1
            
    if Player == 1:
        print (Player1, "Wins the game!")
    else:
        print (Player2, "Wins the game!")

def PlayGame_AI():
    print ("HELLO")
            
          
def WinCondition(board,wdt,lng):
    global game_over 
    #PLAYER 1 CHECK
    for y in range(Width):
        for x in range(Height):
            WinCheck = 0
            for z in range (3):
                if board[x-z][y] == 1 and x > 0:
                    WinCheck += 1
                if WinCheck == 3:
                     print ("TEST 1")
                     game_over = "yes"
                     return game_over
        
    for y in range(Width):
        for x in range(Height):
            WinCheck = 0
            for z in range (3):
                if board[x][y-z] == 1 and y > 0 and y < 7:
                    WinCheck += 1
                if WinCheck == 3:
                    print ("TEST 2")
                    game_over = "yes"
                    return game_over
        
    for y in range(Width):
        for x in range(Height):
            WinCheck = 0
            for z in range (3):
                if board[x-z][y-z] == 1 and x > 0 and y > 0:
                    WinCheck += 1
                if WinCheck == 3:
                    print ("TEST 3")
                    game_over = "yes"
                    return game_over
           

    for y in range(Width):
        for x in range(Height - 3):
            WinCheck = 0
            for z in range(3):             
                if board[x+z][y-z] == 1 and x > 0 and y > 0:
                    WinCheck += 1
                if WinCheck == 3:
                    print ("TEST 4")
                    game_over = "yes"
                    return game_over

    #PLAYER 2 CHECK
    for y in range(Width):
        for x in range(Height):
            WinCheck = 0
            for z in range (3):
                if board[x-z][y] == 2 and x > 0:
                    WinCheck += 1
                if WinCheck == 3:
                     print ("TEST 5")
                     game_over = "yes"
                     return game_over
        
    for y in range(Width):
        for x in range(Height):
            WinCheck = 0
            for z in range (3):
                if board[x][y-z] == 2 and y > 0 and y < 7:
                    WinCheck += 1
                if WinCheck == 4:
                    print ("TEST 6")
                    game_over = "yes"
                    return game_over
        
    for y in range(Width):
        for x in range(Height):
            WinCheck = 0
            for z in range (3):
                if board[x-z][y-z] == 2 and x > 0 and y > 0:
                    WinCheck += 1
                if WinCheck == 4:
                    print ("TEST 7")
                    game_over = "yes"
                    return game_over
           

    for y in range(Width):
        for x in range(Height - 3):
            WinCheck = 0
            for z in range(3):             
                if board[x+z][y-z] == 2 and x > 0 and y > 0:
                    WinCheck += 1
                if WinCheck == 4:
                    print ("TEST 8")
                    game_over = "yes"
                    return game_over
                
StartGame = "YES"

while StartGame == "YES":
    get_players()
    board = create_board(Width,Height)
    display_board(board,Width,Height)
    playgame()
    ReplayGame()
    game_over = "No"

    

