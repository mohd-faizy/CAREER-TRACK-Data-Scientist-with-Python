'''
01 - Using the matplotlib.pyplot interface

There are many ways to use Matplotlib. In this course, we will focus  on the  pyplot  interface, 
which provides the most flexibility in creating and customizing data visualizations.

Initially, we will use the pyplot interface to create two kinds of  objects: Figure objects  and
Axes objects.

This course introduces a lot of new concepts, so if you ever need a quick refresher, download the 
Matplotlib Cheat Sheet and keep it handy!

Instructions:

 - Import the matplotlib.pyplot API, using the conventional name plt.
 - Create Figure and Axes objects using the plt.subplots function.
 - Show the results, an empty set of axes, using the plt.show function.

'''

# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Call the show function to show the result
plt.show()
