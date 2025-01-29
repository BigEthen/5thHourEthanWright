#Name:Ethan Wright
#Class: 5th Hour
#Assignment: HW18


#1. Import the "random" library and create a def function that prints "Hello World!"
import random
from os import remove


def hello():
    print("Hello World!")

#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag = ("red","green","blue","yellow","Black")
#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def man():
    bean = random.choice(beanBag)
    print(bean)
#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def woman():
    bbc = input("would you like to play agian ? y/n")
    if bbc == "y" or "Y":
      pass
    else:
        if bbc == "n" or "N":
         exit()


#5. Call the #3 function at the bottom.
woman()
man()








