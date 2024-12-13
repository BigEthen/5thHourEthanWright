#Name:Ethan Wright and ryley ashcraft
#Class: 5th Hour
#Assignment: Scenario 5

#Scenario 5
#You're all part of a new development team and the big wigs want to see what you are all capable of.
#They want you to develop whatever you want to develop, but there's only one problem:
#the same big wigs only bought enough computers for half of you. Because of this, you will
#all be split into teams of two. One serving as the brain (not using the computer),
#one serving as the hands (using the computer).


#The Teams are as such:

#Team 1: Dom (brain), Zachary (hand)
#Team 2: Ryley (brain), Ethan W (hand)
#Team 3: Eli (brain), Preston (hand)
#Team 4: Gabe (brain), Quinn (hand)
#Team 5: Sam (brain), Chaysen (hand)
#Team 6: Kevin (brain), Ethan M (hand)
#Team 7: Gage (brain), Eric (hand)


#You have until the Scenario is due to brainstorm an idea together, create a flowchart, and then
#turn that flowchart into functioning code. The code itself must have at least: 1 dictionary or list,
#1 loop, 2 if statements (elif and else statements tied to it does not count towards the total),
#1 variable with a user input, and 1 form of an assignment operator. You are free to add whatever else
#you feel is necessary to complete your concept. You will be graded based on how those ideas are
#implemented together.
import random

print("Welcome to Hangman.")
wordlist = ["Uncle snoop","SpongeBob", "Santa", "Boat" , "Batman" , "Robin", "Grinch","Kitty", "Supercalifragalisticexpialidocious", "Capman", "Luffy", "Naruto", "Gojo" , "Sakuna", "Megumi", "Landowner", "False", "say" , "Express","Harry Potter"]
print("This is your word bank:",wordlist)
i = 0
word = random.choice(wordlist)
print(word)

while i < 1:
    guess = input("Guess a word from the word bank")
    if guess == word:
        print("you guessed it right")
        answer = input("Would you like to play again? Y/N")
        if answer == "Y" or answer == "y":
            word = random.choice(wordlist)
            continue
        elif answer == "N" or answer == "n":
            print("Thanks for playing!")
            break
        else:
            print("Not a valid response.")
            break

    else:
        print("try again")













