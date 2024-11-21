#Name:Ethan Wright
#Class: 5th Hour
#Assignment: Scenario 4

#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

while True:
    ask = int(input("how many players"))
    if ask > 0:
        break
colgate = []

for i in range(1,ask +1):


    while True:
        rate = int(input("rate the model from 1 to 5"))
        if ask < 1 or rate > 5:
            print("ahh man that wrong ")
        else:
            break

    colgate.append(rate)




print("the average rating for all model rated is ", sum(colgate) / len(colgate))













