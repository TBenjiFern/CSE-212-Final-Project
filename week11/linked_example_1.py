"""
Yu-Gi-Oh-esque Deck Editing/Formation Program
Author: Benjamin Fernelius

This code demonstrates the uses of Linked Lists by using said structure to organize,
expand, delete, replace, and customize your very own Yu-gi-oh deck. Many games
have a function of some sort which enables the player to keep an organized list of times in check,
so this program will demonstrate a potential framework for how those games might work!

"""
import random

# This is the Linked List class. In other words, here is where the magic happens!
class LinkedList:

    class Node: # embedded class Nodes creates and keeps track of each node in our list

        def __init__(self, data):
            
            self.data = data
            self.next = None
            self.prev = None
    
    def __init__(self): # initializes head and tail variables for identification
        self.head = None
        self.tail = None

    def insert_head(self, value):
        # this inserts into the first position/front of the linked list
        new_node = LinkedList.Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node 
    
    def insert_tail(self, value):
        # this inserts into the last position/end of the linked list
        new_node = LinkedList.Node(value)

        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail 
            self.tail.next = new_node 
            self.tail = new_node

    def remove_head(self):
        # removes value in head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head is not None:
            self.head.next.prev = None 
            self.head = self.head.next
        
    def remove_tail(self):
        # removes value in tail
        if self.tail == self.head:
            self.tail = None
            self.head = None
        elif self.tail is not None:
            self.tail.prev.next = None 
            self.tail = self.tail.prev

    def insert_after(self, value, new_value):
        # inserts new value immediately one position after determined value
        curr = self.head
        while curr is not None:
            if curr.data == value:
                if curr == self.tail:
                    self.insert_tail(new_value)
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = curr       
                    new_node.next = curr.next  
                    curr.next.prev = new_node  
                    curr.next = new_node      
                return 
            curr = curr.next

    def remove(self, value):
        # removes any value in list
        curr = self.head
        while curr is not None:
            if curr.data == value:
                if curr == self.head:
                    self.remove_head()   
                elif curr == self.tail:
                    self.remove_tail()
                else:
                    curr.next.prev = curr.prev 
                    curr.prev.next = curr.next 
                return
            curr = curr.next
    
    def replace(self, old_value, new_value):
        # replaces an existing value with a new one
        curr = self.head
        while curr is not None: 
            if curr.data == old_value: 
                curr.data = new_value 
            curr = curr.next 
            
    def length(self):
        # returns length of the linked list
        count = 0
        for _ in self:
            count += 1
        return count

    def __iter__(self):
        # used to iterate forwards through list
        curr = self.head 
        while curr is not None:
            yield curr.data  
            curr = curr.next

    def __reversed__(self):
        # used to interate backwards through list
        curr = self.tail 
        while curr is not None:
            yield curr.data 
            curr = curr.prev 

    def __str__(self):
        # used to print out contents of list in a string
        output = ""
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        return output

