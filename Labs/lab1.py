from lab1_functions import draw_shape, check_num, check_magnitude
from math import sqrt
    
# Task 0: Print your name and honor pledge
print("Maciej Kowalczyk")
print("I pledge my Honor that I have abided by the Stevens Honor Code")

# Task 1: Mathematical operations ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Change the (+) operators to make 'num' equal to 1

# 'num' will store the result of the calculation
num = 4 - 4 + 4 / 4
check_num(num)

# Task 2: Vector magnitude ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Calculate the magnitude of a 2D vector
# Note: 'x' and 'y' represent coordinates in a vector < x, y >
# Hint: sqrt(4) performs a square root on 4 and returns 2

x = 140.15
y = 144.75
solution = sqrt((x**2 + y**2))

# Replace 1.0 with your final answer
magnitude = solution
check_magnitude(magnitude)

# Task 3: Drawing shapes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Define a list of coordinates to draw some shapes

# Here's an isosceles triangle as an example
draw_shape([
    (-100, 0),
    (100, 0),
    (0, 300),
    (-100, 0)
])

# 3.1: Equilateral triangle
draw_shape([
    (-100,0),
    (100,0),
    (0,175),
    (-100,0)

])

# 3.2: Square
draw_shape([
    (-50,0),
    (50, 0),
    (50,100),
    (-50,100),
    (-50,0)
    
])

# 3.3: Any shape with 5+ vertices
draw_shape([
    (-25,0),
    (25,0),
    (75,50),
    (50,100),
    (0,125),
    (-50,100),
    (-75,50),
    (-25,0)
    
    
])
