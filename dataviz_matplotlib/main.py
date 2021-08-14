'''
All about matplotlib
dive into deep matplotlib goto www.matplotlib.org/gallery
'''
import matplotlib.pyplot as plt
import numpy as np
'''
# %matplotlib inline only for notebook
That line is only for jupyter notebooks, if you are using another editor, you'll use: plt.show() at the end of all your plotting 
commands to have the figure pop up in another window.
'''
x =np.linspace(0,5,11)
y=x**2
# commands for 2 ways creating plot
#1. functional method and 2.OOP method

# 1.functions method
#plt.plot(x,y)
plt.subplot(1,2,1) # to create multiple plots on the same table.
plt.plot(x,y,'r')
plt.subplot(1,2,2)
plt.plot(y,x,'b')

#plt.show()
'''
Matplotlib Object Oriented Method¶
Now that we've seen the basics, let's break it all down with a more formal introduction of 
Matplotlib's Object Oriented API. This means we will instantiate figure objects and then call methods 
or attributes from that object
Introduction to the Object Oriented Method¶
The main idea in using the more formal Object Oriented method is to create figure objects and then 
just call methods or attributes off of that object. This approach is nicer when dealing with a canvas 
that has multiple plots on it.

To begin we create a figure instance. Then we can add axes to that figure:
'''
# 2.OOP method
fig=plt.figure() # figure object has been created. This figure  object is like imaginary
# blank canvas . We can add set of axis to the canvas
axes =fig.add_axes([0.1,0.1,0.8,0.8],facecolor ='r') # [left, bottom, width, height] value always (0 to 1)
axes.plot(x,y)
axes.set_xlabel("X label")
axes.set_ylabel("Y label")
axes.set_title("Example")
fig =plt.figure()
axes1=fig.add_axes([0.1,0.1,0.8,0.8]) # creating plot inside plot - outplot
axes2=fig.add_axes([0.2,0.5,0.4,0.3])# inner plot
'''
subplots()
The plt.subplots() object will act as a more automatic axis manager.
'''
# Use similar to plt.figure() except use tuple unpacking to grab fig and axes
fig1, axes = plt.subplots()

# Now use the axes object to add stuff to plot
axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title')
axes.axhline(linewidth=4, color='r') #draw a thick red hline at ‘y’ = 0 that spans the xrange:
axes.axhline(y=1) #draw a default hline at ‘y’ = 1 that spans the xrange:
axes.axhline(y=.5, xmin=0.25, xmax=0.75)#draw a default hline at ‘y’ = .5 that spans the middle half of the xrange:
'''
Then you can specify the number of rows and columns when creating the 
subplots() object:
'''
# Empty canvas of 1 by 2 subplots
fig1, axes = plt.subplots(nrows=1, ncols=2)
# We can iterate through this array:
for ax in axes: # axes[0].plot(x,y) ploting one by one
    ax.plot(x, y, 'b')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')

'''
A common issue with matplolib is overlapping subplots or figures. We ca use 
fig.tight_layout() or plt.tight_layout() method, which automatically adjusts the positions 
of the axes on the figure canvas so that there is no overlapping content:
'''
fig2, axes = plt.subplots(nrows=1, ncols=2)

for ax in axes:
    ax.plot(x, y, 'g')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')



plt.tight_layout() # always put at the end of the plot

'''
Figure size, aspect ratio and DPI
Matplotlib allows the aspect ratio, DPI and figure size to be specified when the Figure object is created. 
You can use the figsize and dpi keyword arguments.

****figsize is a tuple of the width and height of the figure in inches
****dpi is the dots-per-inch (pixel per inch).
'''
fig4 = plt.figure(figsize=(8,4), dpi=100) # figsize = width & height
fig4, axes = plt.subplots(figsize=(12,3))

axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title');
'''
Saving figures
Matplotlib can generate high-quality output in a number formats, 
including PNG, JPG, EPS, SVG, PGF and PDF.

To save a figure to a file we can use the savefig method in the 
Figure class:
'''
fig.savefig("filename.png", dpi=200) # will save the figure to the file
'''
Legends, labels and titles
Now that we have covered the basics of how to create a figure canvas and add axes instances to the canvas, 
let's look at how decorate a figure with titles, axis labels, and legends.

Figure titles

A title can be added to each axis instance in a figure. To set the title, use the set_title method 
in the axes instance:
'''
fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x, x**2,'b.-', label="x**2")
ax.plot(x, x**3,'g--', label="x**3")
ax.legend()
'''
to avoid overlaps between legend and plot
we can pass a value to loc argiment
 Lots of options....

ax.legend(loc=1) # upper right corner
ax.legend(loc=2) # upper left corner
ax.legend(loc=3) # lower left corner
ax.legend(loc=4) # lower right corner

# .. many more options are available

# Most common to choose
ax.legend(loc=0) # let matplotlib decide the opt
'''
'''
Colors with the color= parameter
We can also define colors by their names or RGB hex codes and optionally provide an 
alpha value using the color 
and alpha keyword arguments. Alpha indicates opacity.
'''
fig, ax = plt.subplots()

ax.plot(x, x+1, color="blue", alpha=0.5) # half-transparant
ax.plot(x, x+2, color="#8B008B")        # RGB hex code
ax.plot(x, x+3, color="#FF8C00")        # RGB hex code

'''
Line and marker styles
To change the line width, we can use the linewidth or lw keyword argument. The line style can be 
selected using the linestyle or ls keyword arguments:

'''
fig, ax = plt.subplots(figsize=(12,6))

ax.plot(x, x+1, color="red", linewidth=0.25)
ax.plot(x, x+2, color="red", linewidth=0.50)
ax.plot(x, x+3, color="red", linewidth=1.00)
ax.plot(x, x+4, color="red", linewidth=2.00)

# possible linestype options ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
ax.plot(x, x+5, color="green", lw=3, linestyle='-')
ax.plot(x, x+6, color="green", lw=3, ls='-.')
ax.plot(x, x+7, color="green", lw=3, ls=':')

# custom dash
line, = ax.plot(x, x+8, color="black", lw=1.50)
line.set_dashes([5, 10, 15, 10]) # format: line length, space length, ...

# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax.plot(x, x+ 9, color="blue", lw=3, ls='-', marker='+')
ax.plot(x, x+10, color="blue", lw=3, ls='--', marker='o')
ax.plot(x, x+11, color="blue", lw=3, ls='-', marker='s')
ax.plot(x, x+12, color="blue", lw=3, ls='--', marker='1')

# marker size and color
ax.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
ax.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
ax.plot(x, x+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
ax.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8,
markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="green")
fig.savefig("line_color.png", dpi=200)

'''
Control over axis appearance
Plot range
We can configure the ranges of the axes using the set_ylim and set_xlim methods in the axis object, 
or axis('tight') for automatically getting "tightly fitted" axes ranges:
'''
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].plot(x, x**2, x, x**3)
axes[0].set_title("default axes ranges")

axes[1].plot(x, x**2, x, x**3)
axes[1].axis('tight')
axes[1].set_title("tight axes")

axes[2].plot(x, x**2, x, x**3)
axes[2].set_ylim([0, 60])
axes[2].set_xlim([2, 5])
axes[2].set_title("custom axes range")
fig.savefig("limit.png", dpi=200)

'''
Special Plot Types
There are many specialized plots we can create, 
such as barplots, 
histograms, 
scatter plots, and much more. 
Most of these type of plots we will actually create using seaborn, 
a statistical plotting library for Python. 
But here are a few examples of these type of plots:
'''
plt.scatter(x,y) # scatter plot

from random import sample
data = sample(range(1, 1000), 100)
plt.hist(data) # histogram

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# rectangular box plot
plt.boxplot(data,vert=True,patch_artist=True);
plt.show()