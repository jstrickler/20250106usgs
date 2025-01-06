
class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    @rank.setter
    def rank(self, value):
        pass

    def __repr__(self):
        return f"Card('{self._rank}', '{self._suit}')"

    def __str__(self):
        return f"{self.rank}-{self.suit}"
