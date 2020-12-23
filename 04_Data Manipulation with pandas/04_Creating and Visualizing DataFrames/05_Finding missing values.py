'''
Finding missing values:

Missing values are everywhere, and you don't want them interfering with your work.
Some functions ignore missing data by default, but that's not always the  behavior
you might want. Some functions can't handle missing values at all, so these values
need to be taken care of before you can use  them. If  you don't  know  where  your
missing values are, or if they exist, you could  make  mistakes  in  your  analysis. 
In this exercise, you'll determine if there are missing values in the dataset, and if 
so, how many.

pandas has been imported as pd and avocados_2016, a subset of avocados that contains 
only sales from 2016, is available.

Instructions:

 - Print a DataFrame that shows whether each value in avocados_2016 is missing or not.
 
 - Print a summary that shows whether any value in each column is missing or not.
 
 - Create a bar plot of the total number of missing values in each column.
 
----------------------------------------------------------------------------------------------------------------------------------------
 avocados_2016.head()

         date  avg_price  total_sold  small_sold  large_sold    xl_sold  total_bags_sold  small_bags_sold  large_bags_sold  xl_bags_sold
0  2016-12-25       1.00   3.029e+07   9.255e+06   1.028e+07  541972.42        1.021e+07        7.710e+06        2.417e+06      81101.22
1  2016-12-18       0.96   2.958e+07   9.394e+06   1.034e+07  427872.42        9.423e+06        6.970e+06        2.358e+06      94011.78
2  2016-12-11       0.98   3.009e+07   9.010e+06         NaN  403047.93        1.071e+07        8.149e+06        2.490e+06      73342.82
3  2016-12-04       1.00   3.162e+07   1.104e+07   9.909e+06  428009.84        1.024e+07        7.187e+06        2.989e+06      65350.63
4  2016-11-27       1.21   2.292e+07   7.891e+06   7.337e+06        NaN        7.350e+06        5.691e+06        1.610e+06      48623.28
----------------------------------------------------------------------------------------------------------------------------------------
'''

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind='bar')

# Show plot
plt.show()
