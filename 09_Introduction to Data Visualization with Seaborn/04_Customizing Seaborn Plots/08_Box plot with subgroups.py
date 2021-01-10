'''
08 - Box plot with subgroups

In this exercise, we'll look at the dataset containing  responses
from a survey given to young people. One of the questions asked of
the young people was: "Are you interested in  having pets?"  Let's
explore whether the distribution of ages of those  answering "yes"
tends to be higher or lower than those answering "no", controlling
for gender.

Instructions

- Set the color palette to "Blues".
- Add subgroups to color the box plots based on "Interested in Pets".
- Set the title of the FacetGrid object g to "Age of Those Interested 
  in Pets vs. Not".
- Make the plot display using a Matplotlib function.
'''
# Set palette to "Blues"
sns.set_palette("Blues")

# Adjust to add subgroups based on "Interested in Pets"
g = sns.catplot(x="Gender",
                y="Age", data=survey_data,
                kind="box", hue="Interested in Pets")

# Set title to "Age of Those Interested in Pets vs. Not"
g.fig.suptitle("Age of Those Interested in Pets vs. Not")

# Show plot
plt.show()
