'''
04 - Removing spines
In general, visualizations should minimize extraneous markings so that the data
speaks for itself. Seaborn allows you to remove the lines on the top, bottom, left
and right axis, which are often called spines.

Instructions:

- Use a white style for the plot.
- Create a lmplot() comparing the pop2010 and the fmr_2 columns.
- Remove the top and right spines using despine().
'''
# Set the style to white
sns.set_style('white')

# Create a regression plot
sns.lmplot(data=df,
           x='pop2010',
           y='fmr_2')

# Remove the spines
sns.despine(right=True)

# Show the plot and clear the figure
plt.show()
plt.clf()
