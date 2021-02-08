############################################################
# Name: Maciej Kowalczyk
# CS115 HW3 ~ Applications of Map & Reduce
# Due : Sep. 30th, 2020
# 
# Pledge: I pledge my honor that I have abided by the Stevens Honor System

from functools import reduce
from math import factorial, sqrt # this import is necessary to use sqrt and factorial.


def taylorApproxE(lastIter):
    '''
     appoximates the mathematical value of e^x using the Taylor Expansion
     sequence. First we get a list of integers to represent the factors of the number
     input. Then we take the factorial of each one. Later we take the reciprocal of said
     numbers, add them together. Finally, we return that sum + 1 to get the approx value
     of e^x.
     '''
    integers = range(1, lastIter+1)
    factorials = list(map(factorial, integers))
    
    def reciprocal(x):   # Pretty sure I wasn't allowed to import this one. Thankfully its a super easy helper function to write.
        return 1/x  
    
    reciprocals = list(map(reciprocal, factorials))  # make a new list of recips
    recip_Sum = reduce(lambda a,b: a+b, reciprocals) # Couldn't use Sum function. Reduce function was still easy to write out.
    return recip_Sum +1 # Final result

print(taylorApproxE(4))


intlst = [3 , 6 , 7, 1]

def vectorNorm(vect1):
    '''
    Function will take a list of numbers and map a new list with those same values
    but squared. Then they will all be added up using the reduce function and finally
    the square root will be taken
    '''
    def square(x): # Helper function
        return x**2
    
    squared_list = list(map(square, vect1))
    sum_of_squares = reduce(lambda x,y: x + y, squared_list)
    return sqrt(sum_of_squares)

print(vectorNorm(intlst))


numlst = [1, 2, 3, 4 ,5]
def arithMean(vect1):
    '''
    Function will take a list of integers and add them all up. It will then divide that sum
    by the length of the list and return that value.
    '''
    listLength = len(vect1)
    listSum = reduce(lambda x,y: x+y, vect1)
    return listSum/listLength

print(arithMean(numlst))
    
    



