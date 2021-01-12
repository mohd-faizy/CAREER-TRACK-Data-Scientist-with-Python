'''
05 - Printing HTTP request results in Python using urllib

You have just packaged and sent a GET request to "https://campus.datacamp.com/courses/1606/4135?ex=2"
and then caught the response. You saw that such a response is a http.client.HTTPResponse object. The 
question remains: what can you do with this response?

Well, as it came from an HTML page, you could read it to extract the HTML and, in fact, such a 
http.client.HTTPResponse object has an associated read() method. In this exercise, you'll build 
on your previous great work to extract the response and print the HTML.

Instructions

- Send the request and catch the response in the variable response with the function urlopen(), as 
  in the previous exercise.
- Extract the response using the read() method and store the result in the variable html.
- Print the string html.
- Hit submit to perform all of the above and to close the response: be tidy!
'''
# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "http://www.datacamp.com/teach/documentation"

# This packages the request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Extract the response: html
html = response.read()

# Print the html
print(html)

# Be polite and close the response!
response.close()
