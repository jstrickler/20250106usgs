import numpy as np

a1 = np.arange(15)  # create 1D array
print("a1 shape", a1.shape)  # get shape
print()

print(a1)
print()

a1.shape = 3, 5  # reshape to 3x5
print(a1)
print()

a1.shape = 5, 3  # reshape to 5x3
print(a1)
print()

a1.shape = 3, -1  # reshape back to 3x5, let numpy calculate other dimension
print(a1)
print()

print(a1.flatten())  # print array as 1D (always returns a new array())
print()

print(a1.ravel()) # like .flatten(), but makes a *view* if possible (tries not to copy)
print()

print(a1.transpose())  # print transposed array
print("------------------")

a2 = np.arange(40)  # create 1D array
a2.shape = 2, 5, 4  # reshape to 2x5x4

print(a2)
print()
