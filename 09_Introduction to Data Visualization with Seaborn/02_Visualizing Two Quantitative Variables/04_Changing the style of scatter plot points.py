'''
04 - Changing the style of scatter plot points

Let's continue exploring Seaborn's mpg dataset by looking at the 
relationship between how fast a car can accelerate ("acceleration") 
and its fuel efficiency ("mpg"). Do these properties vary by country 
of origin ("origin")?

Note that the "acceleration" variable is the time to accelerate from 0 
to 60 miles per hour, in seconds. Higher values indicate slower acceleration.

Instructions

- Use relplot() and the mpg DataFrame to create a scatter plot with "acceleration"
  on the x-axis and "mpg" on the y-axis. Vary the style and color of the plot points 
  by country of origin ("origin").
'''
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x='acceleration',
            y='mpg',
            data=mpg,
            kind='scatter',
            hue='origin',
            style='origin')

# Show plot
plt.show()
