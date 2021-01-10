'''
08 - Point plots with subgroups

Let's  continue exploring  the  dataset of  students  in  secondary  school.
This time, we'll ask  the question:  is being  in  a  romantic  relationship
associated with higher or lower school attendance? And does this association
differ by which school the students attend? Let's find out using a point plot.

We've already imported Seaborn as sns and matplotlib.pyplot as plt.

Instructions 1/3

- Use sns.catplot() and the student_data DataFrame to create  a  point  plot  with 
  relationship status ("romantic") on the x-axis and number of absences ("absences")
  on the y-axis. Create subgroups based on the school that they attend ("school")
'''
# Create a point plot with subgroups
sns.catplot(x="romantic", y="absences",
            data=student_data,
            kind="point",
            hue='school'
            )

# Show plot
plt.show()

'''
Instructions 2/3

- Turn off the confidence intervals for the plot.
'''
# Turn off the confidence intervals for this plot
sns.catplot(x="romantic", y="absences",
            data=student_data,
            kind="point",
            hue="school",
            ci=None)

# Show plot
plt.show()

'''
Instructions 3/3

- Since there may be outliers of students with many absences, import the median function 
  from numpy and display the median number of absences instead of the average.

'''
# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None,
            estimator=median)

# Show plot
plt.show()