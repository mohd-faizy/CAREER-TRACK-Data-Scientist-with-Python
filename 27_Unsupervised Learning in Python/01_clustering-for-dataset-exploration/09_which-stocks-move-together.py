'''
09 - Which stocks move together?

In the previous exercise, you clustered companies by their daily  stock  price  movements. 
So which company have stock prices that tend to change in the same way? You'll now inspect 
the cluster labels from your clustering to find out.

Your solution to the previous exercise has already been run. Recall that you constructed  a 
Pipeline pipeline containing a KMeans model and fit it to the NumPy array movements of daily 
stock movements. In addition, a list companies of the company names is available.

Instructions:

- Import pandas as pd.
- Use the .predict() method of the pipeline to predict the labels for movements.
- Align the cluster labels with the list of company names companies by creating a 
  DataFrame df with labels and companies as columns. This has been done for you.
- Use the .sort_values() method of df to sort the DataFrame by the 'labels' column, 
  and print the result.
- Hit 'Submit Answer' and take a moment to see which companies are together in each cluster!!!
'''
# Import pandas
import pandas as pd

# Predict the cluster labels: labels
labels = pipeline.predict(movements)

# Create a DataFrame aligning labels and companies: df
df = pd.DataFrame({'labels': labels, 'companies': companies})

# Display df sorted by cluster label
print(df.sort_values('labels'))


'''
<script.py> output:
        labels                           companies
    59       0                               Yahoo
    15       0                                Ford
    35       0                            Navistar
    26       1                      JPMorgan Chase
    16       1                   General Electrics
    58       1                               Xerox
    11       1                               Cisco
    18       1                       Goldman Sachs
    20       1                          Home Depot
    5        1                     Bank of America
    3        1                    American express
    55       1                         Wells Fargo
    1        1                                 AIG
    38       2                               Pepsi
    40       2                      Procter Gamble
    28       2                           Coca Cola
    27       2                      Kimberly-Clark
    9        2                   Colgate-Palmolive
    54       3                            Walgreen
    36       3                    Northrop Grumman
    29       3                     Lookheed Martin
    4        3                              Boeing
    0        4                               Apple
    47       4                            Symantec
    33       4                           Microsoft
    32       4                                  3M
    31       4                           McDonalds
    30       4                          MasterCard
    50       4  Taiwan Semiconductor Manufacturing
    14       4                                Dell
    17       4                     Google/Alphabet
    24       4                               Intel
    23       4                                 IBM
    2        4                              Amazon
    51       4                   Texas instruments
    43       4                                 SAP
    45       5                                Sony
    48       5                              Toyota
    21       5                               Honda
    22       5                                  HP
    34       5                          Mitsubishi
    7        5                               Canon
    56       6                            Wal-Mart
    57       7                               Exxon
    44       7                        Schlumberger
    8        7                         Caterpillar
    10       7                      ConocoPhillips
    12       7                             Chevron
    13       7                   DuPont de Nemours
    53       7                       Valero Energy
    39       8                              Pfizer
    41       8                       Philip Morris
    25       8                   Johnson & Johnson
    49       9                               Total
    46       9                      Sanofi-Aventis
    37       9                            Novartis
    42       9                   Royal Dutch Shell
    19       9                     GlaxoSmithKline
    52       9                            Unilever
    6        9            British American Tobacco
'''
