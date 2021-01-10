'''
07 - Customizing point plots

Let's continue to look at data from students in  secondary  school, this  time
using a point plot to answer the question: does the quality  of  the  student's
family relationship influence the number of absences the student has in school?
Here, we'll use the "famrel" variable, which describes the quality of a student's
family relationship from 1 (very bad) to 5 (very good).

As a reminder, to create a point plot, use the catplot() function and specify the
name of the categorical variable to put  on the x-axis (x=____), the name  of  the 
quantitative variable to summarize on the y-axis (y=____), the Pandas DataFrame to 
use (data=____), and the type of categorical plot (kind="point").

We've already imported Seaborn as sns and matplotlib.pyplot as plt.

Instructions 1/3

- Use sns.catplot() and the student_data DataFrame to create a point plot with 
  "famrel" on the x-axis and number of absences ("absences") on the y-axis.
'''
# Create a point plot of family relationship vs. absences
sns.catplot(x="famrel", y="absences",
            data=student_data,
            kind="point")

# Show plot
plt.show()

'''
Instructions 2/3

- Add "caps" to the end of the confidence intervals with size 0.2.
'''
# Add caps to the confidence interval
sns.catplot(x="famrel", y="absences",
            data=student_data,
            kind="point",
            capsize=0.2)

# Show plot
plt.show()


'''
Instructions 3/3

- Remove the lines joining the points in each category.
'''
# Remove the lines joining the points
sns.catplot(x="famrel", y="absences",
            data=student_data,
            kind="point",
            capsize=0.2,
            join=False)

# Show plot
plt.show()
