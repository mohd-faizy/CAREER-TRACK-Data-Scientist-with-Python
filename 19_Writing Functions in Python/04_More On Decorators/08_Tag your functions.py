'''
08 - Tag your functions

Tagging something means that you have given that thing one  or  more 
strings that act as labels. For instance, we  often  tag  emails  or 
photos so that we can search for them later. You've decided to write 
a decorator that will let you tag your functions with an arbitrary 
list of tags. You could use these tags for many things:

    -   Adding information about who has worked on the function, so a 
        user can look up who to ask if they run into trouble using it.

    -   Labeling functions as "experimental" so that users know that 
        the inputs and outputs might change in the future.

    -   Marking any functions that you plan to remove in a future version
        of the code.

    -  etc.

Instructions

- Define a new decorator, named decorator(), to return.
- Ensure the decorated function keeps its metadata.
- Call the function being decorated and return the result.
- Return the new decorator.
'''
from functools import wraps

def tag(*tags):
    # Define a new decorator, named "decorator", to return
    def decorator(func):
        # Ensure the decorated function keeps its metadata
        @wraps(func)
        def wrapper(*args, **kwargs):
        # Call the function being decorated and return the result
            return func(*args, **kwargs)
        wrapper.tags = tags
        return wrapper
    # Return the new decorator
    return decorator

@tag('test', 'this is a tag')
def foo():
    pass

print(foo.tags)

'''
With this new decorator, you can do some really interesting  things.  For 
instance, you could tag a bunch of image transforming functions,  and then 
write code that searches for all of the functions  that  transform  images 
and apply them, one after the other, on  a  given  input image. What other 
neat uses can you come up with for this decorator?
'''
