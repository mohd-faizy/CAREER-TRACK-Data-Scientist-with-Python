'''
06 - Plotting your Twitter data

Now that you have the number of tweets that each candidate was mentioned 
in, you can plot a bar chart of this data. You'll use the statistical data
visualization library seaborn, which you may not have seen before, but we'll
guide you through. You'll first import seaborn as sns. You'll then construct 
a barplot of the data using sns.barplot, passing it two arguments:

a list of labels and
a list containing the variables you wish to plot (clinton, trump and so on.)
Hopefully, you'll see that Trump was unreasonably represented! We have already
run the previous exercise solutions in your environment.

Instructions:

- Import both matplotlib.pyplot and seaborn using the aliases plt and sns, respectively.

- Complete the arguments of sns.barplot:
        - The first argument should be the list of labels to appear on the x-axis (created in the
          previous step).

        - The second argument should be a list of the variables you wish to plot, as produced in 
          the previous exercise (i.e. a list containing clinton, trump, etc).
'''
# Import packages
import seaborn as sns
import matplotlib.pyplot as plt

# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']

# Plot histogram
ax = sns.barplot(cd, [clinton, trump, sanders, cruz])
ax.set(ylabel="count")
plt.show()
