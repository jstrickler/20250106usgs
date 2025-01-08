import operator as op

def doit(func, value):
    return func(value)

def triple(x):
    return 3 * x

print(f"{doit(triple, 9) = }")

def spam(m):
    return m * 100

print(f"{doit(spam, '-') = }")

print(f"{doit(lambda a: 10 * a, 50) = }")

nums = [800, 80, "abc", 1000, 32, -3, 8, "wombat", 18, 255, 400, "penguin", 5, 5000]

print(f"{max(nums, key=lambda x:str(x)[:2]) = }")
print(f"{min(nums, key=lambda x:str(x)[:2]) = }")

#  lambda : value
#  lambda x: value
#  lambda x, y: value
# ...

def math_op(func, x, y):
    return func(x, y)

def add(a, b):
    return a + b

print(f"{math_op(add, 5, 8) = }")
print(f"{math_op(op.add, 5, 8) = }")

#  + - * / % ^ ** += ...

print(f"{op.mul(5, 85) = }")
