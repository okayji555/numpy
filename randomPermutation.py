from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)     #changes the original array

print(arr)

arr1 = np.array([1, 2, 3, 4, 5])

print(random.permutation(arr))      # returns a rearranged array(and leaves the original array unchanged)