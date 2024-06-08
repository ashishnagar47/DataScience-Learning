import numpy as np

arr1=np.array([[1,2],[3,4]])
arr2=np.array([[6,7],[8,9]])

for var in arr1:
    for val in arr2:
        print(var+val)