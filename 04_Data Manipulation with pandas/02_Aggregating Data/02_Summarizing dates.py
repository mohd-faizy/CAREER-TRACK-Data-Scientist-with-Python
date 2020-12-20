'''
02 - Summarizing dates

Summary statistics can also be calculated on date columns
that have values with the data type datetime64. Some summary
statistics — like mean — don't make a ton of sense on dates,
but others are super helpful, for example, minimum and maximum,
which allow you to see what time range your data covers.

Instructions:

 - Print the maximum of the date column.
 - Print the minimum of the date column.
'''
# Import pandas using the alias pd
import pandas as pd
sales = pd.read_csv('content/wallmart_sales.csv')

# Print the maximum of the date column
print(sales['date'].max())

# Print the minimum of the date column
print(sales['date'].min())
