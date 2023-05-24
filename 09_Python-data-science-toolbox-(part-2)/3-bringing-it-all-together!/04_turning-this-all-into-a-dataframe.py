'''
04 - Turning this all into a DataFrame

You've zipped lists together, created a function to house your code, and even used  the  function in a 
list comprehension to generate a list of dictionaries. That was a lot of work and you did a great job!

You will now use of all these to convert the list of dictionaries into  a  pandas  DataFrame. You  will  see 
how convenient it is to generate a DataFrame from dictionaries with the DataFrame() function from the pandas 
package.

The lists2dict() function, feature_names list, and row_lists list have been preloaded for this exercise.

Go for it!

Instructions:

- To use the DataFrame() function you need, first import the pandas package with the alias pd.
- Create a DataFrame from the list of dictionaries in list_of_dicts by calling pd.DataFrame(). Assign the resulting
  DataFrame to df.
- Inspect the contents of df by printing the head of the DataFrame.
'''

# Import the pandas package
import pandas as pd

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Turn list of dicts into a DataFrame: df
df = pd.DataFrame(list_of_dicts)

# Print the head of the DataFrame
print(df.head())

'''
Output:

<script.py> output:
      CountryCode CountryName   IndicatorCode                                      IndicatorName               Value  Year
    0         ARB  Arab World     SP.ADO.TFRT  Adolescent fertility rate (births per 1,000 wo...  133.56090740552298  1960
    1         ARB  Arab World     SP.POP.DPND  Age dependency ratio (% of working-age populat...    87.7976011532547  1960
    2         ARB  Arab World  SP.POP.DPND.OL  Age dependency ratio, old (% of working-age po...   6.634579191565161  1960
    3         ARB  Arab World  SP.POP.DPND.YG  Age dependency ratio, young (% of working-age ...   81.02332950839141  1960
    4         ARB  Arab World  MS.MIL.XPRT.KD        Arms exports (SIPRI trend indicator values)           3000000.0  1960
'''