# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name    : Maciej Kowalczyk
# Pledge  : I pledge my Honor that I have abided by the Stevens Honor System
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Max:
#  Write a hmmm function that gets two numbers,
#   then prints the larger of the two.
#  Assumptions: Both inputs are any integers
Max = """
00 read r1           
01 read r2       #User input
02 copy r3 r1
03 copy r4 r2   #set user inputs to iterative operators
04 jeqzn r3  09
05 jeqzn r4  11    #if one of the iterative operators hits 0, jump to line where the max is printed
06 addn r3 -1
07 addn r4 -1       #iteration to determine max
08 jumpn 04       #back to 04 to check for 0
09 write r2   
10 halt
11 write r1  
12 halt                  #depending on which hits 0 first, these print the max

"""

# Power:
#  Write a hmmm function that gets two numbers,
#   then prints (No.1 ^ No.2).
#  Assumptions: No.1 is any integer, No.2 >= 0
Power = """
00 read r1
01 read r2                   # reading user input...
02 setn r3 1                # Setting the base
03 jeqzn r2 07             # if iterative operator = 0, skip to end
04 mul r3 r1 r3             # raising the base to 'power'
05 addn r2 -1               # iteration to repeat process till our power reaches 0
06 jumpn 03
07 write r3
08 halt

"""


# Fibonacci
#  Write a hmmm function that gets one number,
#   then prints the No.1st fibonacci number.
#  Assumptions: No.1 >= 0
#  Hint: You really don't want to implement
#   recursion in hmmm, try to find an
#   iterative method to compute your goal.
#  Tests: f(2) = 1
#         f(5) = 5
#         f(9) = 34
Fibonacci = """
00 read r1
01 setn r2 0 # represents the answer
02 setn r3 1 # represents the number that comes AFTER the answer
03 jeqzn r1 09  # if r1 (iterative operator) is 0, write r2 and end
04 add r4 r2 r3  # Fibonacci sequence...
05 copy r2 r3  
06 copy r3 r4    # sets new variables to current values in order to continue Fibonacci
07 addn r1 -1    # iteration
08 jumpn 03     # back to 03 to check if 0. If not, continue
09 write r2       
10 halt


"""


# ~~~~~ Running ~~~~~~
import hmmm
import importlib

runThis = Fibonacci # Change to the function you want to run
doDebug = True # Change to turn debug mode on/off

# call main() from the command line to run the program again
def main(runArg = runThis, debugArg = doDebug):
    importlib.reload(hmmm)
    hmmm.main(runArg, debugArg)

if __name__ == "__main__" : 
    main()


