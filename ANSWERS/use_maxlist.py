from maxlist import MaxList

m = MaxList(3)

for letter in 'abcdef':
    try:
        m.append(letter)
    except IndexError as err:
        print(err)

    print(f"{m = }")

try:
    m.insert(1, 'x')
except IndexError as err:
    print(err)
    print(f"{m = }")


print(f"{type(m) = }")
print(f"{isinstance(m, list) = }")

x = m[::]
print(f"{x = }")
print(f"{type(x) = }")
a = m.pop()
print(f"{a = }")
try:
    m.extend("qrs")
except IndexError as err:
    print(err)
print(f"{m = }")


