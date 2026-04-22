import numpy as np

a = np.array(55)
b = np.array([1,2,3])
c = np.array([[1,2,3], [4,5,6]])
d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)



arr = np.array([1,2,3,4], ndmin = 5)

print(arr)
print("No. of dimension: ", arr.ndim)