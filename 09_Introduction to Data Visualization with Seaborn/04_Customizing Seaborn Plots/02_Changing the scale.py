'''
02 - Changing the scale

In this exercise, we'll  continue  to  look at  the  dataset  containing 
responses from a survey of young people. Does the  percentage  of  people
reporting that they feel lonely vary depending on  how many siblings they
have? Let's find out using a bar plot, while also exploring Seaborn's four
different plot scales ("contexts").

We've already imported Seaborn as sns and matplotlib.pyplot as plt.

Instructions:

- Set the scale ("context") to "paper", which is the smallest of the scale options.
- Change the context to "notebook" to increase the scale.
- Change the context to "talk" to increase the scale.
- Change the context to "poster", which is the largest scale available.
'''
# Set the context
sns.set_context("paper")
#sns.set_context("notebook")
#sns.set_context("talk")
#sns.set_context("poster")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()
