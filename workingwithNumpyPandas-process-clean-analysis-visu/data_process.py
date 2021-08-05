import numpy as np
import pandas as pd
#from pip import openpyxl
file_path ='Data/csv_data.csv'
data = pd.read_csv(file_path)
print(data)
''' inside the file we have this table that is a Pandas's DataFrame
    id             name  price  sales      brand
0  101         biscuits   5.00    227  HomeFoods
1  102          cookies   7.25    158    TBakery
2  103             cake  12.00     50    TBakery
3  104  whey_supplement  34.90     24    MusleUp
4  105     protein_bars   4.90     85    MusleUp
5  106     potato_chips   1.75    121  HomeFoods
'''
print(type(data))#<class 'pandas.core.frame.DataFrame'>
print(data["name"])
''' returns the name column elements as a list with index. it is a Pandas's Series type
0           biscuits
1            cookies
2               cake
3    whey_supplement
4       protein_bars
5       potato_chips
'''
file_path1 ='Data/json_data.json'
j_data = pd.read_json(file_path1)
#print(j_data)
''' returns the same DataFrame 
id             name  price  sales      brand
0  101         biscuits   5.00    227  HomeFoods
1  102          cookies   7.25    158    TBakery
2  103             cake  12.00     50    TBakery
3  104  whey_supplement  34.90     24    MusleUp
4  105     protein_bars   4.90     85    MusleUp
5  106     potato_chips   1.75    121  HomeFoods
'''
#print(j_data["id"])
''' returns pandas's Series 
0    101
1    102
2    103
3    104
4    105
5    106
'''
file_path2 ='Data/xlsx_data.xlsx'
e_data = pd.read_excel(file_path2)
print(e_data)
''' returns same Dataframe object
 id             name  price  sales      brand
0  101         biscuits   5.00    227  HomeFoods
1  102          cookies   7.25    158    TBakery
2  103             cake  12.00     50    TBakery
3  104  whey_supplement  34.90     24    MusleUp
4  105     protein_bars   4.90     85    MusleUp
5  106     potato_chips   1.75    121  HomeFoods
'''
print(e_data["price"])
''' returns same Series object from Pandas
0     5.00
1     7.25
2    12.00
3    34.90
4     4.90
5     1.75
'''