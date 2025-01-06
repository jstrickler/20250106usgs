# sum the squares of a list of numbers
# using list comprehension, entire list is stored in memory
s1 = sum([x * x for x in range(10)])  # using list comprehension, entire list is stored in memory

# only one square is in memory at a time with generator expression
s2 = sum(x * x for x in range(10))  # with generator expression, only one square is in memory at a time
print(s1, s2)
print()

