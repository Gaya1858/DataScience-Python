'''
Distributiong plots for seaborn
Distribution Plots
Let's discuss some plots that allow us to visualize the distribution of a data set. These plots are:

distplot
jointplot
pairplot
rugplot
kdeplot
'''
import seaborn as sns
tips =sns.load_dataset('tips') #Seaborn comes with built-in data sets(tips is one of them)
print(tips.head())

#TODO distplot The distplot shows the distribution of a univariate set of observations.
print(sns.histplot(tips['total_bill']))