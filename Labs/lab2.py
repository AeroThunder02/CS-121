# Adapted by Dominick DiMaggio for Prof. Nicolosi's CS 115 at Stevens Institute of Technology, 2020

##########################################
# Name: Maciej Kowalczyk
# Pledge: I pledge my Honor that I have abided by the Stevens Honor Code 
##########################################

# Import reduce from the functools package
from functools import reduce

#######################################################################################
# Task 1: Use reduce to determine if all elements in a boolean list are true
    #TODO: Implement
L = [True, True, True, False]
R = [True, True, True, True]
G = [False, False, False, False]
F =[True, False]
I =[False]
B =[False, False, False, False, True, True, True, False]
def all_true(lst):
    result = reduce(lambda a, b: True if a and b else False, lst)
    return result

#tests
print(all_true(L))
print(all_true(R))
print(all_true(G))
print(all_true(F))
print(all_true(I))
print(all_true(B))
    

    

#######################################################################################
# Task 1.1: Use reduce to determine if AT LEAST one element in a boolean list is true
# Hint: Should be very similar to the above function
    # TODO: Implement
def one_true(lst):
    result = reduce(lambda a, b: True if a or b else False, lst)
    return result

#tests
print(one_true(L))
print(one_true(R))
print(one_true(G))
print(one_true(F))
print(one_true(I))
print(one_true(B))

#######################################################################################
# Task 2: Use map and reduce to return how many elements are True in a boolean list
    # TODO: Implement

#converts the list into a list of 1's and 0's
def conversion(ListToConvert):
    if ListToConvert == True:
        return 1
    else:
        return 0


def count_true(lst):
    converted_List = list(map(conversion, lst))
    True_count = reduce(lambda a, b: a + b, converted_List)
    return True_count

#tests
print(count_true(L))
print(count_true(R))
print(count_true(G))
print(count_true(F))
print(count_true(I))
print(count_true(B))

    
# This function is provided for you
# Gets a list of strings through the command line
# Input is accepted line-by-line
def getInput():
    lst = []
    txt = input()

    while(len(txt) != 0):
        lst.append(txt)
        txt = input()

    return lst

# Task 3: Get the longest string in the list using map and reduce, and print it out
# 'strings' is a list of input strings e.g. [ 'hello', 'world' ]
# Hint: The 'map' part of your program should take a string s into a length-2 list [len(s), s].
def StringWithLength(s):
    length = len(s)
    New_StringList = s + ' ' + str(length)
    return New_StringList
    
def getLongestString():
    strings = getInput()
    strings = list(map(StringWithLength, strings))
    print(reduce(lambda a, b: a if (len(a) > len(b)) else b, strings))
    
getLongestString()

    # TODO: Implement
