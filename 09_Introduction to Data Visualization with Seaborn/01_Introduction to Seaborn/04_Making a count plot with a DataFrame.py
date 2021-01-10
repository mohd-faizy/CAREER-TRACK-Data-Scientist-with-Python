'''
04 - Making a count plot with a DataFrame

In this exercise, we'll look at the responses to a  survey  sent  out  to
young people. Our primary  question  here  is:   how  many  young  people 
surveyed report being scared  of  spiders? Survey participants were asked
to agree or disagree with the statement "I am afraid of spiders". Responses
vary from 1 to 5, where 1 is "Strongly disagree" and 5 is "Strongly agree".

To get you started, the filepath to the csv file with the survey data has been
assigned to the variable csv_filepath.

Note that because csv_filepath is a Python variable, you will not need to put
quotation marks around it when you read the csv.

Instructions:

- Import Matplotlib, Pandas, and Seaborn using the standard names.
- Create a DataFrame named df from the csv file located at csv_filepath.
- Use the countplot() function with the x= and data= arguments to create a count plot
  with the "Spiders" column values on the x-axis.
- Display the plot.
'''

# Import Matplotlib, Pandas, and Seaborn
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x='Spiders', data=df)

# Display the plot
plt.show()
