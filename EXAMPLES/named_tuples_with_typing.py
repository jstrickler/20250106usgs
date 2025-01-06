from typing import NamedTuple
from pprint import pprint

# collections.namedtuple typing.NamedTuple
# dataclasses.dataclass
# pydantic (d/l + install) -- validation
# attrs (d/l + install)
 
Person = NamedTuple("Person", [('first_name', str), ('last_name', str), 
                               ('age', int)])

p1 = Person("Jill", "Ortilla", 55)
print(f"{p1 = }")
print(f"{p1.age = }")

p2 = Person("Guido", "van Rossum", "88")
print(f"{p2 = }")
print(f"{p2.age = }")

# alternate
class Human(NamedTuple):
    first_name: str
    last_name: str
    age: int = 0

p3 = Human("Frank", "Capra", 88)
print(f"{p3 = }")
print(f"{p3.age = }")

p4 = Human("Frank", "Capra", [1, 2, 3])
print(f"{p4 = }")
print(f"{p4.age = }")

p5 = Human("Willy", "Wonka")
print(f"{p5 = }")
print(f"{p5.age = }")
    