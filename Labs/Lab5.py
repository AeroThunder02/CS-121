####################################################################################
# Name: Maciej Kowalczyk
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
####################################################################################


# The binary format you'll be working with for this assignment is called R2L,
# as it is a right-to-left representation.
####################################################################################
## Ex: 8 in decimal is 1000 in standard binary (2^3),
## and represented as a list [0, 0, 0, 1] in our R2L representation.
####################################################################################

# Notice that this makes it very easy to work with binary,
# by using num[0] to grab the least significant bit (2^0)!
#
# Please fill out the following 4 functions below using recursion, as specified.

# Given an integer x >= 0, convert it to the R2L binary format.
# Take note that both [] and [0] are used to represent 0 in R2L
def decimalToBinary(x):
    if x == 0:
        return [0]
    
    elif x == 1:
        return [1]
    
    else:
        binary = [x % 2] + decimalToBinary(x//2)
        return binary


# Given an R2L formatted number, return the integer it is equivalent to.
# The function should function with both [] and [0] returning 0.
def binaryToDecimal(num):
    if num == []:
        return 0
    
    elif num ==[1]:
        return 1
    
    else:
       list_length = len(num)
       head = num[-1]
       tail= num[:-1]
       conversion = head*2**(list_length-1)
       prev_conversion = binaryToDecimal(tail)
       result = conversion + prev_conversion

    return result
   

# Given an R2L formatted number, return an R2L equivalent to num + 1
# If you need to increase the length, do so. Again, watch out for 0

def incrementBinary(num):
    if num == []:
        return [1]

    else:
        head = num[0]
        tail = num[1:]

        if head == 0:
            return [1] + tail
        else:
            return [0] + incrementBinary(tail)

# Given 2 R2L numbers, return their sum.
## You MUST implement recursively the algorithm for bit-by-bit addition as taught in class,
## you may NOT do something like decimalToBinary( binaryToDecimal(num1) + binaryToDecimal(num2) ).
# Make sure to figure out what to do when num1 and num2 aren't of the same length!
# (and be sure you can add [] and [0])
## Tip: Try this on paper before typing it up


# own carrying, can call incrementBinary

def addBinary(num1, num2):
    
    if num1 == []:
        return num2
    elif num2 == []:
        return num1

    else:
        head1 = num1[0]
        head2 = num2[0]
        tail1 = num1[1:]
        tail2 = num2[1:]
        head_add = head1 + head2
        
        if head_add == 2:
            head_add = 0
            tail1 = incrementBinary(tail1)
            
        return [head_add] + addBinary(tail1, tail2)
    
