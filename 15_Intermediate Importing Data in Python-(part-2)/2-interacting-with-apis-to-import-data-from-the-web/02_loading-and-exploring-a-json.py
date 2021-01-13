'''
02 - Loading and exploring a JSON

Now that you know what a JSON is, you'll load one into your Python environment 
and explore it yourself. Here, you'll load the JSON  'a_movie.json'  into  the 
variable json_data, which will be a dictionary. You'll then explore  the  JSON 
contents by printing the key-value pairs of json_data to the shell.

Instructions:

- Load the JSON 'a_movie.json' into the variable json_data within  the  context 
  provided by the with statement. To do so, use the function json.load() within 
  the context manager.

- Use a for loop to print all key-value pairs in the dictionary json_data. Recall 
  that you can access a value in a dictionary using the syntax: dictionary[key]
'''
# Load JSON: json_data
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])
