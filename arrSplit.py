import numpy as np

arr = np.array([1 ,2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)
newarr1 = np.array_split(arr, 4)  # this splits the array and adjust from the end accordingly

print(newarr)
print(newarr1)


print(newarr[0])    # prints the first split array
print(newarr[1])    # prints the second split array
print(newarr[2])    # prints the third Split array



arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newar = np.array_split(arr1, 3)
ar = np.array_split(arr1, 3, axis = 1)  #splits along the coloumn, axis as 1
arr = np.hsplit(arr1, 3)  #spits horizontally

print(newar)
print(ar)

