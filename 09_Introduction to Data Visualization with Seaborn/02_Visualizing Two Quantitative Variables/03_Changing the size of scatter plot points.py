'''
03 - Changing the size of scatter plot points

In this exercise, we'll explore Seaborn's mpg  dataset,  which  contains 
one row per car model and includes information such as the year  the  car 
was made, the number of miles per gallon ("M.P.G.") it achieves, the power 
of its engine (measured in "horsepower"), and its country of origin.

What is the relationship between the power of a car's engine ("horsepower") and
its fuel efficiency ("mpg")? And how does this relationship vary by the number of 
cylinders ("cylinders") the car has? Let's find out.

Let's continue to use relplot() instead of scatterplot() since it offers more flexibility.

Instructions 1/2

- Use relplot() and the mpg DataFrame to create a scatter plot with "horsepower" on 
  the x-axis and "mpg" on the y-axis. Vary the size of the points by the number of cylinders 
  in the car ("cylinders").
'''
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
sns.relplot(x='horsepower',
            y='mpg',
            data=mpg,
            kind='scatter',
            size='cylinders')

# Show plot
plt.show()

'''
Instructions 2/2

- To make this plot easier to read, use hue to vary the color of the points by the number 
  of cylinders in the car ("cylinders").
'''
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", 
            data=mpg, kind="scatter", 
            size="cylinders",
            hue="cylinders")

# Show plot
plt.show()