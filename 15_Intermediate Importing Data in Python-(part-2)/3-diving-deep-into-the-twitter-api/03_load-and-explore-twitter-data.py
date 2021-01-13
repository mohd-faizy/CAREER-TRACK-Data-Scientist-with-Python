'''
03-Load and explore your Twitter data

Now that you've got your Twitter data sitting locally in a text file, it's time 
to explore it! This is what you'll do in the next few interactive exercises. In 
this exercise, you'll read the Twitter data into a list: tweets_data.

Be aware that this is real data from Twitter and as such there is always a risk 
that it may contain profanity or other offensive content (in this exercise, and 
any following exercises that also use real Twitter data).

Instructions

- Assign the filename 'tweets.txt' to the variable tweets_data_path.

- Initialize tweets_data as an empty list to store the tweets in.

- Within the for loop initiated by for line in tweets_file:, load each tweet into
  a variable, tweet, using json.loads(), then append tweet to tweets_data using the 
  append() method.
  
- Hit submit and check out the keys of the first tweet dictionary printed to the shell.
'''
# Import package
import json

# String of path to file: tweets_data_path
tweets_data_path = 'tweets.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data = []

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())

'''
Output
<script.py> output:
    dict_keys(['in_reply_to_user_id', 'created_at', 'filter_level', 'truncated', 'possibly_sensitive', 'timestamp_ms', 'user', 'text', 'extended_entities', 'in_reply_to_status_id', 'entities', 'favorited', 'retweeted', 'is_quote_status', 'id', 'favorite_count', 'retweeted_status', 'in_reply_to_status_id_str', 'in_reply_to_user_id_str', 'id_str', 'in_reply_to_screen_name', 'coordinates', 'lang', 'place', 'contributors', 'geo', 'retweet_count', 'source'])
'''
