# As a beginner Python learner, your task is to demonstrate that you can set up Python locally and create simple unit tests. Follow these steps:

    # Install Python on your local machine if you haven't already. Make sure you have version 3.x installed.
    # Open a text editor or IDE (like PyCharm, VSCode, or Sublime Text) and create a new Python file.
    # Write a simple Python script with at least two functions that perform different operations. 
    # Documentation video on unit testing in python: https://www.youtube.com/watch?v=6tNS--WetLI

def subtract_numbers(a, b):
  """Subtrate Function """
  """Checks if the datatype is a integar or float """
  if isinstance(a, (int, float)) and isinstance (b, (int, float)):
     return a - b
  else:
     return "Please enter a valid number!"

print (subtract_numbers(2,3))
print (subtract_numbers("hi", "not a number!"))

def divide_numbers(a, b):
  """ Divide Function """
  """Checks if the inputs are 0"""
  if b == 0 or a == 0:
    return "Cannot divide by 0"
  
  elif isinstance(a, (int, float)) and isinstance (b, (int, float)):
    return a/b

print (divide_numbers(2, 3))
print (divide_numbers(10, 0))

