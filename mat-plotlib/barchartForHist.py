from matplotlib import pyplot as plt
from collections import Counter

grades =[67,57,98,78,82,45,20,49,94,76,0,100,77,0]
# bucket grades by decile, but put 100 in the 99s
'''
COUNTER CLASS
class collections.Counter([iterable-or-mapping])
A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.

Elements are counted from an iterable or initialized from another mapping (or counter):

>>>
>>> c = Counter()                           # a new, empty counter
>>> c = Counter('gallahad')                 # a new counter from an iterable
>>> c = Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
>>> c = Counter(cats=4, dogs=8)             # a new counter from keyword args
Counter objects have a dictionary interface except that they return a zero count for missing items instead of raising a KeyError:

>>>
>>> c = Counter(['eggs', 'ham'])
>>> c['bacon']                              # count of a miss
'''
histogram = Counter(min(grade//10*10,90) for grade in grades)
#print(histogram) Counter({90: 3, 70: 3, 40: 2, 0: 2, 60: 1, 50: 1, 80: 1, 20: 1})
plt.bar([x+5 for x in histogram.keys()], # shift bars right by 5
        histogram.values(), #give each bar its correct height
        10,# give each bar a width of ten
        edgecolor =(0,0,0))# balck edge for each bar

plt.axis([-5,105,0,5]) # x-axis from -5 to 105, y-axis from 0 to 5
plt.xticks([10*i for i in range(11)]) # x-axis labels at 0, 10,...100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()