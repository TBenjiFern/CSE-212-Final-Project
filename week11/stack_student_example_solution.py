"""
Two Player Full-House Race
Author: Benjamin Fernelius

This is a made-up card game for two players where the goal is to be the first player to get a full-house 
(three-of-a-kind and a two-of-a-kind). This program uses a Stack in order to keep track of the discard pile.
The players have the option to draw from the draw pile (which is random) or the discard pile (which is known) after
discarding one of their five cards. The first to get a full-house wins.

"""
import random

def random_card_draw():
    pile = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace", 
    "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace", 
    "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace", 
    "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    
    random_card = random.randint(0, len(pile) - 1)
    if len(pile) > 0:
        return pile.pop(random_card)
    else:
        print("**There are no more cards in the pile!**")
        return False


def discard_pile_push(hand, card_id, discard_pile):
    player_deck = hand
    card_to_discard = card_id
    discard_pile = discard_pile
    toss_card = player_deck.pop(card_to_discard - 1)
    discard_pile.append(toss_card)
    

def discard_pile_pop(hand, card_id, discard_pile):
    player_deck = hand
    card_to_discard = card_id
    discard_pile = discard_pile
    toss_card = player_deck.pop(card_to_discard - 1)
    taken_card = discard_pile.pop()
    player_deck.append(taken_card)
    discard_pile.append(toss_card)
    

def main():
    game_on = True
    player_1 = []
    player_2 = []
    discard_pile = []
    first_player = True

    for _ in range(5):
        player_1.append(random_card_draw())
        player_2.append(random_card_draw())

    print("\n")
    print("Welcome to Race to Full-House")
    print("Beat your opponent by swapping cards in your hand with cards in the draw pile or discard pile")
    print("until you get a Full-House!")
    print("\n")
    print("Here are your hands: ")

    while game_on:
        print(f"Player 1: {player_1}")
        print(f"Player 2: {player_2}")
        print("\n")
        print("This is what's in the discard pile:")
        print(discard_pile)
        print("\n")
        if first_player:
            print("Player 1's turn!")
        else:
            print("Player 2's turn!")
        answer = input("Will you draw from Pile (P), draw from the Discard pile (D), or declare Victory (V)?\n")

        if first_player:
            if answer.upper() == "P":
                swap = int(input("Choose a card from your hand to discard (choose the placement value 1 - 5):\n"))
                checker = random_card_draw()
                if checker == False:
                    print("There are no more cards to draw! Lose a turn!")
                else:
                    discard_pile_push(player_1, swap, discard_pile)
                    player_1.append(checker)
            elif answer.upper() == "D":
                swap = int(input("Choose a card from your hand to discard (choose the placement value 1 - 5):\n"))
                if len(discard_pile) > 0:
                    discard_pile_pop(player_1, swap, discard_pile)
                else:
                    print("There is nothin in the discard pile! Lose a turn!")
            elif answer.upper() == "V":
                break
            else:
                print("I don't know what that means, so you lose a turn!")
            first_player = False
        else:
            if answer.upper() == "P":
                swap = int(input("Choose a card from your hand to discard (choose the placement value 1 - 5):\n"))
                checker = random_card_draw()
                if checker == False:
                    print("There are no more cards to draw! Lose a turn!")
                else:
                    discard_pile_push(player_2, swap, discard_pile)
                    player_2.append(checker)
            elif answer.upper() == "D":
                swap = int(input("Choose a card from your hand to discard (choose the placement value 1 - 5):\n"))
                if len(discard_pile) > 0:
                    discard_pile_pop(player_2, swap, discard_pile)
                else:
                    print("There is nothin in the discard pile! Lose a turn!")
            elif answer.upper() == "V":
                break
            else:
                print("I don't know what that means, so you lose a turn!")
            first_player = True

            
    print("Thanks for playing!")


if __name__ == "__main__":
    main()