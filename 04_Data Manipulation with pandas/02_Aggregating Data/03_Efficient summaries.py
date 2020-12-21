'''
03 - Efficient summaries

While pandas and NumPy have tons of functions, sometimes, you may need a different
function to summarize your data.

The .agg() method allows you to apply your own custom functions to a DataFrame,
as well as apply functions to more than one column of a DataFrame at once, making
your aggregations super-efficient.

For example:

df['column'].agg(function)

In the custom function for this exercise,"IQR" is short for inter-quartile range,
which is the 75th percentile minus the 25th percentile. It's an alternative to
standard deviation that is helpful if your data contains outliers.

Instructions:

1. Use the custom iqr function defined for you along with .agg() to print the IQR
   of the temperature_c column of sales.


2. Update the column selection to use the custom iqr function with .agg() to print
   the IQR of temperature_c, fuel_price_usd_per_l, and unemployment, in that order.

3. Update the aggregation functions called by .agg(): include iqr and np.median
   in that order.
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


# Import pandas using the alias pd
import pandas as pd
sales = pd.read_csv('content/wallmart_sales.csv')

# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Print IQR of the temperature_c column
print(sales['temperature_c'].agg(iqr))
