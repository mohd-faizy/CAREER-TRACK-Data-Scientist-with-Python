'''
03 - Avocado supply and demand:

Scatter plots are ideal for visualizing relationships between numerical
variables. In this exercise, you'll compare the number of avocados sold
to average price and see if they're at all related. If they're related,
you may be able to use one number to predict the other.

Instructions:

- Create a scatter plot with nb_sold on the x-axis and avg_price on the y-axis.
  Title it "Number of avocados sold vs. average price".

- Show the plot.
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

# Scatter plot of nb_sold vs avg_price with title
avocados.plot(x='nb_sold', y='avg_price', kind='scatter',
              title="Number of avocados sold vs. average price")

# Show the plot
plt.show()
