#@author: Oscar Martinez Vega
#
#Homework - Shoe Class
#Programming Languages
#Dr. John Coleman
#
#Description:
#Shoe class – Shoe is a container of k decks of cards shuffled.
#It represents each card as an ordered pair which looks like
#(‘A’,’H’) for ace of hearts or (10,’C’) for a 10 of clubs.
#
#The constructor takes a single argument, which is the number of decks.
#The method hit deals a card from the shoe.

import random

class Shoe:
    def __init__(self, numDecks):
        self.numDecks = numDecks
        self.nums = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
        self.suits = ['C','D','H','S']
        self.Deck = []
        for x in range(self.numDecks):
            for s in self.suits:
                for n in self.nums:
                    card = n,s
                    self.Deck.append(card)
        random.shuffle(self.Deck)

    def __next__(self):
        if self.Deck == []:
            raise StopIteration
        card = self.Deck.pop(0)
        return card

    def __iter__(self):
        return self

    def __repr__(self):
        return f'Shoe({self.Deck})'

    #deals a card
    def hit(self):
        if self.Deck == []:
            raise ValueError("This shoe has no more cards")
        return self.__next__()

#Test function where I create a Shoe with 2 decks of cards
#and then I deals all cards in the shoe calling the method hit.
#After the shoe is empty, it raises an error that the shoe is empty.
def main():
    s = Shoe(2)
    print('\n')
    print(s)
    print('\n')
    print(s.hit())
    print('\n')
    print(s.hit())
    print('\n')
    for x in range(100):
        print(s.hit())
    print('\n')
    print(s)
    print('\n')
    print(s.hit())
    print('\n')
    print(s.hit())
    print('\n')
    s.hit()

main()





            
        

    
