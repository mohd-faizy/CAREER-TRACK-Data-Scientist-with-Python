'''
09 - Importing Stata files

Here, you'll gain expertise in importing Stata files as DataFrames using
the pd.read_stata() function from pandas. The last exercise's file,
'disarea.dta', is still in your working directory.

Instructions:

- Use pd.read_stata() to load the file 'disarea.dta' into the DataFrame df.
- Print the head of the DataFrame df.
- Visualize your results by plotting a histogram of the column disa10.
  We’ve already provided this code for you, so just run it!
'''
# Import matplotlib
import matplotlib.pyplot as plt

# Import pandas
import pandas as pd

# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('disarea.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of coutries')
plt.show()


'''
df.head()
---------------------------------------------------------------------------------------------------
<script.py> output:
      wbcode               country  disa1  disa2  disa3  ...  disa21  disa22  disa23  disa24  disa25
    0    AFG           Afghanistan   0.00   0.00   0.76  ...     0.0    0.00    0.02    0.00    0.00
    1    AGO                Angola   0.32   0.02   0.56  ...     0.0    0.99    0.98    0.61    0.00
    2    ALB               Albania   0.00   0.00   0.02  ...     0.0    0.00    0.00    0.00    0.16
    3    ARE  United Arab Emirates   0.00   0.00   0.00  ...     0.0    0.00    0.00    0.00    0.00
    4    ARG             Argentina   0.00   0.24   0.24  ...     0.0    0.00    0.01    0.00    0.11
    
    [5 rows x 27 columns]
--------------------------------------------------------------------------------------------------- 
'''
