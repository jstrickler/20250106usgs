from carddeck import CardDeck

deck = CardDeck("Mary")

deck.shuffle()

for _ in range(30):
    card = deck.draw()
    print(card)
print()

print(deck)

print(deck.cards)


