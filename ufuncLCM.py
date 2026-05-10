import numpy as np

num1 = 4
num2 = 6

arr = np.array([3, 6, 9])

arr1 = np.arange(1,11)

lcm = np.lcm(num1, num2)
x = np.lcm.reduce(arr)
# reduce takes the function and collapses it into a single value
y = np.lcm.reduce(arr1)

print(lcm)
print(x)
print(y)