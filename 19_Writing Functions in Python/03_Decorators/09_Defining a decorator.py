'''
09 - Defining a decorator

Your buddy has been working on a decorator  that  prints  a  "before" 
message before the decorated function is called and prints an "after"
message after the  decorated  function  is  called. They  are  having 
trouble remembering how wrapping the decorated function  is  supposed 
to work. Help them out by finishing their print_before_and_after()
decorator.

Instructions

- Call the function being decorated and pass it the positional arguments 
  *args.
- Return the new decorated function.
'''
def print_before_and_after(func):
    def wrapper(*args):
        print('Before {}'.format(func.__name__))
        # Call the function being decorated with *args
        func(*args)
        print('After {}'.format(func.__name__))
    # Return the nested function
    return wrapper

@print_before_and_after
def multiply(a, b):
  print(a * b)


multiply(5, 10)

'''
The decorator   print_before_and_after()  defines  a  nested  function  wrapper() 
that calls whatever  function  gets passed to print_before_and_after(). wrapper() 
adds a little something else to the function call by printing one message before 
the decorated function is called and another right afterwards. 

Since print_before_and_after() returns the new wrapper() function, we can use it 
as a decorator to decorate the multiply() function.
'''
