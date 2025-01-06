from timeit import Timer

REPEATS = 100

setup_code = """
SIZE = 1_000_000
import numpy as np
my_list = list(range(SIZE))
my_ndarray = np.arange(SIZE)
"""

code_snippets = [
    """
for i in range(SIZE):
    my_list[i] *= 10
    """,

    """
my_ndarray *= 10
    """,
]

for code_snippet in code_snippets:
    t = Timer(code_snippet, setup_code)
    print(f"{code_snippet:60.60s}{t.timeit(REPEATS)}")
    print('-' * 60)
