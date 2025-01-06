from normalstringdict import NormalStringDict

nsd = NormalStringDict()

for key, value in ('a', 'b'), ('a', 1), (1, 'b'), (1, 1), ('c', 'd'):
    try:
        nsd[key] = value
    except TypeError as err:
        print(err)

print(nsd)
