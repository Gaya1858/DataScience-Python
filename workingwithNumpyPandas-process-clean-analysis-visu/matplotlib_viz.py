import pandas as pd
from matplotlib import pyplot as plt

dt =pd.read_csv("Data/csv_data.csv",
                names= ["ID","NAME","PRICE","SALES","BRAND"], # you can change the names of the columns using names param
                skiprows=1) # this will skip the row from beginning. in this case we aare removing the heading row

plt.plot(dt['ID'],dt["PRICE"],'--y',markersize =20) # --y = yellow color dotted line
plt.legend(loc=9)
plt.title("Actual Price")
plt.xlabel("ID")
plt.ylabel("Price")

plt.show()