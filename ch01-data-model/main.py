import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    rank = [str(n) for n in range(2, 11)] + list('JQKA')
    suit = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.rank for suit in self.suit]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __repr__(self) -> str:
        return "a"

    #def __str__(self) -> str:
     #   return "b"

deck = FrenchDeck()
print(deck)
print(len(deck))
print(deck[0])

print(Card('a', 'saj') in deck)


