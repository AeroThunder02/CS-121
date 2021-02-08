# HW4
# Maciej Kowalczyk
# I pledge my honor that I have abided by the Stevens Honor System
#########################################################

from random import randrange
from functools import reduce

c = [7, 24, 42]

def change(amount, coins):
    '''
    takes an amount a list of coins. Returns a list of the least amount of coins to reach
    the amount provided.
    '''
    if amount == 0:
        return 0
    elif coins == []:
        return float("inf")
    elif coins[0] > amount:
        return change(amount, coins[1:])
    else:
       unused = change(amount, coins[1:])
       used = 1 + change(amount - coins[0], coins)
       return min(unused, used)


def currency(length): #pretty bad implementation in all honesty. If you have time later try to find a better one, but this works just fine.
    '''
    Takes a length and returns a list of randomly generated numbers
    of length 'length.' The function also checks for duplicate elements
    and if there are any,
    '''
    length_list = [length] * length
    
    if length_list == []:
        return []
    else:
        lst = list(map(lambda x: randrange(x), length_list))

    lst_set = set(lst)
    
    if len(lst) == len(lst_set):
        print(lst)
    else:
        currency(length)

    
    
currency(5)
currency(7)
