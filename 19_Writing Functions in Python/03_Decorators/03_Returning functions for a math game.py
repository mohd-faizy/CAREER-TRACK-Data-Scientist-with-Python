'''
03 - Returning functions for a math game

You are building an educational math game where the  player  enters 
a math term, and your program returns a function that matches  that 
term. For instance, if the user types "add", your program returns a
function that adds two numbers. So far you've only implemented the 
"add" function. Now you want to include a "subtract" function.

Instructions

- Define the subtract() function. It should take two arguments and return 
  the first argument minus the second argument.
'''

def create_math_function(func_name):
    if func_name == 'add':
        def add(a, b):
            return a + b
        return add
    elif func_name == 'subtract':
        # Define the subtract() function
        def subtract(a, b):
            return a - b
        return subtract
    else:
        print("I don't know that one")

add = create_math_function('add')
print('5 + 2 = {}'.format(add(5, 2)))

subtract = create_math_function('subtract')
print('5 - 2 = {}'.format(subtract(5, 2)))
