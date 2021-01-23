'''
02 - Finding consistency

In this exercise and throughout this chapter, you'll be working with the 
airlines DataFrame which contains survey responses on the  San  Francisco 
Airport from airline customers.

The DataFrame contains flight metadata  such as the  airline,  the  destination, 
waiting times as well as answers to key questions regarding cleanliness, safety, 
and satisfaction. Another DataFrame named  categories  was  created,  containing 
all correct possible values for the survey columns.

In this exercise, you will use both of these DataFrames to find survey  answers
with inconsistent values, and drop them, effectively performing an outer and 
inner join  on both these DataFrames as seen in the video exercise. The pandas 
package has been imported as pd, and the `airlines` and `categories` DataFrames 
are in your environment.

Instructions 1/4

- Print the categories DataFrame and take a close look at all possible correct 
  categories of the survey columns.
- Print the unique values of the survey columns in airlines using the .unique()
  method.
'''
# Print categories DataFrame
print(categories)

# Print unique values of survey columns in airlines
print('Cleanliness: ', airlines['cleanliness'].unique(), "\n")
print('Safety: ',  airlines['safety'].unique(), "\n")
print('Satisfaction: ',  airlines['satisfaction'].unique(), "\n")

'''
<script.py> output:
------------------------------------------------------------------------------------------------
          cleanliness           safety          satisfaction
    0           Clean          Neutral        Very satisfied
    1         Average        Very safe               Neutral
    2  Somewhat clean    Somewhat safe    Somewhat satisfied
    3  Somewhat dirty      Very unsafe  Somewhat unsatisfied
    4           Dirty  Somewhat unsafe      Very unsatisfied
------------------------------------------------------------------------------------------------
    Cleanliness:  [Clean, Average, Unacceptable, Somewhat clean, Somewhat dirty, Dirty]
    Categories (6, object): [Clean, Average, Unacceptable, Somewhat clean, Somewhat dirty, Dirty] 
------------------------------------------------------------------------------------------------    
    Safety:  [Neutral, Very safe, Somewhat safe, Very unsafe, Somewhat unsafe]
    Categories (5, object): [Neutral, Very safe, Somewhat safe, Very unsafe, Somewhat unsafe] 
------------------------------------------------------------------------------------------------   
    Satisfaction:  [Very satisfied, Neutral, Somewhat satisfied, Somewhat unsatisfied, Very unsatisfied]
    Categories (5, object): [Very satisfied, Neutral, Somewhat satisfied, Somewhat unsatisfied,
                             Very unsatisfied] 
'''

'''
Instructions 2/4
Question:

Take a look at the output. Out of the cleanliness, safety and satisfaction columns, 
which one has an inconsistent category and what is it?

Possible Answers
- cleanliness because it has an Unacceptable category.[Correct]
- cleanliness because it has a Terribly dirty category.[X]
- satisfaction because it has a Very satisfied category.[X]
- safety because it has a Neutral category.[X]
'''
'''
Instructions 3/4

- Create a set out of the cleanliness column in airlines using set() and find the inconsistent
  category by finding the difference in the cleanliness column of categories.
- Find rows of airlines with a cleanliness value not in categories and print the output.
'''
# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])

# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# Print rows with inconsistent category
print(airlines[cat_clean_rows])

'''
       id        day           airline  destination  dest_region dest_size  \
4    2992  Wednesday          AMERICAN        MIAMI      East US       Hub   
18   2913     Friday  TURKISH AIRLINES     ISTANBUL  Middle East       Hub   
100  2321  Wednesday         SOUTHWEST  LOS ANGELES      West US       Hub   

    boarding_area   dept_time  wait_min   cleanliness         safety  \
4     Gates 50-59  2018-12-31     559.0  Unacceptable      Very safe   
18   Gates 91-102  2018-12-31     225.0  Unacceptable      Very safe   
100   Gates 20-39  2018-12-31     130.0  Unacceptable  Somewhat safe   

           satisfaction  
4    Somewhat satisfied  
18   Somewhat satisfied  
100  Somewhat satisfied  
'''

'''
Instructions 4/4

- Print the rows with the consistent categories of cleanliness only.
'''
# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])

# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# Print rows with inconsistent category
print(airlines[cat_clean_rows])

# Print rows with consistent categories only
print(airlines[~cat_clean_rows])


'''
  id       day      airline        destination    dest_region dest_size  \
0  1351   Tuesday  UNITED INTL             KANSAI           Asia       Hub   
1   373    Friday       ALASKA  SAN JOSE DEL CABO  Canada/Mexico     Small   
2  2820  Thursday        DELTA        LOS ANGELES        West US       Hub   
3  1157   Tuesday    SOUTHWEST        LOS ANGELES        West US       Hub   
5   634  Thursday       ALASKA             NEWARK        East US       Hub   

  boarding_area   dept_time  wait_min     cleanliness         safety  \
0  Gates 91-102  2018-12-31     115.0           Clean        Neutral   
1   Gates 50-59  2018-12-31     135.0           Clean      Very safe   
2   Gates 40-48  2018-12-31      70.0         Average  Somewhat safe   
3   Gates 20-39  2018-12-31     190.0           Clean      Very safe   
5   Gates 50-59  2018-12-31     140.0  Somewhat clean      Very safe   

         satisfaction  
0      Very satisfied  
1      Very satisfied  
2             Neutral  
3  Somewhat satisfied  
5      Very satisfied
'''