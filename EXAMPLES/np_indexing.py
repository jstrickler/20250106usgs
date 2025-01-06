import numpy as np

a = np.array(
    [[70, 31, 21, 76, 19, 5, 54, 66],
     [23, 29, 71, 12, 27, 74, 65, 73],
     [11, 84, 7, 10, 31, 50, 11, 98],
     [25, 13, 43, 1, 31, 52, 41, 90],
     [75, 37, 11, 62, 35, 76, 38, 4]]
)  # sample data

print("a:")
print(a)
print()

print('a[0] =>', a[0])  # first row
print('a[0][0] =>', a[0][0])  # first element of first row
print('a[0,0] =>', a[0,0])  # same, but numpy style
print('a[0,:3] =>', a[0,:3])  # first 3 elements of first row
print()

print('a[:,:2] =>\n', a[:,:2])  # first 2 columns
print()

print('a[:3,0] =>', a[:3,0])  # first column of first 3 rows
print()

print('a[:3, :3] =>\n', a[:3,:3])  # first 3 rows, first 3 columns
print()

print('a[::2] =>\n', a[::2])  # every second row
print()
