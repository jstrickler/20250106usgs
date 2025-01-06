from timeit import Timer

REPEATS = 1000

setup_code = """
import re
alice_text = open('../DATA/alice.txt').read()
alice_bytes = alice_text.encode()
"""

code_snippets = [
    '''count = alice_text.count('a') + alice_text.count('A')''',
    '''count = alice_text.lower().count('a')''',
    '''count = len(re.findall(r'[aA]', alice_text))''',
    '''count = len(re.findall('a', alice_text, re.I))''',
    '''count = alice_bytes.count(65) + alice_bytes.count(97)''',
]

for code_snippet in code_snippets:
    t = Timer(code_snippet, setup_code)
    print(f"{code_snippet:60.60s}{t.timeit(REPEATS)}")
    print('-' * 60)

