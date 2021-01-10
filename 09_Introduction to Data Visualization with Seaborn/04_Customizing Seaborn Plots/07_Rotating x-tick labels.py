'''
07 - Rotating x-tick labels

In this exercise, we'll continue looking at the miles per gallon  dataset. 
In the code provided, we create a point plot  that  displays  the  average
acceleration for cars in each of the three places of origin. Note that the
"acceleration" variable is the time to accelerate from 0 to 60  miles  per
hour, in seconds. Higher values indicate slower acceleration.

Let's use this plot to practice rotating the x-tick labels. Recall that the 
function to rotate x-tick labels is a standalone Matplotlib function and not 
a function applied to the plot object itself.

We've already imported Seaborn as sns and matplotlib.pyplot as plt.

Instructions

- Rotate the x-tick labels 90 degrees.
'''
# Create point plot
sns.catplot(x="origin",
            y="acceleration",
            data=mpg,
            kind="point",
            join=False,
            capsize=0.1)

# Rotate x-tick labels
plt.xticks(rotation=90)

# Show plot
plt.show()
