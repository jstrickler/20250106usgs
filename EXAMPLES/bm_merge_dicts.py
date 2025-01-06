from timeit import Timer

REPEATS = 1_000_000

setup = """
d1 = {'a': 5, 'b': 10, 'c': 15}
d2 = {'a': 'wombat', 'b': 'wallaby', 'c': 'koala'}
"""

code_snippets = [
    '''{ x: (d1[x], d2[x]) for x in d1}''',
    '''{ x: (y, d2[x]) for x, y in d1.items()}''',
    '''dict(zip(d1.keys(),zip(d1.values(), d2.values())))''',
]

for code_snippet in code_snippets:
    t = Timer(code_snippet, setup)
    print(f"{code_snippet:60.60s}{t.timeit(REPEATS)}")
    print('-' * 60)

