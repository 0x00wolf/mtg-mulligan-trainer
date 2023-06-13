from random import shuffle, randint
import sys

deck = []
shuffledDeck = []
statDeck = []
uniqueDeck = []
tallyDeck = []

class Card:
    def __init__(self, name):
        self.name = name
        self.count = 0

def popCard():
    global cardsInHand, shuffledDeck
    cardOffTheTop = shuffledDeck.pop(0)
    cardsInHand.append(cardOffTheTop)

# build the deck
filename = "./decklists/scam.txt"
with open(filename, 'r') as file:
    cards = file.readlines()
for card in cards:
    card = card.strip()
    deck.append(card)

deckCopy = deck.copy()
uniqueDeck = set(deckCopy)
uniqueDeckList = (list(uniqueDeck))

for cards in uniqueDeckList:
    cardObj = Card(cards)
    tallyDeck.append(cardObj)
    
for x in range(100000):               
    cardsInHand = []
    shuffledDeck = deck.copy()
    shuffle(shuffledDeck)

    for x in range(7):
        popCard()
    setUniqueCards = set(cardsInHand)
    uniqueCards = (list(setUniqueCards))
    for card in uniqueCards:
        for cards in tallyDeck:
            if cards.name == card:
                cards.count += 1

print("Card:\t\tPercentage:")
for cards in tallyDeck:
    print(f"{cards.name}:{(cards.count / 100000): .1%}")
