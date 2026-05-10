import numpy as np

#Product
arr = np.array([1, 2, 3, 4])
arr1 = np.array([5, 6, 7, 8])

x = np.prod(arr)
x1 = np.prod([arr, arr1])
x2 = np.prod([arr, arr1], axis=1)

print(x)
print(x1)
print(x2)


#Cummulative Product
newar = np.cumprod(arr1)

print(newar)