
import random
import time

# cards categories
cards = {'club':['jack', 'king', 'queen', 'ace', 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'diamond':['jack', 'king', 'queen', 'ace', 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'heart':['jack', 'king', 'queen', 'ace', 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'spade':['jack', 'king', 'queen', 'ace', 2, 3, 4, 5, 6, 7, 8, 9, 10]
        }

higherCards = {
    'jack':11,
    'ace':14,
    'queen':12,
    'king':13
}

# testing the cards
cardInputed = input("Card $")


def cardsManager(cardInputed):
    cardChecker = cards[cardInputed]

    print(f"The cards for {cardInputed} are : ")
    for elements in cardChecker:
        if elements == 'jack':
            elements = higherCards['jack']
        if elements == 'ace':
            elements=higherCards['ace']
        if elements == 'king':
            elements=higherCards['king']
        if elements == 'queen':
            elements = higherCards['queen']
            
        


def player(players):
    for player in range(players):
        call = input(f"Player{player+1} card for round{rounds+1} ~#") 
    if call in cardsManager(cardInputed):
        print(call)

"""
main = ['club', 'diamond', 'heart', 'spade']
for index in main:
    _choice = random.shuffle(cards[index])
print(cards)
"""

try:
    print("\n")
    numberOfRounds = int(input("ENter the number of cycles to go ~#"))
    
    for rounds in range(numberOfRounds):
        players = int(input(f"Players involved  in round{rounds+1}~#"))
        player(players)
        time.sleep(10)
        print(f" round{rounds+1} ended... ".center(50,"*"))

except Exception as Ex:

    print(Ex)

