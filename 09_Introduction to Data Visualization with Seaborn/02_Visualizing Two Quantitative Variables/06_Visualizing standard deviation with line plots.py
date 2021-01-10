'''
06 - Visualizing standard deviation with line plots

In the last exercise, we looked at how the  average  miles  per 
gallon achieved by cars has changed over time. Now let's use  a 
line plot to visualize how the distribution of miles per gallon 
has changed over time.

Seaborn has been imported as sns and matplotlib.pyplot has been imported
as plt.

Instructions:

- Change the plot so the shaded area shows the standard deviation instead of the 
  confidence interval for the mean.
'''
# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line", ci='sd')

# Show plot
plt.show()
