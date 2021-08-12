'''

'''
import pandas as pd

df =pd.read_csv("salaries.csv")
#print(df.head())
#print(df.info())
'''
Data columns (total 13 columns):
 #   Column            Non-Null Count   Dtype  
---  ------            --------------   -----  
 0   Id                148654 non-null  int64  
 1   EmployeeName      148654 non-null  object 
 2   JobTitle          148654 non-null  object 
 3   BasePay           148045 non-null  float64
 4   OvertimePay       148650 non-null  float64
 5   OtherPay          148650 non-null  float64
 6   Benefits          112491 non-null  float64
 7   TotalPay          148654 non-null  float64
 8   TotalPayBenefits  148654 non-null  float64
 9   Year              148654 non-null  int64  
 10  Notes             0 non-null       float64
 11  Agency            148654 non-null  object 
 12  Status            0 non-null       float64
dtypes: float64(8), int64(2), object(3)
memory usage: 14.7+ MB
'''
print(df['BasePay'].mean()) #  avrage value of basepay 66325.4488404877
print(df['OvertimePay'].max())#  highest amount  of overtime pay 245131.88
'''
** What is the job title of JOSEPH DRISCOLL ? Note: Use all caps, 
otherwise you may get an answer that doesn't match 
up (there is also a lowercase Joseph Driscoll). **
'''
#print(df[df['EmployeeName'] =='JOSEPH DRISCOLL']['JobTitle'])
#24    CAPTAIN, FIRE SUPPRESSION
#Name: JobTitle, dtype: object

#TODO  How much does JOSEPH DRISCOLL make (including benefits)? **
#print(df[df['EmployeeName'] =='JOSEPH DRISCOLL']['TotalPayBenefits'])
# 24    270324.91
# Name: TotalPayBenefits, dtype: float64


#TODO ** What is the name of highest paid person (including benefits)?**
#print(df[df['TotalPayBenefits'].max()== df['TotalPayBenefits']])
'''
Id    EmployeeName  ...         Agency  Status
0   1  NATHANIEL FORD  ...  San Francisco     NaN

[1 rows x 13 columns]
'''
#TODO ** What is the name of highest paid person (including benefits)?**
print(df[df['TotalPayBenefits'] == df['TotalPayBenefits'].max()]['EmployeeName'])
#0    NATHANIEL FORD
#TODO ** What is the name of highest paid person (including benefits)?**
# both of the below method will return the same output
#print(df.loc[df['TotalPayBenefits'].idxmax()])
#print(df.iloc[df['TotalPayBenefits'].argmax()])
'''
Id                                                               1
EmployeeName                                        NATHANIEL FORD
JobTitle            GENERAL MANAGER-METROPOLITAN TRANSIT AUTHORITY
BasePay                                                  167411.18
OvertimePay                                                    0.0
OtherPay                                                 400184.25
Benefits                                                       NaN
TotalPay                                                 567595.43
TotalPayBenefits                                         567595.43
Year                                                          2011
Notes                                                          NaN
Agency                                               San Francisco
Status                                                         NaN
Name: 0, dtype: object
'''
#TODO ** What is the name of lowest paid person (including benefits)? Do you
# notice something strange about how much he or she is paid?**
#print(df.loc[df['TotalPayBenefits'].idxmin()])
#print(df.iloc[df['TotalPayBenefits'].argmin()])
print(df[df['TotalPayBenefits'] == df['TotalPayBenefits'].min()]['EmployeeName'])#Joe Lopez
'''
Id                                      148654
EmployeeName                         Joe Lopez
JobTitle            Counselor, Log Cabin Ranch
BasePay                                    0.0
OvertimePay                                0.0
OtherPay                               -618.13
Benefits                                   0.0
TotalPay                               -618.13
TotalPayBenefits                       -618.13
Year                                      2014
Notes                                      NaN
Agency                           San Francisco
Status                                     NaN
Name: 148653, dtype: object
'''
#TODO ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **
#print(df.groupby('Year').mean()['BasePay'])
'''
Year
2011    63595.956517
2012    65436.406857
2013    69630.030216
2014    66564.421924
Name: BasePay, dtype: float64
'''
#TODO ** How many unique job titles are there? **
#print(df['JobTitle'].nunique()) # return 2159  or sum(df['JobTitle'].unique()))
#TODO ** What are the top 5 most common jobs? **
#print(df['JobTitle'].value_counts().head(5))
'''
Transit Operator                7036
Special Nurse                   4389
Registered Nurse                3736
Public Svc Aide-Public Works    2518
Police Officer 3                2421
Name: JobTitle, dtype: int64
'''
#TODO ** How many Job Titles were represented by only one person in 2013?
# (e.g. Job Titles with only one occurence in 2013?) **

print(sum(df[df['Year']==2013]['JobTitle'].value_counts()==1))#202
#TODO ** How many Job Titles were represented by only one person in 2013? (e.g.
# Job Titles with only one occurence in 2013?) **
def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False
print(sum(df['JobTitle'].apply(lambda x: chief_string(x)))) #477
#TODO Is there a correlation between
# length of the Job Title string and Salary? **
df['title_len']=df['JobTitle'].apply(len)
print(df[['title_len','TotalPayBenefits']].corr())
# title_len  TotalPayBenefits
# title_len          1.000000         -0.036878
# TotalPayBenefits  -0.036878          1.000000