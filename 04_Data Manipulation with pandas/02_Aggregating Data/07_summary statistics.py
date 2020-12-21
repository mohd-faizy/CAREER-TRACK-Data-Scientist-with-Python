'''
07 - What percent of sales occurred at each store type?

While .groupby() is useful, you can calculate grouped summary
statistics without it.

Walmart distinguishes three types of stores: "supercenters,"
"discount stores," and "neighborhood markets," encoded in this
dataset as type "A," "B," and "C." In this exercise, you'll
calculate the total sales made at each store type, without
using .groupby(). You can then use these numbers to see what
proportion of Walmart's total sales were made at each type.

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

# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)
