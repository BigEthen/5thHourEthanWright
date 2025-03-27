#Name:
#Class: 5th Hour
#Assignment: HW24

import random, time

#1. Copy over your class from HW23 and all the functions inside of it, and alter any functions to use self if applicable.
class Character:
    def __init__(self,health,damage,speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    def take_damage(self):
        for i in range(10):
            damage = random.randint(1, 6)
            self.health -= damage
            print(self.health)
            time.sleep(1)

    def heal_warrior(self, warrior):
        warrior.health += 30
        if warrior.health > 100:
            warrior.health = 100

#2. Create a fourth attribute in the class called max_health that has the same values as health
    def max_health(self, health):
        health.health = 100
#3. Copy the warrior and healer objects from HW23, and then make two more character objects with the following attribute values: thief (health/max: 50, damage: 30, speed: 40) and mage (health/max: 45, damage:35, speed: 25)
healer = Character(100,15,30)
warrior = Character(100,20,30)
thief = Character(50,30,40)
mage = Character(45,35,25)
#4. Randomly choose one of the four character objects to take the damage over time function and call the function to them
thief()
#5. Determine who lost health by comparing the current health to the max_health and heal that character object by calling your healing function to that object and then print their health afterwards.
heal_warrior  max_health