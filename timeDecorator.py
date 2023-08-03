import time

def timed(function):
	"""
    Decorator to get the time some function takes to execute
    Parameters:
    func (callable): The function to be decorated.
    Returns:
    callable: The decorated function.
    """
	def wrapper(*args, **kwargs):
		before = time.time()
		value = function(*args, **kwargs)
		after = time.time()
		fname = function.__name__
		print(f"{fname} tool {after-before} seconds to execute")
		return value
	return wrapper
	
@timed
def factorial(x):
    """
    Calculate the factorial of a given non-negative integer.
    Parameters:
    x (int): The non-negative integer for which the factorial is to be calculated.
    Returns:
    int: The factorial of the input integer.
    """
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

factorial(5000)