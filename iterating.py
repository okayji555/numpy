import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

for x in arr:
  for y in x:
    print(y)



arr1 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.aditer(arr1):
  print(x)

for x in np.nditer(arr1, flags=['buffered'], op_dtypes=['S']):
  print(x)

for x in np.nditer(arr1[:, ::2]):
  print(x)


arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr2):
  print(idx, x)