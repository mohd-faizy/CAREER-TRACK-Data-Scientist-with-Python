'''
02 - Making a count plot with a list

In the last exercise, we explored a dataset that contains information 
about 227 countries. Let's do more exploration of this data - specifically, 
how many countries are in each region of the world?

To do this, we'll need to use a count plot. Count plots take in a categorical 
list and return bars that represent the number of list entries per category. 
You can create one here using a list of regions for each country, which is a 
variable named region.

Instructions

- Import Matplotlib and Seaborn using the standard naming conventions.
- Use Seaborn to create a count plot with region on the y-axis.
- Display the plot.
'''
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()
