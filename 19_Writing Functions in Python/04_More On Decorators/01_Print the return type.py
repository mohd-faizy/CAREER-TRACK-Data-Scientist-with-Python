'''
01 - Print the return type

You are debugging a package that  you've  been  working  on  with  your 
friends. Something weird is happening  with  the  data  being  returned 
from one of your functions, but you're not  even  sure  which  function 
is causing the trouble. You know that sometimes  bugs  can  sneak  into 
your  code when you are expecting a function to return  one thing,  and 
it returns something different. For instance, if you expect a  function 
to return a numpy array, but it returns a list, you can get  unexpected 
behavior. To ensure this is not what is causing the trouble, you decide 
to write a decorator, print_return_type(), that will print out the type 
of the variable that gets returned from every call of any function it is 
decorating.

Instructions

- Create a nested function, wrapper(), that will become the new decorated 
  function.
- Call the function being decorated.
- Return the new decorated function.
'''
def print_return_type(func):
    # Define wrapper(), the decorated function
    def wrapper(*args, **kwargs):
    # Call the function being decorated
        result = func(*args, **kwargs)
        print('{}() returned type {}'.format(
            func.__name__, type(result)
        ))
        return result
    # Return the decorated function
    return wrapper

@print_return_type
def foo(value):
  return value

print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))

'''
Decorator helps you examine the results of your functions at runtime. Now you can 
apply this decorator to every function in the package you are developing and  run 
your scripts. Being able to examine the types of your return values will help you 
understand what is happening and will hopefully help you find the bug.
'''
