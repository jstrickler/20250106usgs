from timeit import Timer
REPEATS = 1000

setup_code = """x = 1000000"""

code_snippets = [
    '''x += 1000000''',
    '''x = x + 1000000''']

for code_snippet in code_snippets:
    t = Timer(code_snippet, setup_code)
    print(f"{code_snippet:60.60s}{t.timeit(REPEATS)}")
    print('-' * 60)
