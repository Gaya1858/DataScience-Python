import pandas as pd
import matplotlib.pyplot as plt
### Data Visualization

dt =pd.read_csv("Data/csv_data.csv",
                names= ["ID","NAME","PRICE","SALES","BRAND"], # you can change the names of the columns using names param
                skiprows=1) # this will skip the row from beginning. in this case we aare removing the heading row
#print(dt.plot()) #AxesSubplot(0.125,0.11;0.775x0.77)
#TODO dt['SALES'].plot() # plots just sales, you dont mention will plot all numerical values
#TODO dt.plot.bar() # will be 3 colored bar chart
#TODO dt.plot.barh() # will show the bar chart in horizontally
#TODO dt.plot.bar(stacked= True) # bar chart colors will be stacked as one bar
#TODO dt.plot.area() # how much area that dat is covering
#TODO dt.plot.hist() # ploting histogram
print(dt['SALES'].sum())
dt_analytics =pd.DataFrame({'Actual Sales':dt['SALES'],
                            'Total Sales': [665,665,665,665,665,665],
                            'Average Sales':[83,83,83,83,83,83]
                            })
dt_analytics.plot.bar(stacked =False)
plt.show()

