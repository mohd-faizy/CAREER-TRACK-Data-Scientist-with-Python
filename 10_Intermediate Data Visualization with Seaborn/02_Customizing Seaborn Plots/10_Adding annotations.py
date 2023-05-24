'''
10 - Adding annotations

Each of the enhancements we have covered  can  be  combined  together. 
In the next exercise, we can annotate our distribution plot to include
lines that show the mean and median rent prices.

For this example, the palette has been changed to bright using sns.set_palette()

Instructions:

- Create a figure and axes.
- Plot the fmr_1 column distribution.
- Add a vertical line using axvline for the median and mean of the values which are 
  already defined.
'''
# Create a figure and axes. Then plot the data
fig, ax = plt.subplots()
sns.distplot(df['fmr_1'], ax=ax)

# Customize the labels and limits
ax.set(xlabel="1 Bedroom Fair Market Rent", xlim=(100, 1500), title="US Rent")

# Add vertical lines for the median and mean
ax.axvline(x=median, color='m', label='Median', linestyle='--', linewidth=2)
ax.axvline(x=mean, color='b', label='Mean', linestyle='-', linewidth=2)

# Show the legend and plot the data
ax.legend()
plt.show()
