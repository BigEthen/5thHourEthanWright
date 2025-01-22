#Name:Ethan Wright
#Class: 5th Hour
#Assignment: HW16
import random
#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".

#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.
from random import randint
def rge_game():
    print("Chose the number 1 for rock , 2 for paper , 3 for scissors")
    playerchoice = int(input())
    oppenemtchoice = random.randint(1,3)
    if playerchoice == 1 and oppenemtchoice == 2:
        print("yoor oppenent chose", oppenemtchoice)
        print("oppenemt beat you with paper")
    elif playerchoice == 1 and oppenemtchoice == 3:
        print("your oppenemt chose", oppenemtchoice)
        print("you beat your oppenemt with rock")
    elif playerchoice == 2 and oppenemtchoice == 3:
        print("your oppenemt chose", oppenemtchoice)
        print("you beat your oppenemt with papper")
    elif playerchoice == 2 and oppenemtchoice == 3:
        print("your oppenemt chose", oppenemtchoice)
        print("oppenemt beat your oppenemt with scissors")
    elif playerchoice == 3 and oppenemtchoice == 3:
        print("your oppenemt chose", oppenemtchoice)
        print("oppenemt beat your oppenemt with rock")
    elif playerchoice == 3 and oppenemtchoice == 2:
        print("your oppenemt chose", oppenemtchoice)
        print("you beat your oppenemt with scissors")
    else:
        print('invalid response')
        rge_game()
    if playerchoice == 1 and oppenemtchoice == 1:
        print("you get a tie ")
    if playerchoice == 2 and oppenemtchoice == 2:
        print("you get a tie ")
    if playerchoice == 3 and oppenemtchoice == 3:
        print("you get a tie ")
    rpe_game()
def rpe_game():
    replayerchoice = input("do you want to play againt? y/n!")
    if replayerchoice == "y" or replayerchoice :
        rge_game()
rge_game()







