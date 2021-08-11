'''
Operations
There are lots of operations with pandas that will be really useful to you,
but don't fall into any distinct category.
df.head()
'''
import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df.head()) # will return first 5 rows of data
'''
   col1  col2 col3
0     1   444  abc
1     2   555  def
2     3   666  ghi
3     4   444  xyz
'''
print(df['col2'].unique()) # return [444 555 666] no duplicate values
print(df['col2'].nunique()) # return 3 number of unique values
print(df['col2'].value_counts()) # returns count of values
'''
444    2
555    1
666    1
Name: col2, dtype: int64
'''
# you can apply the functions builtin or custom insdie the dataframe using apply method
def times2(x):
    return x*2
print(df['col1'].apply(times2))
# df['col1'].apply(lambda x:x*2) = df['col1'].apply(times2)
'''
0    2
1    4
2    6
3    8
Name: col1, dtype: int64
'''
#removing columns
print(df.drop('col1',axis=1))
'''
   col2 col3
0   444  abc
1   555  def
2   666  ghi
3   444  xyz
'''
print(df.columns) #return Index(['col1', 'col2', 'col3'], dtype='object')
print(df.index) #return RangeIndex(start=0, stop=4, step=1)
print(df.sort_values('col2')) # see the index didn't change just it is sorted by col2
'''
   col1  col2 col3
0     1   444  abc
3     4   444  xyz
1     2   555  def
2     3   666  ghi
'''
print(df.isnull()) # there is no null value in the table. so it will return false for all the values

#Select from DataFrame using criteria from multiple columns
newdf = df[(df['col1']>2) & (df['col2']==444)]
print(newdf)
'''
   col1  col2 col3
3     4   444  xyz
'''
data = {'A':['foo','foo','foo','bar','bar','bar'],
        'B':['one','one','two','two','one','one'],
        'C':['x','y','x','y','x','y'],
        'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)
print(df)
'''
     A    B  C  D
0  foo  one  x  1
1  foo  one  y  3
2  foo  two  x  2
3  bar  two  y  5
4  bar  one  x  4
5  bar  one  y  1
'''
print("------")
print(df.pivot_table(values='D',index=['A',"B"],columns =['C']))
'''
C          x    y
A   B            
bar one  4.0  1.0
    two  NaN  5.0
foo one  1.0  3.0
    two  2.0  NaN
'''