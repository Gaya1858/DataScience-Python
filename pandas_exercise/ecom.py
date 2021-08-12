import pandas as pd

df = pd.read_csv("EcommercePurchases")
df.head() #Check the head of the DataFrame.

#TODO ** How many rows and columns are there? **
df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10000 entries, 0 to 9999
Data columns (total 14 columns):
 #   Column            Non-Null Count  Dtype  
---  ------            --------------  -----  
 0   Address           10000 non-null  object 
 1   Lot               10000 non-null  object 
 2   AM or PM          10000 non-null  object 
 3   Browser Info      10000 non-null  object 
 4   Company           10000 non-null  object 
 5   Credit Card       10000 non-null  int64  
 6   CC Exp Date       10000 non-null  object 
 7   CC Security Code  10000 non-null  int64  
 8   CC Provider       10000 non-null  object 
 9   Email             10000 non-null  object 
 10  Job               10000 non-null  object 
 11  IP Address        10000 non-null  object 
 12  Language          10000 non-null  object 
 13  Purchase Price    10000 non-null  float64
dtypes: float64(1), int64(2), object(11)
memory usage: 1.1+ MB

'''

#TODO ** What is the average Purchase Price? **
df["Purchase Price"].mean() #50.34730200000025

#TODO ** What were the highest and lowest purchase prices? **
df["Purchase Price"].min() #0.0
df["Purchase Price"].max() #99.99

#TODO * How many people have English 'en' as their Language
# of choice on the website? **
df[df['Language']== 'en'].count() # will give all the columns back with value of 1098
'''
Address             1098
Lot                 1098
AM or PM            1098
Browser Info        1098
Company             1098
Credit Card         1098
CC Exp Date         1098
CC Security Code    1098
CC Provider         1098
Email               1098
Job                 1098
IP Address          1098
Language            1098
Purchase Price      1098
dtype: int64
'''

#TODO ** How many people have the job title of "Lawyer" ? **
df[df['Job'] =='Lawyer'].count() # 30 for all the columns

#TODO ** How many people made the purchase during the AM and how many
# people made the purchase during PM ? **
df[df['AM or PM'] =='AM'].count() #4932
df[df['AM or PM'] =='PM'].count() #5068

#TODO ** What are the 5 most common Job Titles? **
x=df['Job'].value_counts().head(5)
print(x)
'''
Interior and spatial designer    31
Lawyer                           30
Social researcher                28
Purchasing manager               27
Designer, jewellery              27
'''

#TODO ** Someone made a purchase that came from Lot: "90 WT" , what was
# the Purchase Price for this transaction? **
print(df[df['Lot']=='90 WT']['Purchase Price']) #513    75.1

#TODO ** What is the email of the person with the following
# Credit Card Number: 4926535242672853 **
print(df[df['Credit Card']==4926535242672853]['Email']) #1234    bondellen@williams-garza.com

#TODO * How many people have American Express as their Credit
# Card Provider *and made a purchase above $95 ?**
y=df[(df['CC Provider']=='American Express') & (df['Purchase Price']>95)].count()
print(y)# all 39

#TODO ** Hard: How many people have a credit card that expires in 2025? **
print(sum(df['CC Exp Date'].apply(lambda x: x[3:]== '25'))) #1033

#TODO ** Hard: What are the top 5 most popular email providers/hosts
# (e.g. gmail.com, yahoo.com, etc...) **
axc= df['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)
print(axc)
'''
hotmail.com     1638
yahoo.com       1616
gmail.com       1605
smith.com         42
williams.com      37
'''


