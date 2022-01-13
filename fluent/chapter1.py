import random
class Monster:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Monster(name='{self.name}')"

class Field:
    def __init__(self):
        self._monsters = []

    def append(self, monster):
        self._monsters.append(monster)

    def __getitem__(self, position):
        return self._monsters[position]

    def __len__(self):
        return len(self._monsters)

field = Field()

for name in ['g1', 'g2', 'g3', 'g4', 'g5']:
    field.append(Monster(name))

print(f"랜덤뽑기! >> {random.choice(field)}")
print(list(reversed(field)))


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result


class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        result = self.first + self.second
        return result

cal = FourCal()
cal.setdata(4,2)



# 1.1 파이썬 카드 한 벌

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JKQA')
    suits = 'spades,diamonds,clubs,hearts'.split(",")

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7', 'diamonds')
print(beer_card)

card = FrenchDeck()
print(len(card))

from random import choice
print(choice(card))


suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(card, key=spades_high):
    print(card)

print(_cards)



