'''
Pandas - DataFrame
'''
import pandas as pd
import numpy as np

from numpy.random import randn

np.random.seed(101)
df =pd.DataFrame(randn(5,4),['a','b','c','d','e'],['w','x','y','z'])
#print(df) # dataframe is a series of columns
'''
          w         x         y         z
a  2.706850  0.628133  0.907969  0.503826
b  0.651118 -0.319318 -0.848077  0.605965
c -2.018168  0.740122  0.528813 -0.589001
d  0.188695 -0.758872 -0.933237  0.955057
e  0.190794  1.978757  2.605967  0.683509

'''
w =df["w"]#returns the "w" column . youc an also use df.w. If you need multiple columns then you pass alist column
#names to get like wa =df["w","y"]
# #print(w)  if you pass in a value which is not in the dataframe then it will return "Keyerror"
'''
a    2.706850
b    0.651118
c   -2.018168
d    0.188695
e    0.190794
Name: w, dtype: float64
'''
#adding columns
df["new"]= df["w"]+df["y"] # it will add a new column with adding columns of w and y
#print(df)
'''
          w         x         y         z       new
a  2.706850  0.628133  0.907969  0.503826  3.614819
b  0.651118 -0.319318 -0.848077  0.605965 -0.196959
c -2.018168  0.740122  0.528813 -0.589001 -1.489355
d  0.188695 -0.758872 -0.933237  0.955057 -0.744542
e  0.190794  1.978757  2.605967  0.683509  2.796762
'''
# removing columns
#df.drop("new") # it will return valueerror as it has default axis value of 0 which is an index but you mentiones as column
#df.drop("naw",axis=1)# now it will drop the column. this will only happrn to see it not in the actual DF
#df.drop("naw",axis=1,inplace=True) # you need change inplace =True as its default value is false.
# lot of pandas method we have to specify this inplace value
#df.drop("a",axis=0) # will drop the index a even if you don't m,enton axis as 0 is the default value
#print(df.shape) # return (5,5) (axis=0,axis=1)
#print(df.loc['a']) # it will give as a series
'''
print(df.iloc[2])  numerical base index
w      2.706850
x      0.628133
y      0.907969
z      0.503826
new    3.614819
Name: a, dtype: float64
'''
#print(df.loc['b','y']) # rerurns particular cell value -0.8480769834036315
#print(df.loc[['a','b'],['w','y']]) # returns slice of the table
'''
          w         y
a  2.706850  0.907969
b  0.651118 -0.848077
'''
#TODO conditional selection and multy index part of the DATAFRAME

true =df>0 # will return true if the value is greater than zero False for less then zero
#print(true)
'''
       w      x      y      z    new
a   True   True   True   True   True
b   True  False  False   True  False
c  False   True   True  False  False
d   True  False  False   True  False
e   True   True   True   True   True

'''
#print(df[true]) # you can place NaN for less then zero value using like this
'''
          w         x         y         z       new
a  2.706850  0.628133  0.907969  0.503826  3.614819
b  0.651118       NaN       NaN  0.605965       NaN
c       NaN  0.740122  0.528813       NaN       NaN
d  0.188695       NaN       NaN  0.955057       NaN
e  0.190794  1.978757  2.605967  0.683509  2.796762
'''
# you can use condition to the column or index too
#print(df['w']>0)
'''
a     True
b     True
c    False
d     True
e     True
Name: w, dtype: bool
'''
#print(df[df['w']>0]) # this will just remove the value less than zero in the specifies column
'''
          w         x         y         z       new
a  2.706850  0.628133  0.907969  0.503826  3.614819
b  0.651118 -0.319318 -0.848077  0.605965 -0.196959
d  0.188695 -0.758872 -0.933237  0.955057 -0.744542
e  0.190794  1.978757  2.605967  0.683509  2.796762
'''
#print(df[(df['w']>0) & (df['y']>1)]) # & menas it is an and opeartor here you can use | for or
#           w         x         y         z       new
# e  0.190794  1.978757  2.605967  0.683509  2.796762
#print(df.reset_index()) # this will reset index as numeric value stsrting from 0
'''
  index         w         x         y         z       new
0     a  2.706850  0.628133  0.907969  0.503826  3.614819
1     b  0.651118 -0.319318 -0.848077  0.605965 -0.196959
2     c -2.018168  0.740122  0.528813 -0.589001 -1.489355
3     d  0.188695 -0.758872 -0.933237  0.955057 -0.744542
4     e  0.190794  1.978757  2.605967  0.683509  2.796762
'''
newind = 'CA NY WY OR CO'.split() # instead of using quoets around the char you can use this split method.
df['States']=newind
#print(df)

#TODO Multy index and index level hierarchy
outside =' g1 g1 g1 g2 g2 g2'.split()
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index =pd.MultiIndex.from_tuples(hier_index) # creates multy index in several levels
#print(hier_index)
'''
ultiIndex([('g1', 1),
            ('g1', 2),
            ('g1', 3),
            ('g2', 1),
            ('g2', 2),
            ('g2', 3)],
           )
'''
df1 =pd.DataFrame(randn(6,2),hier_index,['a','b'])
#print(df1)
'''
             a         b
g1 1  0.302665  1.693723
   2 -1.706086 -1.159119
   3 -0.134841  0.390528
g2 1  0.166905  0.184502
   2  0.807706  0.072960
   3  0.638787  0.329646
'''
# as you can see there is no cloumn names for the indices above
df1.index.names=['Groups','NUm']
#print(df1)
'''
                   a         b
Groups NUm                    
g1     1    0.302665  1.693723
       2   -1.706086 -1.159119
       3   -0.134841  0.390528
g2     1    0.166905  0.184502
       2    0.807706  0.072960
       3    0.638787  0.329646
'''
#print(df1.loc['g2'].loc[2]['b']) # returns the particlur cell value- 0.07295967531703869
# cross section
# if we need only on 'g1 then
#print(df1.xs("g1")) # xs - cross section  ---- df1.xs(1,level="num")
'''
            a         b
NUm                    
1    0.302665  1.693723
2   -1.706086 -1.159119
3   -0.134841  0.390528
'''