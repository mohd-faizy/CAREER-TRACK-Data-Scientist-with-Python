'''
04 - Cumulative statistics

Cumulative statistics  can also  be  helpful  in  tracking  summary  statistics
over time. In this exercise, you'll calculate the cumulative sum and cumulative
max of a department's weekly sales, which will allow you to identify what the total
sales were so far as well as what the highest weekly sales were so far.

A DataFrame called sales_1_1 has been created for you, which contains the sales data
for department 1 of store 1. pandas is loaded as pd.

Instructions:

- Sort the rows of sales_1_1 by the date column in ascending order.

- Get the cumulative sum of weekly_sales and add it as a new column of sales_1_1
  called cum_weekly_sales.

- Get the cumulative maximum of weekly_sales, and add it as a column called cum_max_sales.

- Print the date, weekly_sales, cum_weekly_sales, and cum_max_sales columns.
-----------------------------------------------------------------------------------------------------------------
sales_1_1.head()

   store type  department       date  weekly_sales  is_holiday  temperature_c  fuel_price_usd_per_l  unemployment
5      1    A           1 2010-07-02      16333.14       False         27.172                 0.705         7.787
0      1    A           1 2010-02-05      24924.50       False          5.728                 0.679         8.106
4      1    A           1 2010-06-04      17558.09       False         27.050                 0.715         7.808
9      1    A           1 2010-11-05      34238.88       False         14.856                 0.710         7.838
8      1    A           1 2010-10-01      20094.19       False         22.161                 0.688         7.838
-----------------------------------------------------------------------------------------------------------------
'''
# Sort sales_1_1 by date
sales_1_1 = sales_1_1.sort_values("date")

# Get the cumulative sum of weekly_sales, add as cum_weekly_sales col
sales_1_1["cum_weekly_sales"] = sales_1_1['weekly_sales'].cumsum()

# Get the cumulative max of weekly_sales, add as cum_max_sales col
sales_1_1["cum_max_sales"] = sales_1_1['weekly_sales'].cummax()

# See the columns you calculated
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])