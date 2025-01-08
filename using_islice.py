from itertools import chain, islice

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

fruit_gen = (f.upper() for f in fruits)

print(f"{islice(fruit_gen, 0, 5) = }")

fruit_gen = (f.upper() for f in fruits)

print(f"{list(islice(fruit_gen, 0, 5)) = }")

a = [1, 2, 3]
b = 4, 5, 6
c = ["a", "b", "c"]
fruit_gen = (f.upper() for f in fruits)

for item in chain(a, b, c, fruit_gen):
    print(item)
print()
