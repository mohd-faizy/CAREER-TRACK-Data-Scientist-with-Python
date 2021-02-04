'''
07 - Closures keep your values safe

You are still helping your niece understand closures. You  have  written  the 
function get_new_func() that returns a nested function. The  nested  function 
call_func() calls whatever function was passed to get_new_func(). You've also 
written my_special_function() which simply prints a message  that  states that 
you are executing my_special_function().

You want to show your niece that no matter what you do to  my_special_function()
after passing it to get_new_func(), the new function still mimics  the  behavior
of the original my_special_function() because it is in the new function's closure.

Instructions 
-------------------------------------------------------------------------------------------
- Show that you still get the original message even if you redefine my_special_function()
  to only print "hello".
'''

def my_special_function():
    print('You are running my_special_function()')

def get_new_func(func):
    def call_func():
    func()
    return call_func

new_func = get_new_func(my_special_function)

# Redefine my_special_function() to just print "hello"

def my_special_function():
    print("hello")

new_func()

'''
-------------------------------------------------------------------------------------------
- Show that even if you delete my_special_function(), you can still call new_func() without 
  any problems.
'''


def my_special_function():
    print('You are running my_special_function()')


def get_new_func(func):
    def call_func():
        func()
    return call_func


new_func = get_new_func(my_special_function)

# Delete my_special_function()
del(my_special_function)

new_func()

'''
----------------------------------------------------------------------------------------------
- Show that you still get the original message even if you overwrite my_special_function() with 
the new function.
'''

def my_special_function():
    print('You are running my_special_function()')


def get_new_func(func):
    def call_func():
        func()
    return call_func

# Overwrite `my_special_function` with the new function
my_special_function = get_new_func(my_special_function)

my_special_function()
