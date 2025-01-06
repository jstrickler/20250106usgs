import sys
from functools import reduce
from itertools import chain

print(reduce(lambda a, b: a + 1, chain.from_iterable(map(open, sys.argv[1:])), 0))

