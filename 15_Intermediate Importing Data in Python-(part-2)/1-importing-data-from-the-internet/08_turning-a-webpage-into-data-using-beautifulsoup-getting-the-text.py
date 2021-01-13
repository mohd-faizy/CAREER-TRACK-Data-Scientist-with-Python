'''
08 - Turning a webpage into data using BeautifulSoup: getting the text:

As promised, in the following exercises, you'll learn the basics of extracting 
information from HTML soup. In this exercise, you'll figure out how to extract the 
text from the BDFL's webpage, along with printing the webpage's title.

Instructions:

- In the sample code, the HTML response object html_doc has already been created: your 
  first task is to Soupify it using the function  BeautifulSoup()  and  to  assign  the 
  resulting soup to the variable soup.

- Extract the title from the HTML soup soup using the attribute title and assign the result 
  to guido_title.

- Print the title of Guido's webpage to the shell using the print() function.

- Extract the text from the HTML soup soup using the method get_text() and assign to guido_text.

- Hit submit to print the text from Guido's webpage to the shell.
'''
# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Get the title of Guido's webpage: guido_title
guido_title = soup.title

# Print the title of Guido's webpage to the shell
print(guido_title)

# Get Guido's text: guido_text
guido_text = soup.get_text()

# Print Guido's text to the shell
print(guido_text)

