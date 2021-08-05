import pandas as pd

dt =pd.read_csv("Data/csv_data.csv",
                names= ["ID","NAME","PRICE","SALES","BRAND"], # you can change the names of the columns using names param
                skiprows=1) # this will skip the row from beginning. in this case we aare removing the heading row
print(dt)
dt.isnull() # it will return True when null value exist(NaN) rest false
 # fills Nan value to 0 but
#print(dt.fillna(0))# but it won't change inside the dt table. you have to specify inplace =True to change inside the table

print(dt.pad()) # this will put the value above the NaN value column
# if you want to put the below value then do dt.bfill()

dt.dropna(inplace=True)# you want to delete the NaN rows
print(dt)
#dt.drop([4,6]) # this will delete the 4th and 6th rows
# if you want delete column
del dt["PRICE"]
print(dt) # price is removed
#instead of del you can use drop(column =["PRICE"]) and you can store this in diffent object
