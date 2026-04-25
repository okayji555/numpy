import numpy as np

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]

newarr = arr[x]

print(newarr)




arr1 = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = []   # Create an empty list


for element in arr1:
  
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr1 = arr1[filter_arr]

print(filter_arr)
print(newarr1)




#NOW DIRECT APPROACH

arr2 = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr1 = arr % 2 == 0

newarr2 = arr2[filter_arr1]

print(filter_arr1)
print(newarr2)