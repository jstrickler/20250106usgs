import numpy as np

a = np.linspace(100, 200,num=500)

a.shape = (5,10,10)

a *= .5

print(a)
