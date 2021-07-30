'''
Pandas is the key model for datascience
this file is not working as some issue in my computer
please refer to jupyter notebook
'''
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

data=pd.read_csv("cost-revenue-data.csv") # creates dataframe
print(data.describe()) # this will give below in scientific notation
'''production_budget_usd  worldwide_gross_usd
count           5.034000e+03         5.034000e+03
mean            3.290784e+07         9.515685e+07
std             4.112589e+07         1.726012e+08
min             1.100000e+03         2.600000e+01
25%             6.000000e+06         7.000000e+06
50%             1.900000e+07         3.296202e+07
75%             4.200000e+07         1.034471e+08
max             4.250000e+08         2.783919e+09'''

data=pd.read_csv("cost-revenue-data.csv") # creates dataframe
x = DataFrame(data,columns=["production_budget_usd"])
y = DataFrame(data,columns=["worldwide_gross_usd"])

# matplotlib --- scatter plot

plt.scatter(x,y)
plt.show()