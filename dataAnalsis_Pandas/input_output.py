'''
Data Input and Output¶
This notebook is the reference code for getting input and output, pandas can read a variety of
file types using its pd.read_ methods.
reading CSV

Excel
Pandas can read and write excel files,
keep in mind, this only imports data.
Not formulas or images, having images or macros may cause this read_excel
method to crash.

HTML¶
You may need to install htmllib5,lxml, and BeautifulSoup4. In your terminal/command prompt run:

conda install lxml
conda install html5lib
conda install BeautifulSoup4
Then restart Jupyter Notebook. (or use pip install if you aren't using the Anaconda Distribution)

Pandas can read table tabs off of html. For example:

HTML Input
Pandas read_html function will read tables off of a webpage and return a list of DataFrame objects:
'''
# install
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import html5lib
import lxml
from sqlalchemy import create_engine # for simple sql



df =pd.read_csv('example.csv')
#print(df)
'''
a   b   c   d
0   0   1   2   3
1   4   5   6   7
2   8   9  10  11
3  12  13  14  15
'''
df1 =pd.read_excel("example_s.xlsx",sheet_name='NewSheet')
#print(df1)
'''
   Unnamed: 0   a   b   c   d
0           0   0   1   2   3
1           1   4   5   6   7
2           2   8   9  10  11
3           3  12  13  14  15
'''
# to store it as an excel file form dataframe
df.to_excel('exampleSample.xlsx',sheet_name='NewSheet')
"""
HTML Input
Pandas read_html function will read tables off of a 
webpage and return a list of DataFrame objects:
"""
#df2 = pd.read_html("https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/")
#print(df2)

engine=create_engine('sqlite:///:memory:') # created a very small sqlite db to run on this
df.to_sql('my_table',engine)
sqldf=pd.read_sql('my_table',con=engine)
print(sqldf)
'''
   index   a   b   c   d
0      0   0   1   2   3
1      1   4   5   6   7
2      2   8   9  10  11
3      3  12  13  14  15
'''