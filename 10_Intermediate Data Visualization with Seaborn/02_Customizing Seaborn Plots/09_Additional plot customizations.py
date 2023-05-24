'''
09 - Additional plot customizations

The matplotlib API supports many common customizations  such  as 
labeling axes, adding titles, and setting limits. Let's complete 
another customization exercise.

Instructions

- Create a distplot of the fmr_1 column.
- Modify the x axis label to say "1 Bedroom Fair Market Rent".
- Change the x axis limits to be between 100 and 1500.
- Add a descriptive title of "US Rent" to the plot.
'''
# Create a figure and axes
fig, ax = plt.subplots()

# Plot the distribution of 1 bedroom rents
sns.distplot(df['fmr_1'], ax=ax)

# Modify the properties of the plot
ax.set(xlabel="1 Bedroom Fair Market Rent",
       xlim=(100, 1500),
       title="US Rent")

# Display the plot
plt.show()
