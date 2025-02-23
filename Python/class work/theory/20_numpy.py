import numpy as np

arr = np.array([1,2,3])
print("Array:",arr)

arr1 = np.array([[1,2,3],[3,2,1]])
print("Dimension:",arr1.ndim)
print("Shape:",arr1.shape)

arr2 = np.array([[[1,2,3],[3,2,1]],[[4,5,6],[6,5,4]]])
print("Dimension:",arr2.ndim)
print("Shape:",arr2.shape)

arr3 = np.array([[1,2,3,4],[5,6,7,8]])
print("Shape:",arr3.shape)