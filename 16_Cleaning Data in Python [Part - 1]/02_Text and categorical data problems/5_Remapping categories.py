'''
5 - Remapping categories

To better understand survey respondents from airlines, you want to find out if
there is a relationship between certain responses and the day of the week and 
wait time at the gate.

The airlines DataFrame contains the day and wait_min columns, which are categorical and 
numerical respectively. The day column contains the exact day a flight took place,  and 
wait_min contains the amount of minutes it took travelers to wait at the gate. To  make 
your analysis easier, you want to create two new categorical variables:

    - wait_type: 'short' for 0-60 min, 'medium' for 60-180 and long for 180+
    - day_week: 'weekday' if day is in the weekday, 'weekend' if day is in the weekend.

The pandas and numpy packages have been imported as pd and np. Let's create some new 
categorical data!

Instructions

- Create the ranges and labels for the wait_type column mentioned in the description above.
- Create the wait_type column by from wait_min by using pd.cut(), while inputting label_ranges
  and label_names in the correct arguments.
- Create the mapping dictionary mapping weekdays to 'weekday' and weekend days to 'weekend'.
- Create the day_week column by using .replace().
'''
# Create ranges for categories
label_ranges = [0, 60, 180, np.inf]
label_names = ['short', 'medium', 'long']

# Create wait_type column
airlines['wait_type'] = pd.cut(airlines['wait_min'], bins=label_ranges,
                               labels=label_names)

# Create mappings and replace
mappings = {'Monday': 'weekday', 'Tuesday': 'weekday', 'Wednesday': 'weekday',
            'Thursday': 'weekday', 'Friday': 'weekday',
            'Saturday': 'weekend', 'Sunday': 'weekend'}

airlines['day_week'] = airlines['day'].replace(mappings)


'''
Note:
----------------------------------------------------------------------
we just created two new categorical variables, that when combined with 
other columns, could produce really interesting analysis. Don't forget, 
we can always use an assert statement to check our changes passed.
----------------------------------------------------------------------
'''
