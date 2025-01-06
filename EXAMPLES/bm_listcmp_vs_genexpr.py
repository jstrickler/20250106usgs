from timeit import Timer

REPEATS = 100

setup = '''
import random
nums = [random.randint(1,100) for _ in range(100000)]
'''


code_snippets = [
    '''
' '.join([str(n) for n in nums])
    ''',
    '''
' '.join(str(n) for n in nums)
    ''',
]

for code_snippet in code_snippets:
    t = Timer(code_snippet, setup)
    print(f"{code_snippet:60.60s}{t.timeit(REPEATS)}")
    print('-' * 60)

