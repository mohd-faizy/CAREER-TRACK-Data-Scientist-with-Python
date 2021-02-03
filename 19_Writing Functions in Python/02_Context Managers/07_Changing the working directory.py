'''
07 - Changing the working directory

You are using an open-source library that lets you train deep     neural 
networks on your data. Unfortunately, during training, this      library 
writes out checkpoint models (i.e., models that have been trained     on 
a portion of the data) to the current working directory. You find   that 
behavior frustrating because you don't want to have to launch the script 
from the directory where the models will be saved.

You decide that one way to fix this is to write a context manager that 
changes the current working directory, lets you build your models, and 
then resets the working directory to its original location. You'll want 
to be sure that any errors that occur during model training don't prevent 
you from resetting the working directory to its original location.

Instructions

- Add a statement that lets you handle any errors that might occur inside 
  the context.
- Add a statement that ensures os.chdir(current_dir) will be called, whether 
  there was an error or not.
'''


def in_dir(directory):
  """Change current working directory to `directory`,
  allow the user to run some code, and change back.

  Args:
    directory (str): The path to a directory to work in.
  """
  current_dir = os.getcwd()
  os.chdir(directory)

  # Add code that lets you handle errors
  try:
    yield
  # Ensure the directory is reset,
  # whether there was an error or not
  finally:
    os.chdir(current_dir)
