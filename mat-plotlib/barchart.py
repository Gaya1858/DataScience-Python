'''
matplotlib library is used to visualize data
A wide variety of toole exist out  but we are using matplotlip.
http://matplotlib.org
it is used for simple bar charts,line charts and scatter plots

'''
from matplotlib import pyplot as plt

years =[1950,1960,1970,1980,1990,2000,2010]
gdp =[300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3]
#
# #  creating a line chart  years in x-axis and gdp on y-axis
# plt.plot(years,gdp,color ="blue",marker ='v',linestyle ='dotted')
# # add a title
# plt.title("Nominal GDP")
# # add a label to the y-axis
# plt.ylabel("Billions of $")
# plt.xlabel("Years")
#plt.show()

# bar chart - to show how some quantity varies among some discrete set of items
movie =["anni hall","ben-hur","Casablanca","vettri","billa","indian"]
num_oscars =[5,3,2,4,12,50]

# plot bars with left x-coordinates [0,1,2,3,4], heights[num_oscars]
plt.bar(range(len(movie)),num_oscars)
plt.title("My Favorite Movies")
plt.ylabel('# of Academy Awards')
# label x-axis with movie name at bar centers
plt.xticks(range(len(movie)),movie)
plt.show()