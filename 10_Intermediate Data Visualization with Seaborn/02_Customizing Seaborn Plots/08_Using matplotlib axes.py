'''
08 - Using matplotlib axes

Seaborn uses matplotlib as the underlying library for creating plots. Most
of the time, you can use the Seaborn API to modify your visualizations but 
sometimes it is helpful to use matplotlib's  functions  to  customize  your
plots. The most important object in this case is matplotlib's axes.

Once you have an axes object, you can perform a lot of customization of your
plot.

In these examples, the US HUD data is loaded in the dataframe df and all libraries
are imported.

Instructions:

- Use plt.subplots() to create a axes and figure objects.
- Plot a distplot of column fmr_3 on the axes.
- Set a more useful label on the x axis of "3 Bedroom Fair Market Rent".
'''
# Create a figure and axes
fig, ax = plt.subplots()

# Plot the distribution of data
sns.distplot(df['fmr_3'], ax=ax)

# Create a more descriptive x axis label
ax.set(xlabel="3 Bedroom Fair Market Rent")

# Show the plot
plt.show()
