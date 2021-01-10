'''
05 - Omitting outliers

Now let's use the student_data dataset to  compare  the  distribution  of  final
grades ("G3") between students who have internet access at home  and  those  who
don't. To do this, we'll use the "internet" variable, which is a binary (yes/no)
indicator of whether the student has internet access at home.

Since internet may be less accessible in rural areas, we'll add subgroups based on
where the student lives. For this, we can use the "location" variable, which is an
indicator of whether a student lives in an urban ("Urban") or rural ("Rural") location.

Seaborn has already been imported as sns and matplotlib.pyplot has been imported as 
plt. As a reminder, you can omit outliers in box plots by setting the sym parameter
equal to an empty string ("").

Instructions:

- Use sns.catplot() to create a box plot with the student_data DataFrame, putting
  "internet" on the x-axis and "G3" on the y-axis.
- Add subgroups so each box plot is colored based on "location".
- Do not display the outliers.
'''
# Create a box plot with subgroups and omit the outliers
sns.catplot(x='internet',
            y='G3',
            data=student_data,
            kind='box',
            sym='',
            hue='location')

# Show plot
plt.show()
