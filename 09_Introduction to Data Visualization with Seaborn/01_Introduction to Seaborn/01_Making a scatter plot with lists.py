'''
01 - Making a scatter plot with 

In this exercise, we'll use a dataset that contains information about 
227 countries. This dataset has lots of interesting information on each 
country, such as the country's birth rates, death rates, and its gross 
domestic product (GDP). GDP is the value of all the goods and services 
produced in a year, expressed as dollars per person.

We've created three lists of data from this dataset to get you started. 
gdp is a list that contains the value of GDP per country, expressed as 
dollars per person. phones is a list of the number of mobile phones per 
1,000 people in that country. Finally, percent_literate is a list that 
contains the percent of each country's population that can read and write.

Instructions:

- Import Matplotlib and Seaborn using the standard naming convention.
- Create a scatter plot of GDP (gdp) vs. number of phones per 1000 people (phones).
- Display the plot.
- Change the scatter plot so it displays the percent of the population that can read
  and write (percent_literate) on the y-axis.

'''
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
#sns.scatterplot(x=gdp, y=phones)

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=percent_literate)

# Show plot
plt.show()
