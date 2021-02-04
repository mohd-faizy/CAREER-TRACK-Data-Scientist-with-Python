'''
01 - Building a command line data app

You are building a command line tool that lets a user interactively 
explore a data set. We've defined four functions: mean(),     std(), 
minimum(), and maximum() that users can call to analyze their  data. 
Help finish this section of the code so that your users can call any 
of these functions by typing the function name at the input prompt.

Note: The function get_user_input() in this exercise is a mock version 
of asking the user to enter a command. It randomly returns one of  the 
four function names. In real life, you would ask for input and wait until 
the user entered a value.

Instructions

- Add the functions std(), minimum(), and maximum() to the function_map 
  dictionary, like we did with mean().
- The name of the function the user wants to call is stored in func_name. 
  Use the dictionary of functions, function_map, to call the chosen function 
  and pass data as an argument.
'''
# Add the missing function references to the function map
function_map = {
    'mean': mean,
    'std': std,
    'minimum': minimum,
    'maximum': maximum
}

data = load_data()
print(data)

func_name = get_user_input()

# Call the chosen function and pass "data" as an argument
function_map[func_name](data)

'''By adding the functions to a dictionary, we can select the function 
based on the user's input. You could have also used a series of if/else
statements, but putting them in a dicti
'''
