class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def get_rank(self):  # getter method
        return self._rank

    @property
    def rank(self):
        return self._rank
    # rank = property(rank)

    @property
    def suit(self):
        return self._suit

    @rank.setter
    def rank(self, value):
        self._rank = value

    def __repr__(self):
        return f"Card('{self._rank}', '{self._suit}')"

    def __str__(self):
        return f"{self.rank}-{self.suit}"

if __name__ == "__main__":
    c = Card('10', 'Diamonds')
    print(f"{c = }")
    print(c.get_rank())
    print(f"{c.rank = }")
    c.rank = "A"
    print(f"{c = }")
    