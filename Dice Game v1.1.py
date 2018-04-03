#Dice Game
#Daniel Harding, Kyle Nicol, 17th February 2016

from time import sleep
import random

WINNING_SCORE = 150

#Returns a sanitised integer from the user

def get_sani_input(min,max,prompt=""):
    
    not_sanitised = True
    while not_sanitised:
        user_input = input(prompt)
        if user_input.isdigit():
            user_input = int(user_input)
            if user_input > max:
                print("Try again!")
                continue
            else:
                return user_input
        else:
            print("Try again!")
            continue

#rolls a dice, defaults to 2 six sided dice

def dice_roll (num_of_dice = 2,sides_of_dice = 6):
    rolls = []
    x = 0
    while x != num_of_dice:
        dice = random.randint(1,sides_of_dice)
        rolls.append(dice)
        x += 1
    return rolls
    
#displays the player score, accepts a string and an int as arguments

def display (players_name, players_score):
    printout = "\n" + players_name + "\n"
    printout += "Your Score is :" + str(players_score)
    print(printout)

#class to hold the players name and score

class player ():
    def __init__ (self,name,score=0,ai=False):
        self.name = name
        self.score = score
        self.isai = ai

    def ai_move(self,current_total):
        if self.score + current_total >= WINNING_SCORE:
            return 2
        elif self.score + current_total >= 20 :
            return 2
        else:
            return 1
            


#creates the amount of players equal to the integer argument.
#call argument ai as true to enable a computer opponent.

def create_players(number_of_players):
    list_of_players = []
    for y in range(number_of_players):
        print("Please enter player",y+1,"name :", end="")
        player_name = input()
        y = player(player_name)
        list_of_players.append(y)

    return list_of_players



def create_ai(list_of_players,number_of_players):
    for y in range(number_of_players):
        print("Please enter Computer",y+1,"name :", end="")
        player_name = input()
        y = player(player_name,ai=True)
        list_of_players.append(y)

    return list_of_players



#creates the initial game state
#takes no arguments

def startup ():
    number = get_sani_input(1,8,"\nHow many players are there?\n|:")
    players = create_players(number)
    number = get_sani_input(0,8,"\nHow many computers opponenets are there?\n|:")
    players = create_ai(players,number)
    return players
        


def turn(players,p_t):
    display(players[p_t].name,players[p_t].score)
    dice_rolls = 0,0
    turn_score = 0
    try_again = True
    dice_rolls = dice_roll()
    for x in dice_rolls:
            turn_score += x
            
    while try_again:
        if 1 in dice_rolls:
            try_again = False
            continue
               
        prompt = "\n\nYour dice rolls are:" + str(dice_rolls) + "\n"
        prompt+= "Would you like to roll again or bank your score of :" + str(turn_score) + "\n"
        prompt+= "1) Roll Again  2) Bank Score\n|:"

        if players[p_t].isai == True:
            print(prompt)
            user_input = players[p_t].ai_move(turn_score)
            print("I'll choose to do this " + str(user_input))
        elif players[p_t].isai == False:
            user_input = get_sani_input(1,2,prompt)
        
        if user_input == 1:
            dice_rolls = dice_roll()
            for x in dice_rolls:
                turn_score += x
            print("\nRolling Dice",end="")
            for y in range(3):
                sleep(0.5)
                print(".",end="")
            sleep(1)
            continue
        elif user_input == 2:
            players[p_t].score += turn_score
            break

        
    else:
        print("\n\nYour dice rolls are:",dice_rolls)
        print("Bad luck, you have rolled a '1', your turn is over and your")
        print("points are gone!")
        sleep(3)


#to change the winning condition, give this function a third argument as an integer

def win_condition(players, p_t, winning_score=150):
    
    if players[p_t].score >= winning_score:
        return False
    else:
        return True

def player_turn(players,p_t):
    number_of_players = len(players)
    p_t += 1
    if p_t >= number_of_players:
        p_t = 0
    return p_t
    
def declare_winner(players,p_t):
    print('\n\nCongratulations',players[p_t].name,'!','\nYou have won the game!')

def play_again():
    print("\n\n\nWould you like to play again?\n\t1)Yes 2)No\n|:")
    
    user_input = get_sani_input(1,2)
    if user_input == 1:
        return True
    elif user_input == 2:
        return False

def main_menu ():
    welcome = "Welcome to the dice roll game!\n\n"
    welcome+= "Please Select an option:\n"
    welcome+= "1)Play Game 2)Instructions\n"
    welcome+= "3)options   3)Exit Game\n"
    welcome+= "|:"

    menu_functions = {1:main_game,
                      2:instructions,
                      3:options,
                      4:exit_game}

    playing = True
    while playing:
        user_input = get_sani_input(1,4,welcome)
        playing = menu_functions[user_input]()
    else:
        input("Thank you for playing")
    

def instructions ():
    rules = "\n\tINSTRUCTIONS:\n\nThe Rules to the dice game are simple:\n"
    rules+= "The goal is to get your banked score to the winning score\n"
    rules+= "as fast as possible.\n\n"
    rules+= "Beware, if you roll a 1, then your current turns score is forfit.\n\n"
    rules+= "You can save your current turns score however by\n"
    rules+= "banking it, this will end your turn though.\n\n"
    rules+= "Good Luck and Have Fun!"

    print(rules)
    
    return True

def options():
    prompt = "\nPlease enter the winning score you would like.\n"
    prompt+= "It must be higher than 50 but lower than 300\n"
    prompt+= "|:"

    user_input = get_sani_input(50,300,prompt)

    global WINNING_SCORE

    WINNING_SCORE = user_input

    return True

def exit_game():    
    return False

def main_game():
    players = startup()
    play_game = True
    p_t = len(players)
    while play_game:
        p_t = player_turn(players,p_t)        
        turn(players,p_t)
        play_game = win_condition(players,p_t,WINNING_SCORE)
    else:
        declare_winner(players,p_t)
        play_again()


if __name__ == "__main__" :
    main_menu()
