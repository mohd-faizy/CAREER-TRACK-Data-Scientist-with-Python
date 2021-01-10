'''
09 - Bar plot with subgroups and subplots

In this exercise, we'll return to our young people survey dataset
and investigate whether the proportion of people who  like  techno
music ("Likes Techno") varies by their gender ("Gender") or where
they live ("Village - town"). This exercise will give us an opportunity
to practice the many things we've learned throughout this course!

We've already imported Seaborn as sns and matplotlib.pyplot as plt.

Instructions

- Set the figure style to "dark".
- Adjust the bar plot code to add subplots based on  "Gender",  arranged
  in columns.
- Add the title "Percentage of Young People Who  Like  Techno"  to  this
  FacetGrid plot.
- Label the x-axis "Location of Residence" and y-axis "% Who Like Techno".
'''
# Set the figure style to "dark"
sns.set_style("dark")

# Adjust to add subplots per gender
g = sns.catplot(x="Village - town", y="Likes Techno",
                data=survey_data, kind="bar",
                col="Gender")

# Add title and axis labels
g.fig.suptitle("Percentage of Young People Who Like Techno", y=1.02)
g.set(xlabel="Location of Residence",
      ylabel="% Who Like Techno")

# Show plot
plt.show()
