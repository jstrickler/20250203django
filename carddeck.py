import random
from card import Card

class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'clubs diamonds hearts spades'.split()

    def __init__(self):
        self._build_deck()

    def _build_deck(self):
        self._cards = []  # list of cards
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        class_name = type(self).__name__
        return f"{class_name}/{len(self)}"

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}()"

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

if __name__ == "__main__":
    d1 = CardDeck()
    d2 = CardDeck()
    print(d1)
    d2.shuffle()
    print(f"{d2.cards = }\n")
    for i in range(5):
        print(d2.draw())
    print(f"{len(d2) = }")
    print(d2)
    print(repr(d2))
    print(f"{d2.get_ranks() = }")
    print(f"{CardDeck.get_ranks() = }")
    
    