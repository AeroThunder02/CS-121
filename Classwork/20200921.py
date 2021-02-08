Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #review of filter and map
>>> #map on more than one list
>>> #sum, max, min
>>> #functools.reduce
>>> #prelude to lambda
>>> 
>>> def filter_evens(L):
	def is_even(x)
	
SyntaxError: invalid syntax
>>> def filter_evens(L):
	def is_even(x):
		return 0 == x % 2
	return filter(is_even,L)

#below is the edited version for lambda expressions
def filter_evens(L):
        #Simplified function ends up being only 2 lines, which includes the definition
        return filter(lambda x: 0 == x % 2, L)

>>> list(filter_evens(range(0,10))
     )
[0, 2, 4, 6, 8]
>>> #map
>>> def list_of_squares(L):
	def squar(x):
		return x**2
	return map(square, L)

>>> list(list_of_squares(range(6)))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    list(list_of_squares(range(6)))
  File "<pyshell#19>", line 4, in list_of_squares
    return map(square, L)
NameError: name 'square' is not defined
>>> def list_of_squares(L):
	def square(x):
		return x**2
	return map(square, L)

>>> list(list_of_squares(range(6)))
[0, 1, 4, 9, 16, 25]
>>> #map with more than 1 list
>>> # given two lists, compute list of sums
>>> list1= [1, 2, 3]
>>> list2 = [4, 5, 6]
>>> def sum_of_lists(L1, L2):
	def add(x, y):
		return x+y
	return map(add, L1, L2)

>>> list(sum_of_lists(list1, list2))
[5, 7, 9]
>>> list_of_pairs = [[1,4], [2,5], [3,6]]
>>> 
