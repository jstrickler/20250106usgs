from timeit import Timer

REPEATS = 10000

setup = """
values = []
"""  # setup code is only executed once

code_snippets = [
'''
for i in range(10000):
    values.append(i)
values.clear()
''',  # code fragment executed many times
'''
i = 0
while i < 10000:
    values.append(i)
    i += 1
values.clear()
''',  # code fragment executed many times
]

for code_snippet in code_snippets:
    t = Timer(code_snippet, setup)
    print(f"{code_snippet:80.80s}{t.timeit(REPEATS)}")
    print('-' * 60)

