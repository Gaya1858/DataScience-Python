import pandas as pd

dt =pd.read_csv("Data/csv_data.csv",
                names= ["ID","NAME","PRICE","SALES","BRAND"], # you can change the names of the columns using names param
                skiprows=1) # this will skip the row from beginning. in this case we aare removing the heading row
print(dt)

print(sum(dt['SALES'])) # return total sales of 665
print(min(dt['SALES']))# return minimum sales of 24

print(max(dt['SALES']))# return maximum sales of 227 --- you can also mention dt['SALES'].max()
# central tendency includes
# average,  or mean
#  mode and
# median
print(round(dt['SALES'].mean(),2)) #110.83
print(dt['SALES'].median()) # 103.0
print(dt['SALES'].mode()) # inthis case all the sales value comes only once no repeat values so it will give everything b
# in return
print(max(dt['SALES'])-min(dt['SALES'])) # this will give the difference of the sales value which is a Range --203
analytics =pd.DataFrame({'Total Sales': dt["SALES"].sum(),'Average Sales':round(dt["SALES"].mean(),2),
                         'Maximum Sales':dt["SALES"].max()},index=[1])
print(analytics)
'''
   Total Sales  Average Sales  Maximum Sales
1          665     110.833333            227
'''
print(round(dt.describe(),2)) # describe method will give you all the analytics of the data(numerical)
'''
           ID  PRICE   SALES
count    6.00   6.00    6.00
mean   103.50  10.97  110.83
std      1.87  12.21   74.47
min    101.00   1.75   24.00
25%    102.25   4.93   58.75
50%    103.50   6.12  103.00
75%    104.75  10.81  148.75
max    106.00  34.90  227.00
'''