'''
04 - Measuring decorator overhead
----------------------------------------------------------------------------
Your boss wrote a decorator called  check_everything() that  they  think  is 
amazing, and they are insisting you use it on your function. However, you've 
noticed that when you use it to decorate your functions, it makes  them  run 
much slower. You need to convince your boss that the decorator is adding too 
much processing time to your function. To do this, you are going to  measure 
how long the decorated function takes to run and compare it to how long  the 
undecorated function would have taken to run. 

This is the decorator in question:
'''
def check_everything(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    check_inputs(*args, **kwargs)
    result = func(*args, **kwargs)
    check_outputs(result)
    return result
  return wrapper

'''
Instructions

- Call the original function instead of the decorated version by using  an  attribute  of 
  the function that the wraps() statement in your boss's decorator added to the decorated 
  function.
'''
import time

@check_everything
def duplicate(my_list):
    """Return a new list that repeats the input twice"""
    return my_list + my_list

t_start = time.time()
duplicated_list = duplicate(list(range(50)))
t_end = time.time()
decorated_time = t_end - t_start

t_start = time.time()
# Call the original function instead of the decorated one
duplicated_list = duplicate.__wrapped__(list(range(50)))
t_end = time.time()
undecorated_time = t_end - t_start

print('Decorated time: {:.5f}s'.format(decorated_time))
print('Undecorated time: {:.5f}s'.format(undecorated_time))

'''<script.py> output:
    Finished checking inputs
    Finished checking outputs
    Decorated time: 1.51170s
    Undecorated time: 0.00006s

Your function ran  approximately  10,000 times  faster  without  your 
boss's decorator. At least they were smart enough to add @wraps(func) 
to the nested wrapper() function so that you were able to access the 
original function. You should show them the results of this test. Be 
sure to ask for a raise while you're at it!
'''
