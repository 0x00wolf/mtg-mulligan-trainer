from random import shuffle, randint
import sys

premade_decks = ['murktide', 'crashing_footfalls', 'indomitable_creativity', 'hammer_time', 'yawgmoth', 'decklist']
deck = []
shuffledDeck = []

# functions
def buildDeck(filename):
    global deck
    try:
        with open(filename, 'r') as file:
            cards = file.readlines()
    except FileNotFoundError:
        print("Error opening file.\nTry: 'python3 multrainer.py help'\nProgram exititng.")
        sys.exit()
    for card in cards:
        card = card.strip()
        deck.append(card)

def showCardsInHand():
    global cardsInHand
    print('\n'*40 + str(cardsInHand) + '\n')

def popCard():
    global cardsInHand, shuffledDeck
    cardOffTheTop = shuffledDeck.pop(0)
    cardsInHand.append(cardOffTheTop)

def drawAgain():
    draw = input('(d)raw another, (r)estart, or (q)uit?\n>> ')
    if draw == 'd':
        popCard()
        showCardsInHand()
        drawAgain()
    elif draw == 'r':
        return
    else:
        sys.exit()

def whoopsError():
    print("\n"*40 + "Whoops, that decklist isn't.")
    print("For a list of available decklists use:")
    print("python3 multrainer.py list-decks\n")
    sys.exit()

# command line input validation and usage instructions    
if len(sys.argv) != 2:
    print("\n"*40 + "**Usage example:\npython3 multrainer.py murktide\n\nFor premade deck options and more information,\ninput: multrainer.py help\n")
    sys.exit()
    
if sys.argv[1] == "help":
    print("\n"*40 + "Insert custom values into decklist.txt to use a custom deck.")
    print("For a list of decks available with the program use:")
    print("mulligantrainer.py list-decks\n")
    sys.exit()

if sys.argv[1] == "list-decks":
    print("\n"*40 +" **Example usage:\nmultrainer.py murktide\n\nAvailable decks: ")
    print("murktide, crashing_footfalls, indomitable_creativity,\nhammer_time, yawgmoth")
    print("\nTo edit the following deck lists,\nchange the values in the corresponding text files.\n")
    print("To create a custom deck, edit decklist.txt")
    sys.exit()

if sys.argv[1] in premade_decks:
    filename = "./decklists/" + sys.argv[1].lower() + ".txt"
    try:
        buildDeck(filename)
    except IndexError:
        whoopsError()
else:
    whoopsError()

# Primary logic
while True:
    cardsInHand = []
    shuffledDeck = deck.copy()
    shuffle(shuffledDeck)

    for x in range(7):
        popCard()
    showCardsInHand()
    drawAgain()            
