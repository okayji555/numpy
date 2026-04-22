import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5]) # print element 1 to 5
print(arr[4:])  # print element from 4 to end
print(arr[:4])  # print element start to 4
print(arr[-3:-1])  #print element from behind(end of the array)
print(arr[1:5:2]) #Return every other element from index 1 to index 5
print(arr[::2])  # returning every other element from the entire array


#for 2D array

arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr1[1,1:4]) #prints the 2nd dim array and in that element from 1 to 4
print(arr1[0:2, 2]) #from both the elements and return the index 2
print(arr[0:2, 1:4])   #From both elements, slice index 1 to index 4 (not included), this will return a 2-D array