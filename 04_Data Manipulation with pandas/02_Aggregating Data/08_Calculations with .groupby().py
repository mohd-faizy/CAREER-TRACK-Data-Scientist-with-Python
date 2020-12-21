'''
08 - Calculations with .groupby()

The .groupby() method makes life  much  easier. In  this  exercise,
you'll perform the same calculations  as last time,  except  you'll
use the .groupby() method. You'll also perform calculations on data
grouped by two variables to see if sales differ by store type depending
on if it's a holiday week or not.

Instructions:

 - Group sales by "type", take the sum of "weekly_sales", and store as
   sales_by_type.
 
 - Calculate the proportion of sales at each store type by dividing by 
   the sum of sales_by_type. Assign to sales_propn_by_type.
 
 - Group sales by "type" and "is_holiday", take the sum of weekly_sales,
   and store as sales_by_type_is_holiday.

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
# Import pandas using the alias pd
import numpy as np
import pandas as pd

sales = pd.read_csv('content/wallmart_sales.csv')

# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = sales_by_type / sum(sales["weekly_sales"])
print(sales_propn_by_type)

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = ____
print(sales_by_type_is_holiday)
