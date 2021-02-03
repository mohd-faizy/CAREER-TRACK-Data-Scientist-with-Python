'''
01 - Crafting a docstring

You've decided to write the world's greatest  open-source  natural  language 
processing Python package. It will revolutionize working with free-form text, 
the way numpy did for arrays, pandas did for tabular data, and scikit-learn 
did for machine learning.

The first function you write is count_letter(). It takes a string  and  a  single 
letter and returns the number of times the letter appears in the string. You want 
the users of your open-source package to be able to understand how this  function 
works easily, so you will need to give it a docstring. Build up a Google Style 
docstring for this function by following these steps.

Instructions:

- Copy the following string and add it as the docstring for the function: Count the 
  number of times `letter` appears in `content`.
- Now add the arguments section, using the Google style for docstrings. Use  str  to 
  indicate a string. 
- Add a returns section that informs the user the return value is an int.
- Finally, add some information about the ValueError that gets raised when the arguments 
  aren't correct.
'''
def count_letter(content, letter):
  """Count the number of times `letter` appears in `content`.

  Args:
    content (str): The string to search.
    letter (str): The letter to search for.

  Returns:
    int

  # Add a section detailing what errors might be raised
  Raises:
    ValueError: If `letter` is not a one-character string.
  """
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('`letter` must be a single character string.')
  return len([char for char in content if char == letter])


