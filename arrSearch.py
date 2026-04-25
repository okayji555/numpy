import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
arr1 = np.array([10, 14, 93, 41, 8, 7])


x = np.where(arr == 4)
y = np.searchsorted(arr, 5)
y1 = np.searchsorted(arr, 3, side = "right")

x2 = np.where(arr1%2 == 0)
x3 = np.where(arr1%2 == 1)

print(x)
print(y)
print(y1)
print(x2)
print(x3)