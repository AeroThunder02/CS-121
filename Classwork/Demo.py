# All files will start with a block comment as follows

# Filename.py
# Honor Pledge

# Name
# Date

# Description of code by demonstrating basic Python syntax, semantics, and style

from math import sqrt

# Convert a temperature from Celcius to Farenheit
# 0C = 32F
# 100C = 212F
# A gap of 10C corresponds to 18F

def to_F(Celcius):
    return ((18.0/10.0)*Celcius)+32.0

def String_len(value):
    return len(value)

#in both functions above, value and Celcius are 'parameters'
#These are not like typical varaible, as theres no need to define a type
