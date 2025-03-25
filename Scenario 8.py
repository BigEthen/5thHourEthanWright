#Name:Ethan Wright
#Class: 5th Hour
#Assignment: Scenario8
import random

#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)

class Character:
    def __init__(self,name,health,attack,defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
    def is_alive(self):
        return self.health > 0
    def take_damage(self, damage):
        self.damage -= damage
        print(f"{self.name} takes {damage} damage!")
        if not self.is_alive():
            print(f"{self.name} has been defeated!")
    def attacl_target(self , target):
        damage = max(0, self.attack - target.defense)
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)
    if __name__ == "__main__":
        player = character("hero", 100, 20,10)
        enemy= character("goblin",60,15,5)
        print("A wild Goblin appears!")
        while player.is_alive() and enemy.is_alive():
            player.attack_target(enemy)
            if not enemy.is_alive():
                break
            enemy.attack_target(player)
        if player.is_alive():
            print(f"{player.name}wins!")
        else:
            print(f"{enemy.name}wins!")
