'''
04 - Matplotlib color codes

Seaborn offers several options for modifying the colors of your visualizations.
The simplest approach is to explicitly state the color of the plot. A quick way 
to change colors is to use the standard matplotlib color codes.

Instructions

- Set the default Seaborn style and enable the matplotlib color codes.
- Create a distplot for the fmr_3 column using matplotlib's magenta (m) color code.
'''
# Set style, enable color code, and create a magenta distplot
sns.set(color_codes=True)
sns.distplot(df['fmr_3'], color='m')

# Show the plot
plt.show()
