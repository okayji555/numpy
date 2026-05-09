import numpy as np

arr = np.trunc([-3.1666, 3.6667])
arr1 = np.fix([-3.1666, 3.6667]) #same as truncate

arr2 = np.around(3.1666, 2)

ar = np.floor([-3.166, 3.667]) 
ar1 = np.ceil([-3.1666, 3.6667])

print(arr)
print(arr1)
print(arr2)
print(ar)
print(ar1)