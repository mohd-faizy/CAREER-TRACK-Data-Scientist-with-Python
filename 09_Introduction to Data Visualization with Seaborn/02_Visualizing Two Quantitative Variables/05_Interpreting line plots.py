'''
05 - Interpreting line plots

In this exercise, we'll continue  to explore  Seaborn's  mpg  dataset, 
which contains one row per car model and includes information such  as 
the year the car was made, its fuel efficiency (measured in "miles per 
gallon" or "M.P.G"), and its country of origin (USA, Europe, or Japan).

How has the average miles per gallon achieved by these cars changed over 
time? Let's use line plots to find out!

Instructions 1/2

- Use relplot() and the mpg DataFrame to create a line plot with "model_year" 
  on the x-axis and "mpg" on the y-axis.
'''
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot
sns.relplot(x='model_year',
            y='mpg',
            data=mpg,
            kind='line')

# Show plot
plt.show()


'''
Instructions 2/2

Question:
Which of the following is NOT a correct interpretation of this line plot?

Possible Answers

- The average miles per gallon has generally increased over time.[X]

- The distribution of miles per gallon is smaller in 1973 compared to 1977.[Correct]

- The 95% confidence interval for average miles per gallon in 1970 is approximately 
  16 - 19.5 miles per gallon.[X]

- This plot assumes that our data is a random sample of all cars in the US, Europe, and Japan.[X]
'''
