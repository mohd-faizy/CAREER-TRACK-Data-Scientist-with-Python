'''
09 - Check the return type

Python's flexibility around data types  is usually  cited  as  one  of  the 
benefits of the language. It can  occasionally  cause  problems  though  if 
incorrect data types go unnoticed. You've decided that  in  order  to  make 
sure your code is doing exactly what you want it to do, you will explicitly 
check the return types of all of your functions and make sure they are what 
you expect them to be. To do that, you are going to create a decorator that 
checks that the return type of the decorated function is correct.

Note: assert(condition) is a function that you can use to test whether something
is true. If condition is True, this function doesn't do anything. If condition 
is False, this function raises an error. The type of error that it raises is called 
an AssertionError.

Instructions 1/2

- Start by completing the returns_dict() decorator so that it raises an AssertionError 
  if the return type of the decorated function is not a dictionary.
'''
def returns_dict(func):
    # Complete the returns_dict() decorator
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        assert(type(result) == dict)
        return result
    return wrapper

@returns_dict
def foo(value):
    return value

try:
    print(foo([1,2,3]))
except AssertionError:
    print('foo() did not return a dict!')

'''<script.py > output:
    foo() did not return a dict!'''

'''
Instructions 2/2

- Now complete the returns() decorator, which takes the expected return type as an argument.
'''

def returns(return_type):
    # Write a decorator that raises an AssertionError if the
    # decorated function returns a value that is not return_type
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            assert(type(result) == return_type)
            return result
        return wrapper
    return decorator

@returns(dict)
def foo(value):
        return value

try:
    print(foo([1,2,3]))
except AssertionError:
    print('foo() did not return a dict!')