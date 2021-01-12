'''
13 - Customizing your pandas import

The pandas package is also great at dealing with many  of the  issues  you  will
encounter when importing data as a data  scientist,  such  as comments occurring
in flat files, empty lines and missing values. Note that missing values are also
commonly referred to as NA or NaN. To  wrap  up this chapter, you're now going to
import a slightly corrupted copy of the Titanic dataset titanic_corrupt.txt, which

    - contains comments after the character '#'
    
    - is tab-delimited.

Instructions:

- Complete the `sep` (the pandas version of delim), comment and na_values arguments of
  pd.read_csv(). comment takes characters that comments occur after in the file, which
  in this case is '#'. na_values takes a list of strings to recognize as  NA/NaN,  in
  this case the string 'Nothing'.

- Execute the rest of the code to print the head of the resulting DataFrame and plot
  the histogram of the 'Age' of passengers aboard the Titanic.
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Assign filename: file
file = 'titanic_corrupt.txt'

# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values='Nothing')

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()


'''
data.head()
---------------------------------------------------------------------------------------------------------
      PassengerId  Survived  Pclass     Sex   Age  ...  Parch            Ticket    Fare  Cabin Embarked
    0            1         0       3    male  22.0  ...      0         A/5 21171   7.250    NaN       S 
    1            2         1       1  female  38.0  ...      0          PC 17599     NaN    NaN      NaN
    2            3         1       3  female  26.0  ...      0  STON/O2. 3101282   7.925    NaN        S
    3            4         1       1  female  35.0  ...      0            113803  53.100   C123        S
    4            5         0       3    male  35.0  ...      0            373450   8.050    NaN        S
    
    [5 rows x 11 columns]
---------------------------------------------------------------------------------------------------------
'''
