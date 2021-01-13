'''
06 - JSON–from the web to Python

Wow, congrats! You've just queried your first API  programmatically  in  Python
and printed the text of the response to the shell. However, as you  know,  your
response is actually a JSON, so you can do one step better and decode the  JSON.
You can then print the key-value pairs of the resulting dictionary. That's what
you're going to do now

Instructions

- Pass the variable url to the requests.get() function in order to send the relevant 
  request and catch the response, assigning the resultant response message to the variable r.

- Apply the json() method to the response object r and store the resulting dictionary in the 
  variable json_data.
- Hit Submit Answer to print the key-value pairs of the dictionary json_data to the shell.
'''
# Import package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=ff21610b&t=social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])
