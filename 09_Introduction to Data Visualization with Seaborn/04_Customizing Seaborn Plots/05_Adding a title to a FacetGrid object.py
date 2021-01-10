'''
05 - Adding a title to a FacetGrid object

In the previous exercise, we used  relplot() with  the  miles  per  gallon
dataset to create a scatter plot  showing  the relationship between a car's
weight and its  horsepower. This  created a  FacetGrid  object. Now that we
know what type of object it is, let's add a title to this plot. We've already
imported Seaborn as sns and matplotlib.pyplot as plt.

Instructions

- Add the following title to this plot: "Car Weight vs. Horsepower".
'''
# Create scatter plot
g = sns.relplot(x="weight",
                y="horsepower",
                data=mpg,
                kind="scatter")

# Add a title "Car Weight vs. Horsepower"
g.fig.suptitle("Car Weight vs. Horsepower")

# Show plot
plt.show()
