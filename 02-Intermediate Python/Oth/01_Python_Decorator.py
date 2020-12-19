def multiply(by = None):
	def multiply_real_decorator(function):
		def wrapper(*args,**kwargs):
			return by * function(*args,**kwargs)
		return wrapper
	return multiply_real_decorator

@adder()
def adder(a,b):
  return a + b

@subtractor()
def subtractor(a,b):
  return a - b

print(adder(2,3))
print(subtractor(2,3))