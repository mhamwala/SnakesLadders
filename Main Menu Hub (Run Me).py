#Main menu Hub
#Daniel Harding, 13th April 2016

import os
import time

drive = "J"

directories = {1:"Minesweeeper v.1.2.py",
               2:"Connect 4 - V16.py",
               3:"Dice Game v1.1.py",
               4:"Snakes-and-Ladders-V1.9.py",
               5:"BATTLESHIPS-3.py",
               6:"Tic Tac Toe.py"}

#Promtps the user for which game they would like to play
#then runs the user selection in cmd promtp

def menu_display():

    menu = "Welcome to the games library!"
    print(menu)
    
    menu ="Please select the game you would like to play:\n"

    with open ("Game_List.txt", mode="r") as games:
        for item in games:
            menu += item
    menu +="\n0)Exit Game"
    menu +="\n\nPlease enter the number of the game you wish to play\n|:"

    keep_playing = True
    while keep_playing == True:
        
        user_input = get_sani_input(0,6,menu)
        time.sleep(1)

        if user_input == 0:
            keep_playing = False
            continue
        
        else:    
            try:
                os.startfile(directories[user_input])
            except:
                print("404 error, Game file not found, please select another game")
                continue
    else:
        input("Thanks for playing")
        
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


    
menu_display()
#https://docs.python.org/3.2/library/subprocess.html
