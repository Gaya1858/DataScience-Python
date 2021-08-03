from matplotlib import pyplot as plt

# scatter plot is the right choice for visualizing the relationship between teo paried sets of data.

friends =[70,65,72,63,72,64,60,64,67]
minutes =[175,170,205,120,220,130,105,145,190]
lables =['a','b','c','d','e','f','g','h','i']

plt.scatter(friends,minutes)

# label each point
for label, friend_count,minutes_count in zip(lables,friends,minutes):
    plt.annotate(label,
                 xy=(friend_count,minutes_count), # put label with its point
                 xytext =(5,5),# but slightly offset
                 textcoords ='offset points')
plt.axis([59,75,104,230])
plt.title("Daily Minutes vs. NUmber of Friends")
plt.xlabel("# of Friends")
plt.ylabel("dailt minutes spent on the site")
plt.show()