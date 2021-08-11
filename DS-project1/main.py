import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("trees.csv",names= ['Index','Girth','Height','Volume'],skiprows =1)
data.drop(columns="Index",inplace=True)
data.index =data.index+1
average = data.mean()
d_median =data.median()
d_mode =data.mode()
d_max =data.max()
d_min = data.min()
d_range = d_max-d_min

print(data)