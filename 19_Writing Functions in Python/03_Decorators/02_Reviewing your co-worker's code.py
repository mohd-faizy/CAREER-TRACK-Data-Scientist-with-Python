'''
02 - Reviewing your co-worker's code

Your co-worker is asking you to review some code that  they've  written 
and give them some tips on how to get it ready for production. You know 
that having a docstring is considered best practice for   maintainable, 
reusable functions, so as a sanity check you decide    to   run    this 
has_docstring() function on all of their functions.

```python
def has_docstring(func):
  """Check to see if the function 
  `func` has a docstring.

  Args:
    func (callable): A function.

  Returns:
    bool
  """
  return func.__doc__ is not 
```

Instructions:

- Call has_docstring() on your co-worker's load_and_plot_data() function.
- Check if the function as_2D() has a docstring.
- Check if the function log_product() has a docstring.
'''
# Call has_docstring() on the load_and_plot_data() function
ok = has_docstring(load_and_plot_data)

if not ok:
  print("load_and_plot_data() doesn't have a docstring!")
else:
  print("load_and_plot_data() looks ok")

# Call has_docstring() on the as_2D() function
ok = has_docstring(as_2D)

if not ok:
  print("as_2D() doesn't have a docstring!")
else:
  print("as_2D() looks ok")


# Call has_docstring() on the log_product() function
ok = has_docstring(log_product)

if not ok:
  print("log_product() doesn't have a docstring!")
else:
  print("log_product() looks ok")


'''
we have discovered that our co-worker forgot to write a docstring 
for log_product(). You have learned enough about best practices to 
tell them how to fix it.

To pass a function  as  an  argument  to  another  function,  you  had  to 
determine which one you were calling and which one  you  were  referencing. 
Keeping those straight will be important as we dig deeper into this chapter. 
From the function names  can  you  think of any other advice you might give 
your co-worker about their functions?
'''
