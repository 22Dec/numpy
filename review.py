import numpy as np
array = np.array([[1,2,3],[2,3,4]])  #列表转化为矩阵
print(array)
a=np.array([1,2 ,6],dtype=np.float32)
print(a.shape)

print('\n\n\n')
b=np.arange(0,12,2).reshape((3,2))
print(b)

print('\n\n\n')
c=np.dot(array,b)
print(c)