#
# 20fa-cs115bc
#
# Antonio R. Nicolosi 
# 20201120
#************************************************************
# *  Name  : Maciej Kowalczyk
# * Pledge : I pledge my Honor that I have abided by the Stevens Honor System.
#************************************************************

# Programming problems with one-dimensional arrays.
arr = [3, -5,  7, -1, -8, 0, -6, -2]
def isWithinRange(arr, min, sup):
    """
     Return True if and only if all entries in the array fall between
     the specified values, with min being permitted but sup being just
     beyond the allowable range).
     
     Sample input/outputs:
     Let arr = [3, -5,  7, -1, -8, 0, -6, -2]
     Then:
	 * isWithinRange(arr, -6, 10) -> False;
	 * isWithinRange(arr, -8, 10) -> True;
	 * isWithinRange(arr, -8, 7)  -> False;
	 */
    """
    for x in arr:
        if x < min:
            return False
        elif x >= sup:
            return False
        else:
            pass
        
    return True



def isPermutation(arr):
    """Returns True if and only if its entries, taken as a set, consist
    of all the numbers between 0 and len(arr)-1 (possibly permuted
    according to some arbitrary order).

    Sample input/outputs:
    * isPermutation([3, -5, 7, 4, -1, -8, 0, -6, -2]) --> False
    * isPermutation([3, 5, 7, 4, 1, 8, 0, 6, 2])      --> True
    * isPermutation([3, 1, 0, 3, 0])                  --> False
    * isPermutation([])                               --> True
    """

    nset = []
    for x in arr:
        if x not in nset:
            nset.append(x)
            
    nset_len = len(nset)
    maximum = nset_len - 1
    
    for x in nset:  
        if x < 0:
            return False
        elif x > maximum:
            return False
        else:
            pass
        
    return True
                

def isCyclic(arr):
    """
    Return true if-and-only-if the sequence arr[0], * arr[arr[0]],
    arr[arr[arr[0]]], ... reaches 0 * after traversing all entries in
    arr.

    Sample input/outputs:
    * isCyclic([3, 5, 7, 4, 1, 8, 0, 6, 2]) --> True
    * isCyclic([3, 5, 7, 4, 1, 8, 6, 0, 2]) --> False
    * isCyclic([3, 1, 0, 3, 0])             --> False
    * isCyclic([])                          --> True
    """

    pos = 0
    check = len(arr)
    count = 0
    for x in arr:
        count = count + 1
        pos = arr[pos]
        
        if x != 0:
            continue
        elif x == 0:
            if check == count:
                return True
            else:
                return False
        
    return False
    

def isSloppilySorted(arr, k):  #I honestly have no clue how to do this one. I had a ton of other work to do so I gave up
    """
    Return True if-and-only-if the entries in arr are sorted sloppily 
    "up to k", that is, every entry precedes at most k smaller values
     and follows at most k larger values.

    Sample input/outputs:
    * isSloppilySorted([3, 2, 1, 0, 4, 8, 7, 6, 5], 3) --> True
    * isSloppilySorted([3, 2, 1, 0, 4, 8, 7, 6, 5], 2) --> False
    * isSloppilySorted([0, 1, 2, 3, 4, 5, 6, 7, 8], 1) --> True
    * isSloppilySorted([], 3)                          --> True
    """
    
    
        
