'''
05 - Hue and scatter plots

In the prior video, we learned how hue allows  us to  easily  make  subgroups 
within Seaborn plots. Let's try it out by exploring  data  from  students  in 
secondary school. We have a lot of information  about  each student like their 
age, where they live, their study habits and their extracurricular activities.

For now, we'll look at the relationship between the number  of  absences  they 
have in school and their final grade in  the  course,  segmented  by where the 
student lives (rural vs. urban area).

Instructions:

- Create a scatter plot with "absences" on the x-axis and final grade ("G3") on the 
  y-axis using the DataFrame student_data. Color the plot points based on "location" 
  (urban vs. rural).
'''
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of absences vs. final grade
sns.scatterplot(x='absences',
                y='G3',
                data=student_data,
                hue='location'
                )

# Show plot
plt.show()


'''
Instructions 2/2

- Make "Rural" appear before "Urban" in the plot legend.
'''
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change the legend order in the scatter plot
sns.scatterplot(x="absences", y="G3", 
                data=student_data, 
                hue="location",
                hue_order=['Rural', 'Urban'])

# Show plot
plt.show()