from timeit import Timer

REPEATS = 1000

setup = """
import numpy as np
SIZE = 10000
"""

code_snippets = [
    '''my_list = [i for i in range(SIZE)]''',
    '''my_list = list(i for i in range(SIZE))''',
    '''my_list = [*range(SIZE)]''',
    '''my_list = list(range(SIZE))''',
    '''my_list = np.array(range(SIZE))''',
    '''my_list = np.arange(SIZE)''',
]

for code_snippet in code_snippets:
    t = Timer(code_snippet, setup)
    print(f"{code_snippet:60.60s}{t.timeit(REPEATS)}")
    print('-' * 60)


