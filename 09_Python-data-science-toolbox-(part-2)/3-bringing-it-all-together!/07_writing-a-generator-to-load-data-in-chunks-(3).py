'''
07 - Writing a generator to load data in chunks (3)


Great! You've just created a generator function that you can use to help you process large files.

Now let's use your generator function to process the World Bank dataset like you did previously.
You will process the file line by line, to create a dictionary of the counts of how many times each
country appears in a column in the dataset. For this exercise, however, you won't process just 1000
rows of data, you'll process the entire dataset!

The generator function read_large_file() and the csv file 'world_dev_ind.csv' are preloaded and
ready for your use. Go for it!

Instructions
-Bind the file 'world_dev_ind.csv' to file in the context manager with open().
-Complete the for loop so that it iterates over the generator from the call to read_large_file()
to process all the rows of the file.
'''
# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Iterate over the generator from read_large_file()
    for line in read_large_file(file):

        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

# Print
print(counts_dict)

'''
Output

<script.py> output:
    {'CountryName': 1, 'Arab World': 80, 'Caribbean small states': 77, 'Central Europe and the Baltics': 71, 'East Asia & Pacific (all income levels)': 122, 'East Asia & Pacific (developing only)': 123, 'Euro area': 119, 'Europe & Central Asia (all income levels)': 109, 'Europe & Central Asia (developing only)': 89, 'European Union': 116, 'Fragile and conflict affected situations': 76, 'Heavily indebted poor countries (HIPC)': 99, 'High income': 131, 'High income: nonOECD': 68, 'High income: OECD': 127, 'Latin America & Caribbean (all income levels)': 130, 'Latin America & Caribbean (developing only)': 133, 'Least developed countries: UN classification': 78, 'Low & middle income': 138, 'Low income': 80, 'Lower middle income': 126, 'Middle East & North Africa (all income levels)': 89, 'Middle East & North Africa (developing only)': 94, 'Middle income': 138, 'North America': 123, 'OECD members': 130, 'Other small states': 63, 'Pacific island small states': 66, 'Small states': 69, 'South Asia': 36}
'''
