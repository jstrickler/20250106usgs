from collections import deque

d = deque()  # Create an empty deque
for c in 'abcdef':
    d.append(c)   # Append to the deque
print(f"{d = }")

for c in 'ghijkl':
    d.appendleft(c)  # Prepend to the deque
print(f"{d = }")

d.extend('mno')  # Extend the deque at the end one letter at a time
print(f"{d = }")

d.extendleft('pqr')  # Extend the deque at the beginning one letter at a time
print(f"{d = }")

print(d[9])
print(f"{d[9] = }")
print(f"{d.pop() = }")
print(f"{d.popleft() = }")

print(f"{d = }")