def card_list(card_name):
    # this method keeps track of cards which we "own"
    # this list is normally formated names
    card_pool_normal = ["Mystical Elf", "Feral Imp", "Winged Dragon", "Summoned Skull", "Beaver Warrior", "Dark Magician", "Gaia The Fierce Knight",
    "Curse of Dragon", "Celtic Guardian", "Mammoth Graveyard", "Great White", "Silver Fang", "Giant Soldier of Stone",
    "Dragon Zombie", "Doma The Angel of Silence", "Ansatsu", "Witty Phantom", "Claw Reacher", "Mystic Clown", "Sword of Dark Destruction",
    "Book of Secret Arts", "Dark Hole", "Dian Keto the Cure Master", "Ancient Elf", "Magical Ghost", "Fissure", "Trap Hole", "Two-Pronged Attack",
    "De-Spell", "Monster Reborn", "Reinforcements", "Change of Heart", "The Stern Mystic", "Wall of Illusion", "Neo the Magic Swordsman",
    "Baron of the Fiend Sword", "Man-Eating Treasure Chest", "Sorcerer of the Doomed", "Last Will", "Waboku", "Soul Exchange", 
    "Card Destruction", "Trap Master", "Dragon Capture Jar", "Yami", "Man-Eater Bug", "Reverse Trap", "Remove Trap", "Castle Walls", 
    "Ultimate Offering", "Griffore", "Kuriboh", "Swords of Revealing Light", "Blue-Eyes White Dragon", "Hitotsu-Me Giant",
    "Battle Ox", "Koumori Dragon", "Rougue Doll", "Mystic Horseman", "Unknown Warrior of Fiend", "Rude Kaiser", "Pale Beast",
    "Dark Magician Girl", "Catapult Turtle", "Exodia the Forbidden One", "Right Leg of the Forbidden One", "Left Leg of the Forbidden One",
    "Right Arm of the Forbidden One", "Left Arm of the Forbidden One", "Brain Control", "Monster Recovery", "Mystic Box", "Horn of the Unicorn", 
    "Multiply", "Detonate", "Polymerization", "Mirror Force", "Magical Hats", "Buster Blader", "Jack's Knight", "Queen's Knight", 
    "King's Knight", "Big Shield Gardna", "Pot of Greed", "Exchange", "Spellbinding Circle", "Chain Destruction", "Chimera the Flying Mythical Beast",
    "Green Gadget", "Red Gadget", "Yellow Gadget", "Magician's Circle", "Dark Paladin"]
    # this list is for searching for specific names using upper()
    card_pool = ["MYSTICAL ELF", "FERAL IMP", "WINGED DRAGON", "SUMMONED SKULL", "BEAVER WARRIOR", "DARK MAGICIAN", "GAIA THE FIERCE KNIGHT",
    "CURSE OF DRAGON", "CELTIC GUARDIAN", "MAMMOTH GRAVEYARD", "GREAT WHITE", "SILVER FANG", "GIANT SOLDIER OF STONE",
    "DRAGON ZOMBIE", "DOMA THE ANGEL OF SILENCE", "ANSATSU", "WITTY PHANTOM", "CLAW REACHER", "MYSTIC CLOWN", "SWORD OF DARK DESTRUCTION",
    "BOOK OF SECRET ARTS", "DARK HOLE", "DIAN KETO THE CURE MASTER", "ANCIENT ELF", "MAGICAL GHOST", "FISSURE", "TRAP HOLE", "TWO-PRONGED ATTACK",
    "DE-SPELL", "MONSTER REBORN", "REINFORCEMENTS", "CHANGE OF HEART", "THE STERN MYSTIC", "WALL OF ILLUSION", "NEO THE MAGIC SWORDSMAN",
    "BARON OF THE FIEND SWORD", "MAN-EATING TREASURE CHEST", "SORCERER OF THE DOOMED", "LAST WILL", "WABOKU", "SOUL EXCHANGE", 
    "CARD DESTRUCTION", "TRAP MASTER", "DRAGON CAPTURE JAR", "YAMI", "MAN-EATER BUG", "REVERSE TRAP", "REMOVE TRAP", "CASTLE WALLS", 
    "ULTIMATE OFFERING", "GRIFFORE", "KURIBOH", "SWORDS OF REVEALING LIGHT", "BLUE-EYES WHITE DRAGON", "HITOTSU-ME GIANT",
    "BATTLE OX", "KOUMORI DRAGON", "ROUGUE DOLL", "MYSTIC HORSEMAN", "UNKNOWN WARRIOR OF FIEND", "RUDE KAISER", "PALE BEAST",
    "DARK MAGICIAN GIRL", "CATAPULT TURTLE", "EXODIA THE FORBIDDEN ONE", "RIGHT LEG OF THE FORBIDDEN ONE", "LEFT LEG OF THE FORBIDDEN ONE",
    "RIGHT ARM OF THE FORBIDDEN ONE", "LEFT ARM OF THE FORBIDDEN ONE", "BRAIN CONTROL", "MONSTER RECOVERY", "MYSTIC BOX", "HORN OF THE UNICORN", 
    "MULTIPLY", "DETONATE", "POLYMERIZATION", "MIRROR FORCE", "MAGICAL HATS", "BUSTER BLADER", "JACK'S KNIGHT", "QUEEN'S KNIGHT", 
    "KING'S KNIGHT", "BIG SHIELD GARDNA", "POT OF GREED", "EXCHANGE", "SPELLBINDING CIRCLE", "CHAIN DESTRUCTION", "CHIMERA THE FLYING MYTHICAL BEAST",
    "GREEN GADGET", "RED GADGET", "YELLOW GADGET", "MAGICIAN'S CIRCLE", "DARK PALADIN"]

    if card_name.upper() in card_pool: # if card is in pool, return it
        return card_name
    elif card_name.upper() == "RANDOM": # return random card
        return card_pool_normal[random.randint(0, len(card_pool) - 1)]
    elif card_name.upper() == "POOL": # display entire pool
        print(card_pool_normal, "\n")
    else: # if input error
        print("Either your input was incorrect or you don't own that card!")
        return False


