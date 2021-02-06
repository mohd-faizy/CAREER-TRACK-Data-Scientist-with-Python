'''
06 - Run_n_times()

In the video exercise, I showed you an example of  a  decorator  that  takes 
an argument: run_n_times(). The code for that decorator  is  repeated  below 
to remind you how it works. Practice different ways of applying the decorator 
to the function print_sum(). Then I'll show you a funny prank you can play 
on your co-workers.
'''

def run_n_times(n):
    """Define and return a decorator"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

'''
Instructions 1/3

- Add the run_n_times() decorator to print_sum() using decorator syntax so that 
  print_sum() runs 10 times.
'''
# Make print_sum() run 10 times with the run_n_times() decorator
@run_n_times(10)
def print_sum(a, b):
    print(a + b)

print_sum(15, 20)

'''
Instructions 2/3

- Use run_n_times() to create a decorator run_five_times() that will run any 
  function five times.
'''
# Use run_n_times() to create the run_five_times() decorator
run_five_times = run_n_times(5)

@run_five_times
def print_sum(a, b):
  print(a + b)
  
print_sum(4, 100)

'''
Instructions 3/3

- Here's the prank: use run_n_times() to modify the built-in print() function so
  that it always prints 20 times!
'''

# Modify the print() function to always run 20 times
print = run_n_times(20)(print)
print('What is happening?!?!')

'''
- Warning: overwriting commonly used functions is probably not a great idea, so think
  twice before using these powers for evil.
'''
