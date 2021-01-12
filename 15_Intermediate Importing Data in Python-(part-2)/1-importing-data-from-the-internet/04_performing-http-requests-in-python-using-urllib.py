'''
04 - Performing HTTP requests in Python using urllib

Now that you know the basics behind HTTP GET requests,  it's  time  to  perform   some
of your own. In this interactive exercise, you will ping our very own DataCamp servers 
to perform a GET request to extract information from the first coding exercise of this
course, "https://campus.datacamp.com/courses/1606/4135?ex=2".

In the next exercise, you'll extract the HTML itself. Right now, however, you are going
 to package and send the request and then catch the response.

Instructions:

- Import the functions urlopen and Request from the subpackage urllib.request.

- Package the request to the url "https://campus.datacamp.com/courses/1606/4135?ex=2" using
  the function Request() and assign it to request.

- Send the request and catch the response in the variable response with the function urlopen().

- Run the rest of the code to see the datatype of response and to close the connection!
'''
# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "http://www.datacamp.com/teach/documentation"

# This packages the request: request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Print the datatype of response
print(type(response))

# Be polite and close the response!
response.close()

'''
<script.py> output:
    <class 'http.client.HTTPResponse'>
'''
