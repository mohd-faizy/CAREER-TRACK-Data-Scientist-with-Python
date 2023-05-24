'''
02 - Using a factorplot

In many cases, Seaborn's factorplot() can be a simpler way to create
a FacetGrid. Instead of creating a grid and mapping the plot, we can 
use the factorplot() to create a plot with one line of code.

For this exercise, we will recreate one of the plots from the previous
exercise using factorplot() and show how to create a boxplot on a data-
aware grid.
'''
# 1/2---------------------------------------------------------------------------
# Create a factorplot() that contains a boxplot (box) of Tuition values varying by Degree_Type across rows.
sns.factorplot(data=df,
               x='Tuition',
               kind='box',
               row='Degree_Type')

plt.show()
plt.clf()

# 2/2---------------------------------------------------------------------------
# Create a factorplot() of SAT Averages(SAT_AVG_ALL) facetted across Degree_Type that shows a pointplot(point).
# Use row_order to order the degrees from highest to lowest level.
# Create a facetted pointplot of Average SAT_AVG_ALL scores facetted by Degree Type
sns.factorplot(data=df,
               x='SAT_AVG_ALL',
               kind='point',
               row='Degree_Type',
               row_order=['Graduate', 'Bachelors', 'Associates', 'Certificate'])

plt.show()
plt.clf()
