'''
09 - Multiple grouped summaries

Earlier in this chapter, you saw that the .agg() method is useful to
compute multiple statistics on multiple variables. It also works with
grouped data. NumPy, which is imported as np, has many different summary
statistics functions, including: np.min, np.max, np.mean, and np.median.

Instructions:

 - Import numpy with the alias np.
 
 - Get the min, max, mean, and median of weekly_sales for each store type
   using .groupby() and .agg(). Store this as sales_stats. Make sure to use
   numpy functions!
 
 - Get the min, max, mean, and median of unemployment and fuel_price_usd_per_l
   for each store type. Store this as unemp_fuel_stats.

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
# Import numpy with the alias np
import numpy as np

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby('type')['weekly_sales'].agg([np.min, np.max, np.mean, np.median])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby('type')[['fuel_price_usd_per_l', 'unemployment']].agg([np.min, np.max, np.mean, np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)
