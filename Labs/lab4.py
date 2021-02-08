# Name: Maciej Kowalczyk
# Pledge: I pledge my honor that I have abided by the Stevens Honor System

int_list = [1, 2, 3, 4 , 5]
int_list2 = [2, 3, 4, 5, 6]
int_list3 = [5]
int_list4 = [7]
int_list5 = [5,3]
int_list6 = [6,4]

def dotProduct(L, K):
    '''
    Computes the product of L and K recursively.
    Takes in two lists and multiplies all elements that are in the same position
    and adds thenm together.
    '''
    if L == [] or K ==[]:
        return 0

    else:
        head1 = L[0]
        head2 = K[0]
        tail1 = L[1:]
        tail2 = K[1:]
        head_product = head1 * head2
        prev_result = dotProduct(tail1, tail2)
        result = head_product + prev_result

    return result

print(dotProduct(int_list, int_list2))
print(dotProduct(int_list3, int_list4))
print(dotProduct(int_list5, int_list6))


String = 'spam'
String2 = 'this is a string'
String3 = 'this is a different string'




def expand(S):
    '''
    Takes a string input and converts it to a list. It then returns a new list
    of the strings individual characters of length 1.
    '''
    
    if S == '':
        return []
    
    else:
        head = [S[0]]
        tail = S[1:]
        prev_result = expand(tail)
        result = head + prev_result
        
    return result

print(expand(String))
print(expand(String2))
print(expand(String3))

# The following lists are used for the next three funcitons
list1 = [1, 2, [3, [4, [56]], 2, 5], [5, 7]]
list2 = [1, 1, 2, 3, [4,[4,[4,]]]]
list3 = [[1,2], 3, [4,5,6]]
list4 = [1, 2, 3, 3, 3, 3, 4, 5]

def deepMember(e, L):
    '''
    This function takes an element and a list, and proceeds to check the
    list if stated element exists. It also checks any nested lists. If it detects
    the stated element, it returns true. Otherwise it returns false
    '''
 
    if L == []:
        return False
    else:
        if isinstance(L[0], list):
            result = deepMember(e, L[0])
            if result:
                return result
        
        if e == L[0]:
            return True
        else:
            return deepMember(e, L[1:])
        
print(deepMember(5, list3))
print(deepMember(5, list2))
print(deepMember(56, list1))

 
#works fine with normal lists, unsure how to do with nested lists. Try to take example from deepReverse and apply it here
def removeAll(e, L):
    '''
    This function takes an element and a list, and proceeds to check the
    list for said element. If the function detects said element, it removes it.
    '''
    if L == []:
        return []
    else:
        if isinstance(L[0], list):
            result = removeAll(e, L[0])
            return result
        
        if e == L[0]:
            return [] + removeAll(e, L[1:])
        else:
            return [L[0]] + removeAll(e, L[1:])

print(removeAll(4, list2))
print(removeAll(3, list4))
print(removeAll(5, list1))

#do first, its the easiest out of the last 3
def deepReverse(L):
    '''
    Takes a list and reverses it, including any nested lists.
    '''
    if L ==[]:
        return []
    else:
        if isinstance(L[0], list):
            L[0] = deepReverse(L[0])
        return deepReverse(L[1:]) + [L[0]]

print(deepReverse(list3))
print(deepReverse(list1))
     
        

    
    
