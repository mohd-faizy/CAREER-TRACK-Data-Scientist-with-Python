'''
06 - Adjusting the whiskers

In the lesson we saw that there  are  multiple  ways  to  define  the  whiskers
in a box plot. In this set of exercises, we'll continue to use the student_data
dataset to compare the distribution of final grades ("G3") between students who
are in a romantic relationship and those that are not. We'll use the  "romantic"
variable, which is a yes/no indicator of whether the student is  in  a  romantic
relationship.

Let's create a box plot to look at this relationship and try different ways to 
define the whiskers.

We've already imported Seaborn as sns and matplotlib.pyplot as plt.

Instructions 1/3

- Adjust the code to make the box plot whiskers to extend to 0.5 * IQR. Recall: the
  IQR is the interquartile range.
'''
# Set the whiskers to 0.5 * IQR
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=0.5)

# Show plot
plt.show()

'''
Instructions 2/3

- Change the code to set the whiskers to extend to the 5th and 95th percentiles.
'''
# Extend the whiskers to the 5th and 95th percentile
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[5, 95])

# Show plot
plt.show()

'''
Instructions 3/3

- Change the code to set the whiskers to extend to the min and max values.
'''
# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0, 100])

# Show plot
plt.show()
