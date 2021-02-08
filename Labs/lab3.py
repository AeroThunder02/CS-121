############################################################
# Name: Maciej Kowalczyk
# CS115 Lab 3
# 
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
############################################################

from functools import reduce

# Task 1: Use reduce to add up all elements in a list
"""
Input: A list of numbers
Output A number representing the sum
Example: add_all([1, 2, 3]) = 6
"""
num_list = [1,2,3]
num_list2 = [4,5,6]
num_list3 = [7,8,9]

def add_all(lst):
    return reduce(lambda x,y: x+y, lst)
    
print(add_all(num_list))
print(add_all(num_list2))
print(add_all(num_list3))

# Task 2: Use map to evaluate a given polynomial at a specific x-value
"""
Input:
  p: A list of coefficients for increasing powers of x
  x: The value of x to evaluate
Output: Number representing the value of the evaluated polynomial
Example: poly_eval([1, 2, 3], 2) = 1(2)^0 + 2(2)^1 + 3(2)^2 = 17
"""
poly = [1,2,3]
x = 2

poly2 = [1,2]
x2 = 5

poly3 = [1, 2, 3]
x3 = 5


def poly_eval(p, x):
    # Returns the value of x to the ith power
    poly_length = list(range(0, len(p)))
    def x_powers(i):
        return x**i
    
    def mult(a,b):
        return a*b
    
    def add(a,b):
        return a+b

    powers = list(map(x_powers, poly_length))
    print(powers) 
    mult_powers= list(map(mult, powers, p))          #This variable name sucks, change later.
    return reduce(add, mult_powers)
    
    

print(poly_eval(poly, x))
print(poly_eval(poly2, x2))
print(poly_eval(poly3, x3))

# Why did this take me two hours again?
# NOTE: Future me, please do something to wake your brain up before you code next time around.
