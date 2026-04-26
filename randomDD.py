#data distribution
from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
"""
here the p is the probablity of each of the numbers
probablity of 3 is 0.1
probablity of 5 is 0.3
probablity of 7 is 0.6
probablity of 9 is 0.0

and generates 1-D array containing 100 values
"""

x1 = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(x)
print(x1)