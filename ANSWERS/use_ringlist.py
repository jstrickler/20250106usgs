from ringlist import RingList

r = RingList(3)

for letter in 'abcdef':
    r.append(letter)
    print(f"{r = }")
