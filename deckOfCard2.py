# Required dependencies
from random import shuffle

# Deck of cards

class Card(object):
    def __init__(self, suit, value, image=None):
        self.suit = suit
        self.value = value
        self.image = image

class Deck(object):
    def __init__(self, suits, values):
        self.suits = suits
        self.values = values
        self.deck = []
        self.buildDeck()

    def buildDeck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append(Card(suit, value))
        self.shuffle()
        return self

    def shuffle(self):
        shuffle(self.deck)
        return self

    def deal(self):
        if self.deck: # empty lists return as False
            # removes and returns card from deck, shuffled or not
            return self.deck.pop()
        else:
            print "No more cards"

    def returnCard(self, card, reShuffle = False):
        self.deck.append(card)
        if reShuffle:
            self.shuffle()
        return self

    def resetDeck(self):
        self.deck = []
        self.buildDeck()
        return self


# GAME LOGIC
# def show


suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = range(1,14)
print values
deck = Deck(suits, values)
# deck.buildDeck()

print deck.deck.pop().value
print deck.deck.pop().value

# deck.shuffle()

deck.resetDeck()


# print deck.deck[0].value
# print deck.deck[0].suit



# print card.value
