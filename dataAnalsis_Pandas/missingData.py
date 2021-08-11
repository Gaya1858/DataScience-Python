'''
deal with missing data in pandas and group by value

TODO df.dropna(axis=1) # this will remove the column which has null value, if you don't mention the axis
# then this drop the all the rows which have nan value

# you can also give different values like mean value of each column should go into the NaN cell
TODO df.fillna(value=df.mean())

GROUPBY
allows you to group togetehr rows based of a column and perform an aggregate function on them
Aggregate function: a function that take many input values and gives one output value

'''
import pandas as pd
import numpy as np

d ={'a':[1,2,np.nan],'b':[5,np.nan,np.nan],'c':[1,2,3]} # np.nan will create a NaN value
df =pd.DataFrame(d)
#print(df)
'''
     a    b  c
0  1.0  5.0  1
1  2.0  NaN  2
2  NaN  NaN  3
'''
# dropping missing values
df.dropna(axis=1) # this will remove the column which has null value, if you don't mention the axis
# then this drop the all the rows which have nan value
print(df.dropna())
'''
     a    b  c
0  1.0  5.0  1
'''
# fill in those missing values
print(df.fillna(value= 'FILL VALUE')) # this will fill with the value which is within the quoets
'''
            a           b  c
0         1.0         5.0  1
1         2.0  FILL VALUE  2
2  FILL VALUE  FILL VALUE  3
'''
# you can also give different values like mean value of each column should go into the NaN cell
print(df.fillna(value=df.mean()))
'''
     a    b  c
0  1.0  5.0  1
1  2.0  5.0  2
2  1.5  5.0  3
you can also just change with single column at a time too
'''

# Group by (aggregate function
data ={"Company" :["GOOG", "GOOG", "MSFT" ,"MSFT", "FB" ,"FB"],
       "Person": ['Sam',"Charlie",'Amy',"Vanesa","Carl","Sarah"],
       "Sales": [200,120,340,124,243,350]}
df =pd.DataFrame(data)
print(df)
'''
  Company   Person  Sales
0    GOOG      Sam    200
1    GOOG  Charlie    120
2    MSFT      Amy    340
3    MSFT   Vanesa    124
4      FB     Carl    243
5      FB    Sarah    350
'''
#print(df.groupby('Company'))  #  this will return an object of
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7ff0701b1850>
byComp =df.groupby('Company')
#print(byComp.mean()) # pandas will ignore non numeric values. you can do all analytic methods like median,sum and more
'''
Company       
FB       296.5
GOOG     160.0
MSFT     232.0
'''
print(byComp.sum().loc['FB']) # Sales    593 return total sales value
print(byComp.count())
'''
         Person  Sales
Company               
FB            2      2
GOOG          2      2
MSFT          2      2
'''
# you can also to min value max value

print(byComp.describe())
'''
        Sales                                                        
        count   mean         std    min     25%    50%     75%    max
Company                                                              
FB        2.0  296.5   75.660426  243.0  269.75  296.5  323.25  350.0
GOOG      2.0  160.0   56.568542  120.0  140.00  160.0  180.00  200.0
MSFT      2.0  232.0  152.735065  124.0  178.00  232.0  286.00  340.0
'''
print(byComp.describe().transpose())
'''
Company              FB        GOOG        MSFT
Sales count    2.000000    2.000000    2.000000
      mean   296.500000  160.000000  232.000000
      std     75.660426   56.568542  152.735065
      min    243.000000  120.000000  124.000000
      25%    269.750000  140.000000  178.000000
      50%    296.500000  160.000000  232.000000
      75%    323.250000  180.000000  286.000000
      max    350.000000  200.000000  340.000000
'''