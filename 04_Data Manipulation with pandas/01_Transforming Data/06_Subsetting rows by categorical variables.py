'''
06 - Subsetting rows by categorical variables

Subsetting data based on a categorical variable often involves using the
"or" operator (|) to select rows from multiple categories. This can get tedious
when you want all states in one of three different regions, for example. Instead,
use the .isin() method, which will allow you to tackle this problem by writing one
condition instead of three separate ones.

colors = ["brown", "black", "tan"]
condition = dogs["color"].isin(colors)
dogs[condition]

Instructions:

1. Filter homelessness for cases where the USA census region is "South Atlantic"
   or it is "Mid-Atlantic", assigning to south_mid_atlantic. View the printed result.

2. Filter homelessness for cases where the USA census state is in the list of Mojave
states, canu, assigning to mojave_homelessness. View the printed result.
 
'''
# Import pandas using the alias pd
import pandas as pd
homelessness = pd.read_csv('content/homelessness.csv')

# Subset for rows in South Atlantic or Mid-Atlantic regions
# df[(df["col"] == "value_1") | (df["col"] == "value_2")]
south_mid_atlantic = homelessness[(homelessness['region'] == 'South Atlantic') | (
    homelessness['region'] == 'Mid-Atlantic')]

# See the result
print(south_mid_atlantic)

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
# df[df["col"].isin(["value_1", "value_2"])]
mojave_homelessness = homelessness[homelessness["state"].isin(canu)]

# See the result
print(mojave_homelessness)
