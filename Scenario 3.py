#Name:Ethan Wright
#Class: 5th Hour
#Assignment: Scenario 3
from random import random, randint

#Scenario 3:
#Now that the game development team has a dictionary for enemies
#(see Scenario 1) and the dictionary for the party is fixed
#(see Scenario 2), they want to start making a full prototype for the
#combat system. The team lead is a big Dungeons & Dragons fan and
#wants to make the combat similar to that. Because of this, the
#dictionaries need to be reworked slightly to be like that.

#Each enemy and party member in both dictionaries needs:
# - health points (somewhere between 6 and 25)
# - an attack modifier (somewhere between 3 and 7)
# - a damage roll (a number that varies based on weapon/spell)
# - and an Armor Class (somewhere between 10 and 17).

#Once both dictionaries are updated, create a combat
#prototype that has a party member attack first, then an enemy
#attacks back right after.

#To determine if a creature hits another creature, you roll a
#20-sided die (d20) and add the attack modifier to the roll.
#If that number is the same as or higher than the enemy's Armor Class
#(AC), the attack hits and you roll for damage. If it is lower, the
#attack misses. If an enemy or party member hits zero (0) health
#points, they die.

#To make things easier, here is a reference list for party damage rolls.
#(Feel free to use similar numbers for your enemy dictionary.)

# - Lae'Zel uses a greatsword: 2d6 + 3
# - Shadowheart uses a mace: 1d6 + 2
# - Gale uses the firebolt spell: 1d10
# - Astarion uses a shortbow: 1d6 + 4

from random import randint

#Party Dictionary Goes = {
goodpeople = {
    "batman": {
        "health": 25,
        "attack": 7,
        "armor": 17,
    },
    "robin": {
        "health": 16,
        "attack": 4,
        "armor": 14

    },
    "batwoman": {
        "health": 15,
        "attack": 5,
        "armor": 13,
    }}

#Enemy Dictionary Goes Here

enemy = {
    "joker": {
        "health": 20,
        "attack": 6,
        "armor": 15,
    },
    "Harley Quinn": {
        "health": 15,
        "attack": 1,
        "armor": 5,
    },
    "bane": {
        "health": 15,
        "attack": 1,
        "armor": 5,
    }
}



#Combat Code Goe here
print('batman vs joker')
roll = randint(1,20) + goodpeople["batman"]["attack"]
if roll >= enemy["joker"]["armor"]:
    print("hit")
    damage = randint(1,6) + randint(1,6) + goodpeople["batman"]["attack"]
    print("batman did" ,damage, "to joker")
else:
    print("batman missed")


if enemy["joker"]["health"] <= 0:
    print("joker is died")

if enemy["joker"]["health"] > 0:

    enemy_roll = randint(1,20)  + enemy["joker"]["attack"]
    print("joker is attack back")

if enemy_roll >=  goodpeople["batman"]["armor"]:

    enemy_damage = randint(1,6) + randint(1,6) + enemy["joker"]["attack"]
    print("joker does this")
else:
    print("joker missed")






