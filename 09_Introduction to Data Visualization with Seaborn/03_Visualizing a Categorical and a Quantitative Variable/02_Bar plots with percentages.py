'''
2 - Bar plots with percentages

Let's continue exploring the responses to a survey  sent  out  to  young  people.
The variable "Interested in Math" is True if the person reported being interested
or very interested in mathematics, and False otherwise. What percentage of young 
people report being interested in math, and does this vary based on gender? Let's 
use a bar plot to find out.

As a reminder, we'll create a bar plot using the catplot() function, providing the 
name of categorical variable to put on the x-axis (x=____), the name of the quantitative 
variable to summarize on the y-axis (y=____), the Pandas DataFrame to use (data=____), and 
the type of categorical plot (kind="bar").

Seaborn has been imported as sns and matplotlib.pyplot has been imported as plt.

Instructions:

- Use the survey_data DataFrame and sns.catplot() to create a bar plot with "Gender" on the 
  x-axis and "Interested in Math" on the y-axis.
'''
# Create a bar plot of interest in math, separated by gender
sns.catplot(x='Gender',
            y="Interested in Math",
            data=survey_data,
            kind="bar")

# Show plot
plt.show()
