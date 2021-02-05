'''
03 - Preserving docstrings when decorating functions

Your friend has come to you with a  problem. They've  written  some 
nifty decorators and added them to the functions in the open-source 
library they've been working on. However, they  were  running  some 
tests and discovered that all of the docstrings  have  mysteriously 
disappeared from their decorated functions. Show your friend how to 
preserve docstrings and other metadata when writing decorators.

Instructions:

- Decorate print_sum() with the add_hello() decorator to replicate the 
  issue that your friend saw - that the docstring disappears.

- To show your friend that they are printing the wrapper() function's 
  docstring, not the print_sum() docstring, add the following docstring 
  to wrapper():

  """Print 'hello' and then call the decorated function."""

- Import a function that will allow you to add the metadata from print_sum() 
  to the decorated version of print_sum().

- Finally, decorate wrapper() so that the metadata from func() is preserved 
  in the new decorated function.
'''
from functools import wraps

def add_hello(func):
    # Decorate wrapper() so that it keeps func()'s metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Print 'hello' and then call the decorated function."""
        print('Hello')
        return func(*args, **kwargs)
    return wrapper

@add_hello
def print_sum(a, b):
    """Adds two numbers and prints the sum"""
    print(a + b)

print_sum(10, 20)
print(print_sum.__doc__)

'''<script.py> output:
    Hello
    30
    Adds two numbers and prints the sum

That's a wrap! Your friend was concerned that they couldn't  print  the  docstrings  of 
their functions. They now realize that the strange behavior they were seeing was caused 
by the fact that they were accidentally printing the wrapper() docstring instead of the 
docstring of the original function. After adding @wraps(func) to all of their decorators, 
they see that the docstrings are back where they expect them to be.
'''
