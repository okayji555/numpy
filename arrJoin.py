import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))  #joins them in one line
twoarr = np.stack((arr1, arr2), axis = 1)  #stacking is done along a new axis
arrr = np.hstack((arr1, arr2))  #this stacks along rows
ar = np.vstack((arr1, arr2))   # this stack along coloumns

aar = np.dstack((arr1, arr2))  #it stack along height. which is the same as depth

arr3 = np.array([[1, 2], [3, 4]])

arr4 = np.array([[5, 6], [7, 8]])


onearr = np.concatenate((arr3, arr4), axis = 1)

print(arr)
print(twoarr)
print(arrr)
print(ar)
print(aar)
print(onearr)