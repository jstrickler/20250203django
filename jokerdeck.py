from card import Card
from carddeck import CardDeck

class JokerDeck(CardDeck):
    def _build_deck(self):
        super()._build_deck() # call method in parent (or other ancestor)
        for joker_rank in "joker1", "joker2":
            card = Card(joker_rank, "JOKER")
            self._cards.append(card)


if __name__ == "__main__":
    j1 = JokerDeck()
    j2 = JokerDeck()
    j1.shuffle()
    print(f"{j1.cards = }")
    print(f"{len(j2) = }")
    print(f"{j1 = }")
    print(j1)
    