"""
Rock Picking BST Example
Author: Benjamin Fernelius

This code demonstrates the uses of a Binary Search Tree to organize and quickly reference data by inserting into,
traversing through, and referencing items found in a BST. To be completely honest, this code is rather silly because a BST
is most effective when having to deal with a LOT of information because of its efficiency at referencing data. However,
this simple example focuses on how to get inserting, searching, and traversing to work using BSTs

"""

import random

class BST:

    class Node:

        def __init__(self, data):

            self.data = data
            self.left = None
            self.right = None
    
    def __init__(self):

        self.root = None

    def insert(self, data):
        
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self.recurse_insert(data, self.root)
    
    def recurse_insert(self, data, node):

        if data == node.data:
            pass
        elif data < node.data:
            if node.left is None:
                node.left = BST.Node(data)
            else:
                self.recurse_insert(data, node.left)
        else:
            if node.right is None:
                node.right = BST.Node(data)
            else:
                self.recurse_insert(data, node.right)
    
    def __contains__(self, data):
        if self.root == None:
            pass
        else:
            return self.recurse_contains(data, self.root)

    def recurse_contains(self, data, node):

        if data == node.data:
            return True
        elif data < node.data:
            if node.left is None:
                return False
            else:
                return self.recurse_contains(data, node.left)
        else:
            if node.right is None:
                return False
            else:
                return self.recurse_contains(data, node.right)

    def __iter__(self):

        yield from self.traverse(self.root)
    
    def traverse(self, node):
        
        if node is not None:
            yield from self.traverse(node.left)
            yield node.data
            yield from self.traverse(node.right)


def stone_pickup():
    stones = ["Red Stone", "Blue Stone", "Green Stone", "Yellow Stone", "Purple Stone", "Nothing"]

    return stones[random.randint(0, len(stones) - 1)]

def main():
    game_on = True
    red = False
    blue = False
    green = False
    yellow = False
    purple = False

    inv_manager = BST()
    print("\nWelcome to our silly rock picking up game!\n")
    print("You find yourself stuck in an enclosed area and find a door with 5 slots in it.")
    print("In order to open the door to escape, you must find one of each type of rock in your surroundings:")
    print("A Red, Green, Blue, Yellow, and Purple rock.\n")
    print("Start searching!\n")

    while game_on:
        answer = input("What will you do? Search for rocks (S), Try the door (T), or Look at your inventory (L)?\n")

        if answer.upper() == "S":
            print("You rustle through some bushes and find: ")
            draw = stone_pickup()
            if draw == "Nothing":
                print("Nothing... Try again in another bush.\n")
            elif draw in inv_manager:
                print(f"Another {draw}... Let's toss this and try again!\n")
            else:
                print(f"A {draw}! Let's add it to our bag.\n")
                inv_manager.insert(draw)
        elif answer.upper() == "T":
            print("You walk up to the door and try to see if you can open it.\n")
            if "Red Stone" in inv_manager:
                red = True
                print("You insert the Red Stone\n")
            else:
                print("You are missing the Red Stone!\n")
            if "Blue Stone" in inv_manager:
                blue = True
                print("You insert the Blue Stone\n")
            else:
                print("You are missing the Blue Stone!\n")
            if "Green Stone" in inv_manager:
                green = True
                print("You insert the Green Stone\n")
            else:
                print("You are missing the Gree Stone!\n")
            if "Yellow Stone" in inv_manager:
                yellow = True
                print("You insert the Yellow Stone\n")
            else:
                print("You are missing the Yellow Stone!\n")
            if "Purple Stone"in inv_manager:
                purple = True
                print("You insert the Purple Stone\n")
            else:
                print("You are missing the Purple Stone!\n")
            if red and blue and green and yellow and purple:
                print("The door swings open and you run free. Nice job!\n")
                game_on = False
            else:
                print("Looks like you'll need to do a bit more searching!\n")
        elif answer.upper() == "L":
            print("You have the following items in your bag: ")
            for item in inv_manager:
                print(item)
            print()
        else:
            print("*You twiddle your thumbs back and forth for a while*")
            print("Maybe I should do something...\n")


if __name__ == "__main__":
    main()
