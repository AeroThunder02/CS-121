Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # recursive list functions
>>> ## Lists are in fact a *recursive* data structure
>>> ### Lists are only one of two things:
>>> #### Empty []
>>> #### or they consist of a first item (head) followed by a list
>>> 
>>> ### How come [3, 4, 5] is a list?
>>> ### b/c [4, 5] is a list and [3, 4, 5] is obtained adding 3 as the new head
>>> #### how come [4, 5] is a list? b/c [5] is a list and prepending 4 gets you [4, 5]
>>> #### [5] is a list b/c [] is a list
>>> # head of a non-empty list L is L[0] and the tail
>>> #
>>> # 'Tail' of L is L[1:0]
>>> # Recursive list function do not access ay indices/slices other than L[0] and L[1:]
>>> def rec_length(L):
	'''
	Compute the length of L recursively.
	Bases on the idea that.
	-rec_length([]) = 0 (basis)
	-rec_length([L]) = 1 + rec_length(L[1:]
	'''
	if [] == L: #empty list
		result = 0

		
>>> def rec_length(L):
	'''
	Compute the length of L recursively.
	Bases on the idea that.
	-rec_length([]) = 0 (basis)
	-rec_length([L]) = 1 + rec_length(L[1:]
	'''
	if [] == L: #empty list
		result = 0
	else:
		head = L[0]
		tail = L[1:]
		prev_result = rec_length(tail)
		result = 1 + prev_result #combining contrib of head with that of tail
	return result

>>> rec_length([3,5])
2
>>> def rec_sum(L):
	'''
	Compute the sum of the items in L, recursively.
	Bases on the idea that.
	-rec_sum([]) = 0 (basis)
	-rec_sum([L]) = L[0] + rec_sum(L[1:]
	'''
	if [] == L: #empty list
		result = 0
	else:
		head = L[0]
		tail = L[1:]
		prev_result = rec_lsum(tail)
		result = head + prev_result #combining contrib of head with that of tail
	return result

>>> rec_sum([1,2,3,4,5])
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    rec_sum([1,2,3,4,5])
  File "<pyshell#40>", line 13, in rec_sum
    prev_result = rec_lsum(tail)
NameError: name 'rec_lsum' is not defined
>>> rec_sum([1,2,3])
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    rec_sum([1,2,3])
  File "<pyshell#40>", line 13, in rec_sum
    prev_result = rec_lsum(tail)
NameError: name 'rec_lsum' is not defined
>>> def rec_sum(L):
	'''
	Compute the sum of the items in L, recursively.
	Bases on the idea that.
	-rec_sum([]) = 0 (basis)
	-rec_sum([L]) = L[0] + rec_sum(L[1:]
	'''
	if [] == L: #empty list
		result = 0
	else:
		head = L[0]
		tail = L[1:]
		prev_result = rec_sum(tail)
		result = head + prev_result #combining contrib of head with that of tail
	return result

>>> rec_sum([1,2,3,4,5])
15
>>> 