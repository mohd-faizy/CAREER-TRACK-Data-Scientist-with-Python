'''
01 - The number of cats

You are working on a natural language processing project to determine 
what makes great writers so great. Your current hypothesis is    that 
great writers talk about cats a lot. To prove it, you want to   count 
the number of times the word "cat" appears in "Alice's Adventures  in 
Wonderland" by Lewis Carroll. You have already downloaded a text file, 
alice.txt, with the entire contents of this great book.

Instructions:

- Use the open() context manager to open alice.txt and assign the file 
  to the file variable.
'''
# Open "alice.txt" and assign the file to "file"
with open('alice.txt') as file:
  text = file.read()

n = 0
for word in text.split():
  if word.lower() in ['cat', 'cats']:
    n += 1

print('Lewis Carroll uses the word "cat" {} times'.format(n))

'''
<script.py> output:
    Lewis Carroll uses the word "cat" 24 times
'''
