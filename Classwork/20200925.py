Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Recursion
>>> ## Focus on what we are trying to do, rather than how
>>> ## loops --> how
>>> # Quizzes starting next week
>>> ## 8 mins
>>> # to do a task, you may need to perform similar sub-task on smaller inputs
>>> from math import factorial
>>> factorial(1)
1
>>> factorial(2)
2
>>> factorial(4)
24
>>> # factorial(n) is the product of all integers from 1 up to n
>>> # induction / recursion
>>> # simplest example of recursion (that isnt a function) is an integer number
>>> # positive ineger numbers
>>> # 1
>>> # succesor(n)
>>> # successor(n) :: = n+1
>>> # recursive def for pos integers
>>> ## 1
>>> ## s(n) for a positive integer n
>>> # E.G 5 is a positive integer because 4 is
>>> ## we know 4 is a positive integer b/c 4-1 = 3
>>> ## this keeps going until 1, which we know is a positive integer as a fact
>>> 
>>> def is_positive_int(n):
	'''Return True if n is a positive integer'''
	if 1 == n:
		return True
	else:
		flag = is_positive_integer(n-1)
		if flag:
			return True
		else:
			return False

		
>>> def is_positive_integer(n):
	'''Return True if n is a positive integer'''
	if 1 == n:
		return True
	else:
		flag = is_positive_integer(n-1)
		if flag:
			return True
		else:
			return False

		
>>> is_positive_integer(1)
True
>>> is_positive_integer(2)
True
>>> is_positive_integer(351)
True
>>> def is_positive_integer(n):
	'''Return True if n is a positive integer'''
	if n < 0:
		return False
	elif 1 == n:
		return True
	else:
		flag = is_positive_integer(n-1)
		if flag:
			return True
		else:
			return False

		
>>> is_positive_integer(100)
True
>>> is_positive_integer(-1)
False
>>> def is_positive_integer(n):
	'''Return True if n is a positive integer'''
	if n < 0:
		return False
	else:
		if 1 == n:
			return True
		else:
			flag = is_positive_integer(n-1)
			if flag:
				return True
			else:
				return False

			
>>> def is_positive_integer(n):
	'''Return True if n is a positive integer'''
	if n < 0:
		return False
	elif 1 == n:
		return True
	else:
		return is_positive_integer(n-1)

	
>>> def rec_factorial(n):
	'''Recursive Definition of factorial'''
	if n < 0:
		return -1
	elif 1 == n:
		return 1
	else:
		up_to_n_1 = factorial(n-1)
		return n * up_to_n_1

	
>>> rec_factorial(5)
120
>>> 