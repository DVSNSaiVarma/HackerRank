import numpy as np
arr = input().strip().split(' ')
arr = np.array(arr, int)
arr = np.reshape(arr, (3, 3))
print(arr)

