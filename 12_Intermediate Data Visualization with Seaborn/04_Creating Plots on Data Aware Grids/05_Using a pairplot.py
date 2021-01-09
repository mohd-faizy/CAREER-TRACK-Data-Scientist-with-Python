'''
06 - Using a pairplot

The pairplot() function is generally a more  convenient  way  to
look at pairwise relationships. In this exercise, we will create
the same results as the PairGrid using less code. Then, we will 
explore some additional functionality of the pairplot(). We will 
also use a different palette and adjust the transparency of the 
diagonal plots using the alpha parameter.
'''
# 1/2
# Recreate the pairwise plot from the previous exercise using pairplot().
sns.pairplot(data=df,
             vars=["fatal_collisions", "premiums"],
             kind='scatter')

plt.show()
plt.clf()

# 2/2
# Create another pairplot using the "Region" to color code the results.
# Use the RdBu palette to change the colors of the plot.
sns.pairplot(data=df,
             vars=["fatal_collisions", "premiums"],
             kind='scatter',
             hue='Region',
             palette='RdBu',
             diag_kws={'alpha': .5})

plt.show()
plt.clf()
