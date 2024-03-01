import numpy as np

cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]
arr = np.array(cvalues)
print(arr)
print(type(arr))

fvalues = [x*9/5 + 32 for x in cvalues]
print(fvalues)