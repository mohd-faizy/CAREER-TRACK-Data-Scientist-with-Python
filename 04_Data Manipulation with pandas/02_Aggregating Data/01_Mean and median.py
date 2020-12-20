'''
01 - Mean and median
Summary statistics are exactly what they sound like
they summarize many numbers in one statistic. For example:
 - mean
 - median
 - minimum
 - maximum &
 - standard deviation

Calculating summary statistics allows you to get a better sense
of your data, even if there's a lot of it.

Instructions:

 - Explore your new DataFrame first by printing the first few rows of the sales DataFrame.
 - Print information about the columns in sales.
 - Print the mean of the weekly_sales column.
 - Print the median of the weekly_sales column.
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

# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales['weekly_sales'].mean())

# Print the median of weekly_sales
print(sales['weekly_sales'].median())
