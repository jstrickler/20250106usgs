from functools import cache
from random import randint
from geometry import circle_area

circle_area = cache(circle_area)
for _ in range(10000):  # call circle_area() 10000 times
    result = circle_area(randint(1, 50))   # call with argument in range 1-50

print(circle_area.cache_info())  # show cache hits and misses

