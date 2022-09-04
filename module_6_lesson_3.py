import numpy
print("import successful")

import numpy as np 
print("import2 successful")

list = np.arange(1, 100)
print(list)

array = np.arange(2,101,2)
print(array)

arr = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100])
x = np.lcm.reduce(arr)  
print(x)