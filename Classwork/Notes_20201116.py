Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #lists and strings
>>> #lists are mutable and heterogeneous
>>> #How to set up strings and manipulate them
>>> range(0, 10)
range(0, 10)
r
>>> list(range(0,10)
     )
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10, 0, -1)
     )
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
>>> #Task: List of even numbers starting from 0 up to and excluding a given bound
>>> n=10
>>> list(range(0, n, 2))
[0, 2, 4, 6, 8]
>>> #Task: Odd numbers
>>> list(range(1, n, 2))
[1, 3, 5, 7, 9]
>>> #filetering a list
>>> numbers = list(range(n))
>>> numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> filter
<class 'filter'>
>>> filter(None, numbers))
SyntaxError: unmatched ')'
>>> list(filter(None, numbers))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> def retainer_predicate(value):
	return True
list(filter(retainer_predicate, numbers))
SyntaxError: invalid syntax
>>> list(filter(retainer_predicate, numbers))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list(filter(retainer_predicate, numbers))
NameError: name 'retainer_predicate' is not defined
>>> 
KeyboardInterrupt
>>> def retainer_predicate(value):
	return True

>>> list(filter(retainer_predicate, numbers))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> def notZero(v):
	if 0 == v:
		return False
	else:
		return True

	
>>> notZero(numbers[1])
True
>>> notzero(numbers[0])
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    notzero(numbers[0])
NameError: name 'notzero' is not defined
>>> list(filter(notZero, numbers))
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> def isEven(n):
	if 0 == n % 2:
		return True
	else:
		return False

	
>>> list (filter(isEven, numbers))
[0, 2, 4, 6, 8]
>>> def isOdd(n):
	if 0 =! n % 2:
		
SyntaxError: invalid syntax
>>> def isOdd(n):
	if 0 != n % 2:
		return True
	else:
		return False

	
>>> list(filter(isOdd, numbers))
[1, 3, 5, 7, 9]
>>> def MultipleOfThree(n):
	if 0 = n%3:
		
SyntaxError: invalid syntax
>>> def MultipleOfThree(n):
	if 0 == n%3:
		return True
	else:
		return False

	
>>> list(filter(MultipleOfThree, numbers))
[0, 3, 6, 9]
>>> #Identifier conflict
>>> #Resolved based on SCOPE
>>> # != means not equal in programming
>>> # ! means negating
>>> 
>>> 
>>> #map function
>>> numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> #NEW TASK: enumerate (list) all the squares up to the square of 10 (100)
>>> numbers = list(range(0, 100))
>>> numbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> def isSquare(x)
SyntaxError: invalid syntax
>>> #mapping
>>> #different from filtering
>>> ## mapping ALWAYS returns a list of the same length
>>> list(map(isEven, numbers))
[True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False]
>>> def square(x)
SyntaxError: invalid syntax
>>> def square(x):
	x**2
	return x

>>> square(3)
3
>>> square(6)
6
>>> def square(x):
	x = x**2
	return x

>>> square(3)
9
>>> list(map(square, numbers))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801]
>>> numbers = range(10)
>>> list(map(square, numbers))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> #Recap: map 'maps' a list into a brand new list where every item is replaced by the output of a given function
>>> 
>>> #Final Task: evaluate a polynomial
>>> #2x**2 + 4x - 1 = p(x)
>>> # p(3) = 39
>>> 
>>> # p(3) = 29
>>> p = [-1, 4, 2]
>>> def eval_poly(poly, x):
	'''return poly(x)''''
	
SyntaxError: EOL while scanning string literal
>>> def eval_poly(poly, x):
	'''return poly(x)'''
	#First come up with all the powers of x
	#[1, x, x**2, x**3, ... x**len(poly)
	#Then multiply each coefficient with the x power
	#finally, suma ll together

	
>>> 