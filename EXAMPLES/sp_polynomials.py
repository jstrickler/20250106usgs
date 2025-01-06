import scipy as sp

p1 = sp.poly1d([2, 1, 4])  # 2,1,4 are coefficients
print(p1, '\n')

print(p1(.75), '\n')  # evaluate for x = .75

print(p1.r, '\n')  # get the roots

p2 = sp.poly1d([2, 1, -4], True)  # 2,1,-4 are roots
print(p2, '\n')

print(p2(.75))  # evaluate for x = .75
print(p2.r), '\n'  # get the roots

p3 = sp.poly1d([1, 2, 3], False, 'm')  # 1,2,3 are coefficients, variable is 'm'
print(p3, '\n')

print(p3(100), '\n')  # evaluate for m = 100

print(p3.r, '\n')  # get the roots

p4 = sp.poly1d([1, 2])  # polynomial arithmetic
p5 = sp.poly1d([3, 4], '\n')

print(p4, '\n')

print(p5, '\n')

print(p4 + p5, '\n')

print(p4 - p5, '\n')

print(p4 ** 3, '\n')
