import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
arr[0] = 7


print(arr)
print(x.base) #prints none
print(y.base)
print(x)