import pandas as pd

data = [
    [1, 2, 3],
    [4, 5, 6],
    [8, 5, 9],
]

df = pd.DataFrame(data, columns='a b c'.split(), index="alpha beta gamma".split())

print(f"df:\n {df}")

print('-' * 60)

index = df == 5
print(f"index:\n {index}")

print(f"df[df == 5]:\n {df[df == 5]}")

