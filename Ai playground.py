import random
import time


# Functions for sound effects and pauses
def typewriter_effect(text, speed=0.05):
    """Simulate a typewriter effect for suspense."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print()  # To move to the next line


def scary_noise():
    """Play a simple spooky sound or message."""
    spooky_sounds = ["*Eerie sound in the distance...*", "*A door creaks open slowly...*"]
    print(random.choice(spooky_sounds))


def intro():
    """Introduction to the game."""
    typewriter_effect("You are standing in front of an old, creepy house.")
    typewriter_effect("The door is slightly ajar, and you feel a cold breeze coming from inside.")
    time.sleep(1)


def first_choice():
    """The first choice the player makes."""
    typewriter_effect("Do you want to enter the house? (yes/no)")
    choice = input("> ").strip().lower()

    if choice == "yes":
        typewriter_effect("You slowly push the door open and step inside...")
        spooky_event()
    elif choice == "no":
        typewriter_effect("You decide it's too dangerous and walk away, but you hear a whisper behind you...")
        spooky_event()
    else:
        typewriter_effect("That's not a valid choice. Try again.")
        first_choice()


def spooky_event():
    """Random spooky event that happens."""
    event = random.choice([jump_scare, strange_noise, find_object])
    event()


def jump_scare():
    """A jump scare event."""
    typewriter_effect("Suddenly, a loud BANG! Something crashes in the room next to you...")
    scary_noise()
    game_over()


def strange_noise():
    """Strange noise event."""
    typewriter_effect("You hear a faint whisper in the dark: 'Help me...'. The air feels heavy.")
    scary_noise()
    time.sleep(1)
    next_choice()


def find_object():
    """Player finds something mysterious."""
    typewriter_effect("You find an old, dusty book on the floor. It looks ancient.")
    typewriter_effect("As you open the book, a ghostly face appears on the pages!")
    scary_noise()
    next_choice()


def next_choice():
    """The player makes another choice after a spooky event."""
    typewriter_effect("Do you want to continue exploring? (yes/no)")
    choice = input("> ").strip().lower()

    if choice == "yes":
        spooky_event()
    elif choice == "no":
        game_over()
    else:
        typewriter_effect("Invalid input! Try again.")
        next_choice()


def game_over():
    """Ending the game with a spooky conclusion."""
    typewriter_effect("The lights flicker and suddenly go out. You feel something behind you...")
    typewriter_effect("It’s too late... Game over.")
    exit()


# Main game loop
def main():
    intro()
    first_choice()


if __name__ == "__main__":
    main()