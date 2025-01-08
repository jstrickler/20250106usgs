from functools import reduce, partial
import operator
from dataclasses import dataclass, field

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f1 = map(str.upper, fruits)
print(f"{f1 = }\n")
for fruit in f1:
    print(fruit)
print('-' * 60)

f2 = [f.upper() for f in fruits]
print(f"{f2 = }\n")

# reduce(func, iterable)

nums = [800, 80, 1000, 32, -3, 8, 18, 255, 400, 5, 5000]

total = reduce(operator.add, nums)
print(f"{total = }")

words = ['Wankel', "rotary", "engine"]
result = reduce(operator.add, words, "")
print(f"{result = }")

product = reduce(operator.mul, nums)
print(f"{product = }\n")


person_field = partial(field, init=False)

@dataclass
class Person:
    first_name: str
    last_name: str
    zip_code: str = person_field()  # field(init=False)
    city: str = person_field()

p1 = Person("Fred", "Mertz")
p1.zip_code = "12345"
p1.city = "New York"
print(f"{p1 = }\n")
