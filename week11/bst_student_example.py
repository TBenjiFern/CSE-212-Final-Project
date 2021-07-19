"""
Balancing BST Student Example
Author: Benjamin Fernelius

This code demonstrates the uses of a Binary Search Tree in creating a balanced BST and in comparing heights. 
This is a simple exercise which enables the user to add numbers to a BST and then check it's height.
A balanced BST method is also included so the user can compare their tree with the balanced tree example.
This way they can see how balanced their work is.
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
    
    def get_height(self):

        if self.root is None:
            return 0
        else:
            result_left = self.recurse_height(self.root)
            result_right = self.recurse_height(self.root, result_left)

            if result_left > result_right:
                return result_left
            else:
                return result_right
    
    def recurse_height(self, node, result_left=None, count=0):
        
        if result_left == None:
            if node is not None:
                count += 1
                return self.recurse_height(node.left, None, count)
            else:
                return count
        else:
            if node is not None:
                count += 1
                return self.recurse_height(node.right, result_left, count)
            else:
                return count
    

def create_balanced_bst(list):
    
    bst = BST()
    recurse_middle(list, 0, len(list) - 1, bst)
    return bst


def recurse_middle(list, first, last, bst):

    if len(list) != 0:
        halfway = (first + last) // 2
        if bst.root == None:
            bst.insert(list[halfway])
            recurse_middle(list, first, halfway, bst)
            recurse_middle(list, halfway + 1, last, bst)
        else:
            if list[halfway] in bst:
                pass
            else:
                bst.insert(list[halfway])
                recurse_middle(list, first, halfway, bst)
                recurse_middle(list, halfway + 1, last, bst)

def main():
    game_on = True
    number_list = [135, 948, 22, 239, 167, 734, 53, 19, 540, 389, 679]
    sorted_num_list = []
    bst = BST()
    print("\nWelcome to the Balanced BST creator!\n")
    print("Your objective is to try and create a balanced BST by inserting numbers into the correct order.")
    print("You have a premade list of numbers which need to be inserted into a BST. ")
    print("Try your best to make it even! A balanced BST will be displayed after to compare your results with!\n")

    while game_on:
        if len(number_list) == 0:
            print("All of the numbers have been inserted!\n")
            game_on = False
        else:
            print("Your number list: ")
            print(number_list, "\n")
            answer = input("What will you do? Insert a number (I), Look at your BST (L), or Check the height (H)?\n")

            if answer.upper() == "I":
                num = input("Which number will you insert (Choose num position from list 1 - max)?\n")
                insert = number_list.pop(int(num) - 1)
                bst.insert(insert)
                print(f"Inserted {insert} to BST\n")
            elif answer.upper() == "L":
                print("You have the following numbers in your BST: ")
                for number in bst:
                    print(number)
                print()
            elif answer.upper() == "H":
                print("The height of your BST is:")
                print(bst.get_height())
                print()
            else:
                print("Not sure about that command, try again!")
    print("After all that work, this is the height of your BST:")
    print(bst.get_height())
    print()
    print("Now, let's see how it compares to the balanced BST!\n")
    for number in bst:
        sorted_num_list.append(number)
    print(sorted_num_list)
    balanced_bst = create_balanced_bst(sorted_num_list)
    print("Height of balanced bst:")
    print(balanced_bst.get_height())
    print()
    print("How did you do?\n")


if __name__ == "__main__":
    main()
