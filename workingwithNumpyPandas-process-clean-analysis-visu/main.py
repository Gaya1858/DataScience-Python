import numpy as np
import pandas as pd

arr =np.array([[1,2,3,4],[6,7,8,9],[1,2,3,4]],dtype =int)# it can take only homogeneous objects. ndmin can create 2d,or 3d
#dtype can be float, str too
print(arr)
'''[[1 2 3 4]
    [6 7 8 9]
    [1 2 3 4]]
'''
arr5 =arr+5# will add 5 to the whole arr lists. you can multiply with scalar(+,-,*,/)
print(arr5)
# [ [ 6  7  8  9]
#   [11 12 13 14]
#   [ 6  7  8  9]]
print(arr5[0]) # [6 7 8 9]
print(arr5[0][0]) # 6

# Pandas series you can get a list with default index starting from 0 , you can also specify
# index values
ar1 = pd.Series([1,3,5,6,7])
print(ar1)
'''
0    1
1    3
2    5
3    6
4    7
dtype: int64
'''
ar = pd.Series([1,3,5,6,7],index=['a','b','c','d','e'],dtype = int)
print(ar)
'''
a    1
b    3
c    5
d    6
e    7
dtype: int64
'''
# we can make a series to numpy array
ar3 = np.array([1,2,3,4,5,6])
ar4 = pd.Series(data=ar3,index =[100,101,102,103,104,105])
print(ar4)
print(ar4[100]) #passing index value can get the value to that index