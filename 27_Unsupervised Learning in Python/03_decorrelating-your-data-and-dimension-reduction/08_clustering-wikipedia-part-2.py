'''
08 - Clustering Wikipedia part II

It is now time to put your pipeline from the previous exercise to work! You are given 
an array articles of tf-idf word-frequencies of some popular Wikipedia articles, and a 
list titles of their titles. Use your pipeline to cluster the Wikipedia articles.

A solution to the previous exercise has been pre-loaded for you, so a Pipeline pipeline 
chaining TruncatedSVD with KMeans is available.

Instructions

- Import pandas as pd.

- Fit the pipeline to the word-frequency array articles.

- Predict the cluster labels.

- Align the cluster labels with the list titles of article titles by creating a DataFrame df 
  with labels and titles as columns. This has been done for you.

- Use the .sort_values() method of df to sort the DataFrame by the 'label' column, and print 
  the result.

- Hit 'Submit Answer' and take a moment to investigate your amazing clustering of Wikipedia pages!
'''
# Import pandas
import pandas as pd

# Fit the pipeline to articles
pipeline.fit(articles)

# Calculate the cluster labels: labels
labels = pipeline.predict(articles)

# Create a DataFrame aligning labels and titles: df
df = pd.DataFrame({'label': labels, 'article': titles})

# Display df sorted by cluster label
print(df.sort_values('label'))


'''
<script.py> output:
        label                                        article
    59      0                                    Adam Levine
    57      0                          Red Hot Chili Peppers
    56      0                                       Skrillex
    55      0                                  Black Sabbath
    54      0                                 Arctic Monkeys
    53      0                                   Stevie Nicks
    52      0                                     The Wanted
    51      0                                     Nate Ruess
    50      0                                   Chad Kroeger
    58      0                                         Sepsis
    30      1                  France national football team
    31      1                              Cristiano Ronaldo
    32      1                                   Arsenal F.C.
    33      1                                 Radamel Falcao
    37      1                                       Football
    35      1                Colombia national football team
    36      1              2014 FIFA World Cup qualification
    38      1                                         Neymar
    39      1                                  Franck Ribéry
    34      1                             Zlatan Ibrahimović
    26      2                                     Mila Kunis
    28      2                                  Anne Hathaway
    27      2                                 Dakota Fanning
    25      2                                  Russell Crowe
    29      2                               Jennifer Aniston
    23      2                           Catherine Zeta-Jones
    22      2                              Denzel Washington
    21      2                             Michael Fassbender
    20      2                                 Angelina Jolie
    24      2                                   Jessica Biel
    10      3                                 Global warming
    11      3       Nationally Appropriate Mitigation Action
    13      3                               Connie Hedegaard
    14      3                                 Climate change
    12      3                                   Nigel Lawson
    16      3                                        350.org
    17      3  Greenhouse gas emissions by the United States
    18      3  2010 United Nations Climate Change Conference
    19      3  2007 United Nations Climate Change Conference
    15      3                                 Kyoto Protocol
    8       4                                        Firefox
    1       4                                 Alexa Internet
    2       4                              Internet Explorer
    3       4                                    HTTP cookie
    4       4                                  Google Search
    5       4                                         Tumblr
    6       4                    Hypertext Transfer Protocol
    7       4                                  Social search
    49      4                                       Lymphoma
    42      4                                    Doxycycline
    47      4                                          Fever
    46      4                                     Prednisone
    44      4                                           Gout
    43      4                                       Leukemia
    9       4                                       LinkedIn
    48      4                                     Gabapentin
    0       4                                       HTTP 404
    45      5                                    Hepatitis C
    41      5                                    Hepatitis B
    40      5                                    Tonsillitis
'''