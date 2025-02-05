class Card:  # inherits from 'object'
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
    
    @property
    def rank(self):
        return self._rank
    
    @property
    def suit(self):
        return self._suit
    
    def __str__(self):  # returns value for str(self)
        return f"{self.rank}-{self.suit}"

    def __repr__(self): # returns value for repr(self)
        return f"Card('{self.rank}', '{self.suit}')"

if __name__ == "__main__":
    c = Card("9", "diamonds")
#    print(f"{c._rank = }")  # VERY NAUGHTY!!!!
    print(f"{c.rank = }")
    print(f"{c.suit = }")
    print(c)   # uses str()
    print(f"{c = }") # uses repr()
    print(f"{type(c) = }")
    
