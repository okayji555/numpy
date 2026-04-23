import numpy as np

arr = np.array([1 ,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

arr1 = arr.reshape(4,3)
arr2 = arr.reshape(2, 3, 2)

print(arr1)
print(arr2)

ar = np.array([1 ,2, 3, 4, 5, 6, 7, 8])

newar = ar.reshape(2, 2, -1)    # This -1 means that no need to specify an exact number, numpy will calculate it for us
# note: we cannot use -1 in more than one dimension

print(newar)


arrr = np.array([[1, 2, 3], [4, 5, 6]])

newarrr = arrr.reshape(-1)      #this flattens the array to 1D

print(newarrr)