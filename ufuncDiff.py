import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)
newar = np.diff(arr, n=2) #n gives parameter

print(newarr)
print(newar)