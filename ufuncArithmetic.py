import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1, arr2)
newarr1 = np.subtract(arr1, arr2)
newarr2 = np.multiply(arr1, arr2)

print(newarr)
print(newarr1)
print(newarr2)


arr3 = np.array([10, 12, 18, 25])
arr4 = np.array([2, 3, 9, 5])

newar = np.power(arr3, arr4)        #rises the values from the first array to the power of the values of the second array
newar1 = np.divide(arr3, arr4)

newar2 = np.mod(arr3, arr4)
newar3 = np.remainder(arr3, arr4)  #same as mod

newar4 = np.divmod(arr3, arr4)  #returns both quotient and the mod


print(newar)
print(newar1)
print(newar2)
print(newar3)
print(newar4)
