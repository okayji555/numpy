import numpy as np

arr = np.arange(1, 10)

print(np.log2(arr))
print(np.log(arr))

from  math import log

np.log = np.frompyfunc(log, 2, 1)
print(np.log(100,15))