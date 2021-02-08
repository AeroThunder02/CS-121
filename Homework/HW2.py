# Created by Prof. Nicolosi & Dominick DiMaggio for CS 115 at Stevens Institute of Technology, 2020

##########################################
# Name: Maciej Kowalczyk
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
##########################################
from math import floor

######################################################################
# Task 1: Given an 8-digit decimal number representing the date,
#         calculate the day of the week
# Input: 8-digit decimal number in the format of YYYYMMDD
# Saturday: 0, Sunday: 1... Friday: 6  
# Hint: Look at Zeller's congruence.
#       The floor() function may be helpful. (Ex: floor(5.5) = 5)

date = 20200920
year = date // 10000                    
month_day = date % 10000         
month = month_day // 100                   
day = month_day % 100
century = (year % 100) + 1
zero_based_century = year % 100

q = month_day
e = ((13*(month+1))/5)
K = century
J = zero_based_century

x = (q + e + K + (K/4) + (J/4) - 2*J) % 7
x = floor(x)
    

#code is poorly optimized, but I had to rush this a little bit    
   




def getWeekday(timestamp):

    # NOTE: unoptimized 'if' statement mess. Didnt know if i was allowed to use a switch statement
    #   or not since it is my previous knowledge
    if timestamp == 0:
               print('The weekday of your date is Saturday')
    elif timestamp == 1:
               print('The weekday of your date is Sunday')
    elif timestamp == 2:
               print('The weekday of your date is Monday')
    elif timestamp == 3:
               print('The weekday of your date is Tuesday')
    elif timestamp == 4:
               print('The weekday of your date is Wednesday')
    elif timestamp == 5:
               print('The weekday of your date is Thursday')
    elif timestamp == 6:
               print('The weekday of your date is Friday')
    else:
        pass

    
getWeekday(x)


    # TODO: Implement

######################################################################
# Task 2: For this task, you will create an encoder and decoder
#         for a Caesar cipher using the map function.
# You may find this website helpful:
# https://cryptii.com/pipes/caesar-cipher

######################################################################
# This provided helper function may be useful
# Input: List of ASCII values (Ex: [72, 69, 76, 76, 79])
# Output: String (Ex. 'HELLO')     ('H   E   L   L   O')

def asciiToString(asciiList):
    return ''.join(map(chr, asciiList))

def StringtoAscii(stringlist):
    return ''.join(map(ord, stringlist))

######################################################################
# Encoder
# Input: A string value with all capital letters (leave everything
#        else as-is) and a shift value (Ex. HELLO WORLD, 3)
# Output: An encoded string            (Ex. KHOOR ZRUOG)
# Hint: The ord() function converts single-character strings to ASCII
some_string = 'This is a string'

def caesarEncoder(string, shift):
    converted_string = list(map(ord, string))

    def encoder(x):
        return x + shift
                           

    encoded_string = list(map(encoder, converted_string))

    encoded_string = asciiToString(encoded_string)

    print('Your encoded string is: ' + encoded_string)
    # TODO: Implement

caesarEncoder(some_string, 2)
######################################################################
# Decoder
# Input: A string value with all capital letters (leave everything
#        else as-is) and a shift value (Ex. KHOOR ZRUOG, 3)
# Output: A decoded string             (Ex. HELLO WORLD)
# Hint: The chr() function converts ASCII to a single-character string
encoded_string = 'Vjku ku cu vtkpi'
def caesarDecoder(string, shift):
    converted_string = list(map(ord, string))

    def decoder(x):
        return x - shift
                           

    decoded_string = list(map(decoder, converted_string))

    decoded_string = asciiToString(decoded_string)

    print('Your decoded string is: ' + decoded_string)
    
    # TODO: Implement
    
#NOTE: doing this will give you the same string, yes, but the spaces get removed.
    # I do not currently know a fix for this
caesarDecoder(encoded_string, 2)
