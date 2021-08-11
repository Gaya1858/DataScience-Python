'''
Pandas Series :  It is something like Numpy arrary. But you index by label

'''
import pandas as pd
import numpy as np

label = ['a','b','c','d']
my_data =[12,13,14,10]
arr = np.array(my_data)
di ={'a':12,'b':13,'c':14,'d':10}

seri = pd.Series(data=my_data) # data is for data and will create index itself starting from 0
#print(seri)
'''
0    12
1    13
2    14
3    10
dtype: int64
'''
serie = pd.Series(index=label,data=my_data) # in this case index will be givcen as a list
#print(serie)
'''
a    12
b    13
c    14
d    10
dtype: int64
'''
seris = pd.Series(di) # it takes dictionary and returns keys as index and values as data
#print(seris)
'''
a    12
b    13
c    14
d    10
dtype: int64
'''
ser1 =pd.Series([1,2,3,4],["Germany","USA","Japan","Russia"]) # if you don't pass the values with arguments
#then the first parameter is for the "data" and second one is for "index"
ser2 =pd.Series([1,2,3,5],["Germany","USA","Japan","Italy"])
#print(ser1)
'''
Germany    1
USA        2
Japan      3
Russia     4 '''
# you can access the value by using the data like dictionary
x =ser1["USA"] # x will return 2 as value
ser3 =ser1+ser2 # it will check both series and it has some common countries and its value, so it will add the value and
#store it that particular country and if there is no common thing it will put the value as NaN(not a number"
#print(ser3)
'''
Germany    2.0
Italy      NaN
Japan      6.0
Russia     NaN
USA        4.0
dtype: float64
'''
