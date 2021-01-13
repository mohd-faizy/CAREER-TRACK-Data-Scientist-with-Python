'''
09 - Turning a webpage into data using BeautifulSoup: getting the hyperlinks

In this exercise, you'll figure out how to extract the URLs of the hyperlinks from 
the BDFL's webpage. In the process, you'll become close friends with the soup method 
find_all().

Instructions:

- Use the method find_all() to find all hyperlinks in soup, remembering that hyperlinks 
  are defined by the HTML tag <a> but passed to find_all() without angle brackets; store 
  the result in the variable a_tags.

- The variable a_tags is a results set: your job now is to enumerate over it, using a for
  loop and to print the actual URLs of the hyperlinks; to do this, for every element link
  in a_tags, you want to print() link.get('href').
'''
# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Print the title of Guido's webpage
print(soup.title)

# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all('a')

# Print the URLs to the shell
for link in a_tags:
    print(link.get('href'))

'''
Output
<script.py> output:
    <title>Guido's Personal Home Page</title>
    pics.html
    pics.html
    http://www.washingtonpost.com/wp-srv/business/longterm/microsoft/stories/1998/raymond120398.htm
    images/df20000406.jpg
    http://neopythonic.blogspot.com/2016/04/kings-day-speech.html
    http://www.python.org
    Resume.html
    Publications.html
    bio.html
    http://legacy.python.org/doc/essays/
    http://legacy.python.org/doc/essays/ppt/
    interviews.html
    pics.html
    http://neopythonic.blogspot.com
    http://www.artima.com/weblogs/index.jsp?blogger=12088
    https://twitter.com/gvanrossum
    Resume.html
    guido.au
    http://legacy.python.org/doc/essays/
    images/license.jpg
    http://www.cnpbagwell.com/audio-faq
    http://sox.sourceforge.net/
    images/internetdog.gif
'''
