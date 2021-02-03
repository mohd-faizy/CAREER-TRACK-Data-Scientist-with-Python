'''
02 - The speed of cats

You're working on a new web service that processes Instagram     feeds 
to identify which pictures contain cats (don't ask why -- it's     the 
internet). The code that processes the data is slower than you   would 
like it to be, so you are working on tuning it up to run faster. Given 
an image, image, you have two functions that can process it:

    - process_with_numpy(image)
    - process_with_pytorch(image)

Your colleague wrote a context manager, timer(), that will print out   how 
long the code inside the context block takes to run. She is suggesting you 
use it to see which of the two options is faster. Time each function    to 
determine which one to use in your web service.

Instructions

- Use the timer() context manager to time how long process_with_numpy(image) 
  takes to run.
- Use the timer() context manager to time how long process_with_pytorch(image) 
  takes to run.
'''
image = get_image_from_instagram()

# Time how long process_with_numpy(image) takes to run
with timer():
  print('Numpy version')
  process_with_numpy(image)

# Time how long process_with_pytorch(image) takes to run
with timer():
  print('Pytorch version')
  process_with_pytorch(image)

'''
<script.py> output:
    Numpy version
    Processing..........done!
    Elapsed: 1.52 seconds

    Pytorch version
    Processing..........done!
    Elapsed: 0.33 seconds
'''

'''
Terrific timing! Now that we know the pytorch version is   faster, 
you can use it in your web service to ensure your users get   the 
rapid response time they expect.

You may have noticed there was no as <variable name> at the end of 
the with statement in timer() context manager. That is      because 
timer() is a context manager that does not return a value, so   the 
as <variable name> at the end of the with statement isn't necessary. 
In the next lesson, you'll learn how to write your own       context 
managers like timer().
'''
