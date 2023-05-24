'''
01 - Building a FacetGrid

Seaborn's FacetGrid is the foundation for building data-aware grids.
A data-aware grid allows you to create a series of small plots  that 
can be useful for understanding complex data relationships.

For these exercises, we will continue to look at the College Scorecard 
Data from the US Department of Education. This rich  dataset has  many 
interesting data elements that we can plot with Seaborn.

When building a FacetGrid, there are two steps:

 - Create a FacetGrid object with columns, rows, or hue.
 - Map individual plots to the grid.

Instructions:

- Create a FacetGrid that shows a point plot of the Average SAT scores SAT_AVG_ALL.
- Use row_order to control the display order of the degree types.
'''
# Create FacetGrid with Degree_Type and specify the order of the rows using row_order
g2 = sns.FacetGrid(df,
                   row="Degree_Type",
                   row_order=['Graduate', 'Bachelors', 'Associates', 'Certificate'])

# Map a pointplot of SAT_AVG_ALL onto the grid
g2.map(sns.pointplot, 'SAT_AVG_ALL')

# Show the plot
plt.show()
plt.clf()
