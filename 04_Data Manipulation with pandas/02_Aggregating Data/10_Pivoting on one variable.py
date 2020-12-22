'''
10 - Pivoting on one variable

Pivot tables are the standard way of aggregating data in spreadsheets.
In pandas, pivot tables are essentially just another way of performing
grouped calculations. That is, the .pivot_table() method  is  just  an
alternative to .groupby().

In this exercise, you'll perform calculations using  .pivot_table()  to
replicate the calculations you performed in the last lesson using .groupby().

sales is available and pandas is imported as pd.

Instructions:

 - Get the mean weekly_sales by type using .pivot_table() and store as
   mean_sales_by_type.

 - Get the mean and median (using NumPy functions) of  weekly_sales  by
   type using .pivot_table() and store as mean_med_sales_by_type.

 - Get the mean of weekly_sales by type and is_holiday using .pivot_table()
   and store as mean_sales_by_type_holiday.
-----------------------------------------------------------------------------------------------------------------
sales.head()

   store type  department       date  weekly_sales  is_holiday  temperature_c  fuel_price_usd_per_l  unemployment
0      1    A           1 2010-02-05      24924.50       False          5.728                 0.679         8.106
1      1    A           1 2010-03-05      21827.90       False          8.056                 0.693         8.106
2      1    A           1 2010-04-02      57258.43       False         16.817                 0.718         7.808
3      1    A           1 2010-05-07      17413.94       False         22.528                 0.749         7.808
4      1    A           1 2010-06-04      17558.09       False         27.050                 0.715         7.808
-----------------------------------------------------------------------------------------------------------------
'''
# Import pandas and numpy
import numpy as np
import pandas as pd

sales = pd.read_csv('content/wallmart_sales.csv')

# By default Pivot table calculate the mean
# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values='weekly_sales', index='type')

# Print mean_sales_by_type
print(mean_sales_by_type)

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values='weekly_sales', index='type', aggfunc=[np.mean, np.median])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# Pivot for mean weekly_sales by store type and holiday
mean_sales_by_type_holiday = sales.pivot_table(values='weekly_sales', index='type', columns='is_holiday')

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)
