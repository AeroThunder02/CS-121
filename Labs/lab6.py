####################################################################################
# Name: Maciej Kowalczyk    
# Pledge: I pledge my Honor that I have abided by the Stevens Honor System
####################################################################################
# Lab 6: Recursion 2
# Demonstrate recursion as an algorithm design technique for the problem of 
# computing the (length of the) longest common subsequence of two given strings
#####################################################################################

##############################################################################
# Example: The longest common subsequence of "helllowo_rld" and "!helloabcworld!"
# is "helloworld", and it has a length of 10.
#
# Therefore LLCS("helllowo_rld", "!helloabcworld!") returns 10, and
# LCS("helllowo_rld", "!helloabcworld!") returns "helloworld"
##############################################################################

def LLCS(S1, S2):
    '''
    Return the length of the longest common subsequence (LLCS) of strings S1 and S2
    '''
    if not S1 or not S2:
        return 0
    else:
        head1, tail1 = S1[0], S1[1:]
        head2, tail2 = S2[0], S2[1:]
        if head1 == head2:
            return 1 + LLCS(tail1, tail2)
        else:
            return max(LLCS(tail1, S2), LLCS(S1, tail2))
    

##############################################################################
# Instead of returning the length of the longest common substring, this task
# asks you to return the string itself.
##############################################################################
# Tip: You may find it helpful to copy your solution to LLCS and edit it
# to solve this problem
##############################################################################

def LCS(S1, S2):
    '''return the longest common subsequence (LCS) between strings S1 and S2'''
    
    if not S1 or not S2:
        return ''
    else:

        head1, tail1 = S1[0], S1[1:]
        head2, tail2 = S2[0], S2[1:]
        
        a = LCS(tail1, tail2)
        b = LCS(tail1, S2)
        c = LCS(S1, tail2)
        b_len = len(LCS(tail1, S2))
        c_len = len(LCS(S1, tail2))
        
        if head1 == head2:
            return head1 + a
        
        else:
            if b_len > c_len:
                return b
            else:
                return c
                
     
