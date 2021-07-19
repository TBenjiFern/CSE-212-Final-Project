"""
Undertale Practice Example
Author: Benjamin Fernelius

If you've played Undertale before, then you're familiar with the basic item menu which only hold 8 items!
In the game, you are able to remove item, add new items, and replace items (when at a chest). We will 
be taking inspiration from Undertale to use a Linked List to represent our own inventory!

"""
class LinkedList:

    class Node:

        def __init__(self, data):
            
            self.data = data
            self.next = None
            self.prev = None
    
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, value):

        new_node = LinkedList.Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node 
    
    def insert_tail(self, value):

        new_node = LinkedList.Node(value)

        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail 
            self.tail.next = new_node 
            self.tail = new_node

    def remove_head(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head is not None:
            self.head.next.prev = None 
            self.head = self.head.next
        
    def remove_tail(self):

        if self.tail == self.head:
            self.tail = None
            self.head = None
        elif self.tail is not None:
            self.tail.prev.next = None 
            self.tail = self.tail.prev

    def insert_after(self, value, new_value):

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

        curr = self.head 
        while curr is not None:
            yield curr.data  
            curr = curr.next

    def __reversed__(self):

        curr = self.tail 
        while curr is not None:
            yield curr.data 
            curr = curr.prev 

    def __str__(self):

        output = ""
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        return output

def random_items(request):
    items = ["Bandage", "Monster Candy", "Spider Donut", "Spider Cider", "Butterscotch Pie", "Snail Pie", "Snowman Piece",
    "Nice Cream", "Bisicle", "Unisicle", "Cinnamon Bunny", "Astronaut Food", "Crab Apple", "Sea Tea", "Abandoned Quiche", "Temmie Flakes",
    "Dog Salad", "Instant Noodles", "Hot Dog...?", "Hot Cat", "Junk Food", "Hush Puppy", "Starfait", "Glamburger", "Legendary Hero",
    "Steak in the Shape of Mettaton's Face", "Popato Chisps", "Bad Memory", "Last Dream", "Puppydough Icecream", "Pumpkin Rings",
    "Rock Candy", "Croquet Roll", "Ghost Fruit", "Stoic Onion", "Stick", "Toy Knife", "Tough Glove", "Ballet Shoes", "Torn Notebook", 
    "Burnt Pan", "Empty Gun", "Worn Dagger", "Real Knife", "Faded Ribbon", "Manly Bandana", "Old Tutu", "Cloudy Glasses", "Temmie Armor",
    "Stained Apron", "Cowboy Hat", "Heart Locket", "The Locket", "Punch Card", "Annoying Dog", "Dog Residue", "Mystery Key", "Silver Key",
    "Undyne's Letter", "Undyne's Letter EX"]

    items_compare = ["BANDAGE", "MONSTER CANDY", "SPIDER DONUT", "SPIDER CIDER", "BUTTERSCOTCH PIE", "SNAIL PIE", "SNOWMAN PIECE",
    "NICE CREAM", "BISICLE", "UNISICLE", "CINNAMON BUNNY", "ASTRONAUT FOOD", "CRAB APPLE", "SEA TEA", "ABANDONED QUICHE", "TEMMIE FLAKES",
    "DOG SALAD", "INSTANT NOODLES", "HOT DOG...?", "HOT CAT", "JUNK FOOD", "HUSH PUPPY", "STARFAIT", "GLAMBURGER", "LEGENDARY HERO",
    "STEAK IN THE SHAPE OF METTATON'S FACE", "POPATO CHISPS", "BAD MEMORY", "LAST DREAM", "PUPPYDOUGH ICECREAM", "PUMPKIN RINGS",
    "ROCK CANDY", "CROQUET ROLL", "GHOST FRUIT", "STOIC ONION", "STICK", "TOY KNIFE", "TOUGH GLOVE", "BALLET SHOES", "TORN NOTEBOOK", 
    "BURNT PAN", "EMPTY GUN", "WORN DAGGER", "REAL KNIFE", "FADED RIBBON", "MANLY BANDANA", "OLD TUTU", "CLOUDY GLASSES", "TEMMIE ARMOR",
    "STAINED APRON", "COWBOY HAT", "HEART LOCKET", "THE LOCKET", "PUNCH CARD", "ANNOYING DOG", "DOG RESIDUE", "MYSTERY KEY", "SILVER KEY",
    "UNDYNE'S LETTER", "UNDYNE'S LETTER EX"]

    if request.upper() in items_compare:
        return request

def main():
    game_on = True
    inventory = LinkedList()
    inventory.insert_tail(random_items("Bandage"))
    inventory.insert_head(random_items("Stick"))

    print(inventory)

    while game_on:
        pass


if __name__ == "__main__":
    main()