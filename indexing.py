import numpy as np

arr = np.array([1,2,3,4])

print(arr[0])
print(arr[3])
print(arr[0] + arr[2]) # this adds the element

#this is to access 2D array
arr1 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print("2nd element on the 1st row: ", arr1[0,1])
print("5th element on the 2nd row: ", arr[1,4])


#this is to access 3D array
arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr2[0,1,2])


#this is negative indexing
arr3 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print("Last element from 2nd dimension:", arr[1,-1])