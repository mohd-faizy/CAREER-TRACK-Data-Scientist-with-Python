'''
01 - Creating subplots with col and row

We've seen in prior exercises that students with  more  absences  ("absences")
tend to have lower final grades ("G3"). Does this relationship hold regardless 
of how much time students study each week?

To answer this, we'll look at the relationship between  the  number  of  absences  that 
a student has in school and their final grade in the course, creating separate subplots 
based on each student's weekly study time ("study_time").

Seaborn has been imported as sns and matplotlib.pyplot has been imported as plt.
'''
# 1 - Modify the code to use relplot instead of scatterplot
sns.relplot(x="absences", y="G3",
            data=student_data,
            kind="scatter")

# Show plot
plt.show()


# 2 - Modify the code to create one scatter plot for each level of the variable 
# "study_time", arranged in columns.
# Change to make subplots based on study time
sns.relplot(x="absences", y="G3",
            data=student_data,
            kind="scatter",
            col="study_time")

# Show plot
plt.show()

# 3 - Adapt your code to create one scatter plot for each level of a student's weekly 
# study time, this time arranged in rows.
# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3",
            data=student_data,
            kind="scatter",
            row="study_time")

# Show plot
plt.show()
