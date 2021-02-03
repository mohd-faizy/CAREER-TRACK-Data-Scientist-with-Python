'''
03 - The timer() context manager

A colleague of yours is working on a web service that processes Instagram photos. 
Customers are complaining that the service takes too long to identify whether  or 
not an image has a cat in it, so your colleague has come to you for help.     You 
decide to write a context manager that they can use to time how long        their 
functions take to run.

Instructions

- Add a decorator from the contextlib module to the timer() function that will make 
  it act like a context manager.
- Send control from the timer() function to the context block.
'''

# Add a decorator that will make timer() a context manager
@contextlib.contextmanager
def timer():
  """Time the execution of a context block.

  Yields:
    None
  """
  start = time.time()
  # Send control back to the context block
  yield
  end = time.time()
  print('Elapsed: {:.2f}s'.format(end - start))


with timer():
  print('This should take approximately 0.25 seconds')
  time.sleep(0.25)


'''<script.py> output:
    This should take approximately 0.25 seconds
    Elapsed: 0.25s
    
You're managing context like a boss! And your colleague can now use     your 
timer() context manager to figure out which of their functions is    running 
too slow. Notice that the three elements of a context manager are all  here: 
a function definition, a yield statement, and the @contextlib.contextmanager 
decorator. It's also worth noticing that timer() is a context manager   that 
does not return an explicit value, so yield is written by itself without 
specifying anything to return.
 '''
