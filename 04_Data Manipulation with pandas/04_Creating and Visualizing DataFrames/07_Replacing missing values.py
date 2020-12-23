'''
07 - Replacing missing values

Another way of handling missing  values is to  replace  them  all with  the 
same value. For numerical variables, one option is to  replace values  with 
0— you'll do this here. However, when you replace missing  values, you  make 
assumptions about what a missing value means. In this case,  you will  assume 
that a missing number sold means that no sales for that avocado type were made 
that week.

In this exercise, you'll see how replacing missing values can affect the distribution
 of a variable using histograms. You can plot histograms for multiple variables at a 
 time as follows:

dogs[["height_cm", "weight_kg"]].hist()
pandas has been imported as pd and matplotlib.pyplot has been imported as plt. The
avocados_2016 dataset is available.

Instructions:

 - A list has been created, cols_with_missing, containing the names of columns with missing 
   values: "small_sold", "large_sold", and "xl_sold".

 - Create a histogram of those columns.

 - Show the plot.
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
# List the columns with missing values
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]

# Create histograms showing the distributions cols_with_missing
avocados_2016[cols_with_missing].hist()

# Show the plot
plt.show()

'''
 - Replace the missing values of avocados_2016 with 0s and store the result as avocados_filled.
 - Create a histogram of the cols_with_missing columns of avocados_filled.
'''
# From previous step
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()
