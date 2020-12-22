'''
05 - Dropping duplicates

Removing duplicates is an essential skill  to  get  accurate
counts because often, you don't want to count the same thing
multiple times. In this exercise,  you'll  create  some  new
DataFrames using unique values from sales.

Instructions:

 - Remove rows of sales with duplicate pairs of store and type and save
   as store_types and print the head.

 - Remove rows of sales with duplicate pairs of store and department and
   save as store_depts and print the head.

 - Subset the rows that are holiday weeks using the is_holiday column, and
   drop the duplicate dates, saving as holiday_dates.

 - Select the date column of holiday_dates, and print.
 ---------------------------------------------------------------------------------------------------------------
sales.head()

store type  department          date  weekly_sales  is_holiday  temperature_c  fuel_price_usd_per_l  unemployment
0      1    A           1 2010-02-05      24924.50       False          5.728                 0.679         8.106
1      1    A           1 2010-03-05      21827.90       False          8.056                 0.693         8.106
2      1    A           1 2010-04-02      57258.43       False         16.817                 0.718         7.808
3      1    A           1 2010-05-07      17413.94       False         22.528                 0.749         7.808
4      1    A           1 2010-06-04      17558.09       False         27.050                 0.715         7.808
 ----------------------------------------------------------------------------------------------------------------
'''

# Import pandas and numpy
import numpy as np
import pandas as pd

sales = pd.read_csv('content/wallmart_sales.csv')

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=['store', 'type'])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=['store', 'department'])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales['is_holiday']].drop_duplicates('date')

# Print date col of holiday_dates
print(holiday_dates)
