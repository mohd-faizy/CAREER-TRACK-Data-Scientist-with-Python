'''
02 - NMF features of the Wikipedia articles

Now you will explore the NMF features you created in the previous exercise. 
A solution to the previous exercise has  been  pre-loaded,  so  the  array 
nmf_features is available. Also available is a list titles giving the title 
of each Wikipedia article.

When investigating the features, notice that for both actors, the NMF feature
3 has by far the highest value. This means that both articles are reconstructed
using mainly the 3rd NMF component. In the next video, you'll see why: NMF 
components represent topics (for instance, acting!).

INSTRUCTIONS

- Import pandas as pd.
- Create a DataFrame df from nmf_features using pd.DataFrame(). Set the index to 
  titles using index=titles.
- Use the .loc[] accessor of df to select the row with title 'Anne Hathaway', and print 
  the result. These are the NMF features for the article about the actress Anne Hathaway.
- Repeat the last step for 'Denzel Washington' (another actor).
'''
# Import pandas
import pandas as pd

# Create a pandas DataFrame: df
df = pd.DataFrame(nmf_features, index=titles)

# Print the row for 'Anne Hathaway'
print(df.loc['Anne Hathaway'])

# Print the row for 'Denzel Washington'
print(df.loc['Denzel Washington'])

'''
Notice that for both actors, the NMF feature 3 has by far the highest value. 
This means that both articles are reconstructed using  mainly  the  3rd  NMF 
component.

script.py

Light Mode
1234567891011
print(df.loc['Denzel Washington'])


Run Code

Submit Answer
IPython Shell
Slides


<script.py> output:
    0    0.003845
    1    0.000000
    2    0.000000
    3    0.575711
    4    0.000000
    5    0.000000
    Name: Anne Hathaway, dtype: float64
    0    0.000000
    1    0.005601
    2    0.000000
    3    0.422380
    4    0.000000
    5    0.000000
    Name: Denzel Washington, dtype: float64
'''
