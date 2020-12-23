'''
04 - Price of conventional vs. organic avocados:

Creating multiple plots for different subsets of data allows you to compare
groups. In this exercise, you'll create multiple histograms to compare the prices
of conventional and organic avocados.

matplotlib.pyplot has been imported as plt and pandas has been imported as pd.

Instructions 1/3

- Subset avocados for the conventional type, and the average price column. Create a histogram.
- Create a histogram of avg_price for organic type avocados.
- Add a legend to your plot, with the names "conventional" and "organic".
- Show your plot.
--------------------------------------------------------------
avocados.head()

         date          type  year  avg_price   size    nb_sold
0  2015-12-27  conventional  2015       0.95  small  9.627e+06
1  2015-12-20  conventional  2015       0.98  small  8.710e+06
2  2015-12-13  conventional  2015       0.93  small  9.855e+06
3  2015-12-06  conventional  2015       0.89  small  9.405e+06
4  2015-11-29  conventional  2015       0.99  small  8.095e+06
---------------------------------------------------------------
'''
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Histogram of conventional avg_price
avocados[avocados['type'] == 'conventional']['avg_price'].hist()

# Histogram of organic avg_price
avocados[avocados['type'] == 'organic']['avg_price'].hist()

# Add a legend
plt.legend(['conventional', 'organic'])

# Show the plot
plt.show()
