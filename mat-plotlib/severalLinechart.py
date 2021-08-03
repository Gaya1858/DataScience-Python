from matplotlib import pyplot as plt

variance = [1,2,4,8,16,32,64,128,256]
bias_squared =[256,128,64,32,16,8,4,2,1]
'''
The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is 
paired together, and then the second item in each passed iterator are paired together etc.
If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
syntax: zip(iterator1, iterator2, iterator3 ...)
'''
total_error = [x+y for x,y in zip(variance,bias_squared)]
print(total_error)
xs =[i for i,_ in enumerate(variance)]
# we can make multiple calls to plt.plot
plt.plot(xs,variance,'g-',label='variance') # green solid line
plt.plot(xs,bias_squared,'r-.',label ='bias^2') # red dot-dashed line
plt.plot(xs,total_error,'b:',label ='total error') # blue dotted line

# becasue we have assigned labels to each series ,
# we can get a legend for free (loc =9,means "top center")
'''
plt.legend(loc=num)
Location String	Location Code
'best'	0
'upper right'	1
'upper left'	2
'lower left'	3
'lower right'	4
'right'	5
'center left'	6
'center right'	7
'lower center'	8
'upper center'	9
'center'	10
'''
plt.legend(loc=1)
plt.xlabel("model complexity")
plt.xticks([])
plt.title("The Bias-Variance Tradeoff")
plt.show()
