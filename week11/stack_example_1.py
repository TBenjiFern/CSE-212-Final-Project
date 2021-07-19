"""
Enter the Gungeon-esque Item Shuffle
Author: Benjamin Fernelius

This code mimics the swap gun function which Enter the Gungeon uses.
In order to better display the uses of Stacks, the functionality differs
from the original game in include sorting through more weapons, but the concept
is preserved.

"""

import random

def gun_generator():
    gun_list = ["Rusty Sidearm", "Marine Sidearm", "Rogue Special", "Budget Revolver",
    "Dart Gun", "Robot's Right Hand", "Slinger", "Blasphemy", "Casey", "Pea Shooter",
    "38 Special", "Derringer", "Trank Gun", "Unfinished Gun", "Elimentaler", "Bullet", 
    "Shell", "Hyper Light Blaster", "Boxing Glove", "Makarov", "M1911", "Magnum", 
    "Colt 1851", "SAA", "Cold 45", "Polaris", "Jolter", "Dungeon Eagle", "Grey Mauser", 
    "Vorpal Gun", "High Kaliber", "Shellegun", "Dueling Pistol", "AU Gun", "Big Iron", 
    "Composite Gun", "Flare Gun", "Smiley's Revolver", "Shades's Revolver", "Knight's Gun"]

    random_gun = random.randint(0, len(gun_list) - 1)

    return gun_list[random_gun]

def gun_stack_push(gun_stack):
    gun_stack.append(gun_generator())
    print(gun_stack)

def gun_stack_pop(gun_stack):
    if len(gun_stack) > 0:
        gun = gun_stack.pop()
        print(f"*Ran out of ammo and discarded {gun}*")
        print(gun_stack)
    else:
        print("You don't have any weapons! Get one first!")

def main():
    game_on = True
    gun_stack = []
    print("Welcome to Enter The Gungeon Gun Rotator")
    print("You will be prompted to either Acquire a gun (A), Shoot the gun (S), or Exit the game (E).")
    print("The purpose of this game is to demonstrate how a Stack keeps track of items!")
    while game_on:
        answer = input("Make a decision: Acquire weapon (A), Shoot weapon (S), or Exit program: (E)\n")
        if answer.upper() == "A": 
            gun_stack_push(gun_stack)
        elif answer.upper() == "S":
            gun_stack_pop(gun_stack)
        elif answer.upper() == "E":
            game_on = False
        else:
            print("Didn't recognize input, try again.")
    print("Program Exited")
        
if __name__ == "__main__":
    main()