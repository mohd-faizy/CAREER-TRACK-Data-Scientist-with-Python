'''
01 - stripplot() and swarmplot()

Many datasets have categorical data and Seaborn supports several useful
plot types for this data. In this example, we will continue to look  at 
the 2010 School Improvement data and segment the data by the  types  of 
school improvement models used.

As a refresher, here is the KDE distribution of the Award Amounts:
-01_Image-

While this plot is useful, there is a lot more we can learn by looking at 
the individual Award_Amounts and how they are distributed among the 4 categories.
'''
# 1 - stripplot
# Create a stripplot of the Award_Amount with the Model Selected on the y axis with jitter enabled.
sns.stripplot(data=df,
              x='Award_Amount',
              y='Model Selected',
              jitter=True)

plt.show()

# 2 - swarmplot
# Create a swarmplot() of the same data, but also include the hue by Region.
sns.swarmplot(data=df,
              x='Award_Amount',
              y='Model Selected',
              hue='Region')

plt.show()
