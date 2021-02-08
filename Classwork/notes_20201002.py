Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def binomial_coefficient(n, k):
	'''
	compute \choose {n}{k}
	say you have n items, and need to coount all the possible choices
	that you have if you can grab k distinct items

	Assume 0 <= k <= n
	'''
	#use it or lose it paradigm
	if n-1 < k or k-1 < 0:
		result = 1
	else:
		useit_count = binomial_coefficient(n-1, k-1)
		loseit_count = binomial_coefficient(n-1, k)
		result = useit_count + loseit_count

		
>>> def binomial_coefficient(n, k):
	'''
	compute \choose {n}{k}
	say you have n items, and need to coount all the possible choices
	that you have if you can grab k distinct items

	Assume 0 <= k <= n
	'''
	#use it or lose it paradigm
	if n-1 < k or k-1 < 0:
		result = 1
	else:
		useit_count = binomial_coefficient(n-1, k-1)
		loseit_count = binomial_coefficient(n-1, k)
		result = useit_count + loseit_count
	return result

>>> binomial_coefficient(4, 2)
6
>>> 