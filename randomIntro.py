from numpy import random

x = random.randint(100)
x1 = random.randint(100, size = (5))
x2 = random.rand()
x3 = random.rand(5) #Generate a 1-D array containing 5 random floats
x4 = random.rand(3, 5)

y = random.choice([3, 5, 7, 9])
y1 = random.choice([3, 5, 7, 9], size = (3, 5))


print(x)
print(x1)
print(x2)
print(x3)
print(x4)
