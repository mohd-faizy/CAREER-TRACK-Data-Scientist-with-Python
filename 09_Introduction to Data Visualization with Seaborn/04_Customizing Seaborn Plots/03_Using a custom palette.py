'''
03 - Using a custom palette

So far, we've looked  at several  things  in the dataset  of  survey  responses 
from young  people, including  their internet usage, how often they  listen  to 
their parents, and how many of  them  report feeling lonely. However, one thing 
we haven't done is a basic summary of the type of people answering this survey, 
including their age and gender. Providing these basic summaries is always a good 
practice when dealing with an unfamiliar dataset.

The code provided will create a box plot showing the distribution of ages for male
versus female respondents. Let's adjust the code to customize the appearance, this 
time using a custom color palette.

We've already imported Seaborn as sns and matplotlib.pyplot as plt.

Instructions

- Set the style to "darkgrid".
- Set a custom color palette with the hex color codes "#39A7D0" and "#36ADA4".
'''
# Set the style to "darkgrid"
sns.set_style("darkgrid")
# Set a custom color palette
custom_palette = ["#39A7D0", "#36ADA4"]
sns.set_palette(custom_palette)

# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age",
            data=survey_data, kind="box")

# Show plot
plt.show()
