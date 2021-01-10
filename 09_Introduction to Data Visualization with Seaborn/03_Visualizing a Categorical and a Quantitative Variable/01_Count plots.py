'''
01 - Count plots

In this exercise, we'll return to exploring our  dataset that 
contains the responses to a survey sent out to  young  people. 
We might suspect that young people spend a lot of time on the 
internet, but how much do they report using the internet each 
day? Let's use a count plot to break down the number of survey 
responses in each category and then explore whether it changes 
based on age.

As a reminder, to create a count plot, we'll use  the  catplot()
function and specify the name of  the  categorical  variable  to 
count (x=____), the Pandas DataFrame to use (data=____), and the
type of plot (kind="count").

Seaborn has been imported as sns and matplotlib.pyplot  has  been 
imported as plt.

Instructions 1/3

- Use sns.catplot() to create a count plot using the survey_data 
  DataFrame with "Internet usage" on the x-axis.
'''
# Create count plot of internet usage
sns.catplot(x='Internet usage',
            data=survey_data,
            kind='count')

# Show plot
plt.show()

'''
Instructions 2/3

- Make the bars horizontal instead of vertical.
'''
# Change the orientation of the plot
sns.catplot(y="Internet usage",
            data=survey_data,
            kind="count")

# Show plot
plt.show()


'''
Instructions 3/3

- Create column subplots based on "Age Category", which separates
  respondents into those that are younger than 21 vs. 21 and older.
'''
# Create column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count", col='Age Category')

# Show plot
plt.show()
