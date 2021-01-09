'''
07 - Building a JointGrid and jointplot

Seaborn's JointGrid combines univariate plots such as histograms,
rug plots and kde plots with bivariate plots such as scatter and 
regression plots. The process for creating these plots should be 
familiar to you now. These plots also  demonstrate  how  Seaborn 
provides convenient functions to combine multiple plots together.

For these exercises, we will use the bike share data that we reviewed
earlier. In this exercise, we will look at the relationship between 
humidity levels and total rentals to see if there is an interesting 
relationship we might want to explore later.

Instructions 1/2

- Use Seaborn's "whitegrid" style for these plots.
- Create a JointGrid() with "hum" on the x-axis and "total_rentals" on the y.
- Plot a regplot() and distplot() on the margins.
'''
# Build a JointGrid comparing humidity and total_rentals
sns.set_style("whitegrid")
g = sns.JointGrid(x="hum",
                  y="total_rentals",
                  data=df,
                  xlim=(0.1, 1.0))

g.plot(sns.regplot, sns.distplot)

plt.show()
plt.clf()

'''
Instructions 2/2

- Re-create the plot using a jointplot().
'''
# Create a jointplot similar to the JointGrid
sns.jointplot(x="hum",
              y="total_rentals",
              kind='reg',
              data=df)

plt.show()
plt.clf()

