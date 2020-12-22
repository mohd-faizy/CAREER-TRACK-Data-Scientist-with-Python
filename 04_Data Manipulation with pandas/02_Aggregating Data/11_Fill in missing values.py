'''
11 - Fill in missing values and sum values with pivot tables:

The .pivot_table() method has several useful arguments, including fill_value 
and margins.

 - fill_value replaces missing values with a real value (known as imputation).
   What to replace missing values with is a topic big enough to have  its  own
   course (Dealing with Missing Data in Python), but the simplest thing  to do
   is to substitute a dummy value.
 
 - margins is a shortcut for when you pivoted by two variables, but also wanted
   to pivot by each of those variables separately: it gives the row  and column 
   totals of the pivot table contents.

In this exercise, you'll practice using these arguments to up your  pivot  table
skills, which will help you crunch numbers more efficiently!

Instructions:

 - Print the mean weekly_sales by department and type, filling in any missing
   values with 0.

 - Print the mean weekly_sales by department and type, filling in any missing
   values with 0 and summing all rows and columns.
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

# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values='weekly_sales', index='type', columns=None, fill_value=0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, margins=0))

                        
