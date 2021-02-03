'''
02 - Retrieving docstrings

You and a group of friends are working on building an amazing      new 
Python IDE (integrated development environment -- like         PyCharm, 
Spyder, Eclipse, Visual Studio, etc.). The team wants to add a feature 
that displays a tooltip with a function's docstring whenever the  user 
starts typing the function name. That way, the user doesn't have to go 
elsewhere to look up the documentation for the function they are trying 
to use. You've been asked to complete the build_tooltip() function that 
retrieves a docstring from an arbitrary function.

Note that in Python, you can pass a function as an argument to  another 
function. I'll talk more about this in chapter 3, but it will be useful 
to keep in mind for this exercise.
--------------------------------------------------------------------------
Instructions: 1/3
--------------------------------------------------------------------------
- Begin by getting the docstring for the function count_letter(). Use an 
attribute of the count_letter() function.
'''
# Get the docstring with an attribute of count_letter()
docstring = count_letter.__doc__

border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))

'''
--------------------------------------------------------------------------
Instructions: 2/3
--------------------------------------------------------------------------
- Now use a function from the inspect module to get a     better-formatted 
  version of count_letter()'s docstring.
'''
import inspect

# Get the docstring with a function from the inspect module
docstring = inspect.getdoc(count_letter)

border = '#' * 28
print('{}\n{}\n{}'.format(border, docstring, border))

'''
--------------------------------------------------------------------------
Instructions: 3/3
--------------------------------------------------------------------------
- Use the inspect module again to get the docstring for any function being 
  passed to the build_tooltip() function.
'''


def build_tooltip(function):
  """Create a tooltip for any function that shows the 
  function's docstring.
  
  Args:
    function (callable): The function we want a tooltip for.
    
  Returns:
    str
  """
  # Use 'inspect' to get the docstring
  docstring = inspect.getdoc(function)
  border = '#' * 28
  return '{}\n{}\n{}'.format(border, docstring, border)


print(build_tooltip(count_letter))
print(build_tooltip(range))
print(build_tooltip(print))