def main():
    game_on = True # loop boolean
    deck = LinkedList() # create linked list
    # add 10 cards to deck to start
    deck.insert_tail(card_list("Man-Eater Bug"))
    deck.insert_head(card_list("Monster Reborn"))
    deck.insert_head(card_list("Dark Hole"))
    deck.insert_head(card_list("Mystical Elf"))
    deck.insert_head(card_list("Feral Imp"))
    deck.insert_head(card_list("Beaver Warrior"))
    deck.insert_head(card_list("Great White"))
    deck.insert_head(card_list("Griffore"))
    deck.insert_head(card_list("Kuriboh"))
    deck.insert_head(card_list("Swords of Revealing Light"))
    
    print("\nWelcome to the Yu-Gi-Oh deck builder!\n")
    print("You currently have a deck with 10 pre-set cards and are free to add, replace, and delete cards")
    print("to make the perfect deck. Remember that you have a limited deck size of 30 cards!\n")

    print(f"This is your default deck: ({deck.length()}/30)")
    print(deck, "\n")

    while game_on:  # game loops while true
        print("Deck Builder Interface:")
        print("Press \"L\" to display commands.\n")

        response = input("Enter input: ")
        # options for taking inputs and completing actions
        if response.upper() == "I": # add to linked list
            if deck.length() >= 30:
                print("Your deck is full! You can't add any more.\n")
            else:
                print(deck, "\n")
                print("What card would you like to add? (Enter: \"Card Name\" (\"Random\" is also an option!) and \"Position\" (Head, Tail, or Card Name (will insert after said card)))")
                name = input("Enter Card Name: ")
                position = input("Enter Position: ")
                if card_list(name) != False:
                    if position.upper() == "HEAD":
                        deck.insert_head(card_list(name))
                    elif position.upper() == "TAIL":
                        deck.insert_tail(card_list(name))
                    else:
                        deck.insert_after(position, name)
                else:
                    print("I didn't catch that card name, please try again!")
        elif response.upper() == "R": # replace value in linked list
            print(deck)
            print("Which card would you like to replace? (Enter: \"Old Card\" and \"New Card\")")
            old = input("Old Card: ")
            new = input("New Card: ")
            if card_list(old) != False and card_list(new) != False:
                deck.replace(old, new)
            else:
                print("Invalid input.")
        elif response.upper() == "D": # delete value in linked list
            print(deck)
            print("Please determine which card to delete.")
            delete = input("Enter Card Name: ")
            deck.remove(delete)
        elif response.upper() == "P": # display pool
            card_list("pool")
        elif response.upper() == "DECK": # display deck
            print(deck)
        elif response.upper() == "E": # exit program
            game_on = False
        elif response.upper() == "L": # display commands
            print("Enter \"I\" to insert a card to your deck.")
            print("Enter \"R\" to replace a card in your deck with another.")
            print("Enter \"D\" to delete a card in your deck.")
            print("Enter \"P\" to display list of card available to add to your deck.")
            print("Enter \"Deck\" to display your current deck.")
            print("Enter \"E\" to exit this program.\n")
        else: # catch errors
            print("I didn't catch that. Please try again!")


if __name__ == "__main__":
    main()