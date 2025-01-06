from carddeck import CardDeck, Card

JOKER = '\U0001F0CF'

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck()
        for _ in range(2):
            card = Card(JOKER, JOKER)
            self._cards.append(card)
