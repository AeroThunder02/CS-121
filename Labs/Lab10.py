######################################################
# Name   : Maciej Kowalczyk
# Pledge : I pledge my Honor that I have abided by the Stevens Honor System
######################################################
from cs5png import *

def mult(c,n):
    '''Given numbers c and n, return c*n, using only addition and lööps'''
    result = 0
    
    while n > 0:
        result = result + c
        n = n - 1
        
    return result    
    

def update(c,n):
    '''Given numbers c and n,
    return z where z(0, c) = z and z(n, c) = z(n-1, c)**2 + c,
    absolutely no recursion'''
    z = 0
    
    while n > 0:
        z = z**2 + c
        n = n - 1
        
    return z
    

def inMSet(c,n):
    '''Given a complex c and a number n, return if the magnitude of z
    never goes above 2 in the process of doing update(...). Don't(!)
    call update'''
    z = 0
    
    while z > 0:
        z = z * z + c
        if abs(z) > 2:
            return False
        return True
    
    return z

def weWantThisPixel( col, row ):
    """ a function that returns True if we want
    the pixel at col, row and False otherwise"""
    if col%10 == 0  or  row%10 == 0:
        return True
    else:
        return False
def test():
    """ a function to demonstrate how
     to create and save a png image"""
    width = 300
    height = 200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()
test()

def scale(pix, pixelMax, floatMin, floatMax):
    '''Given a pixel value, the max pixel value,
    return where that pixel lies on [floatMin, floatMax] where
    pix=0 -> floatMin and pix=pixelMax -> floatMax'''
    return floatMin + (floatMax - floatMin) * pix / pixelMax

def mset(n):
    '''Creates a 300x200 image of the Mandelbrot set, where
    the image is of the complex plane with x real [-2, 1] and y imaginary, [-i, i]'''
    width = 300
    height = 200
    image = PNGImage(width, height)

    for col in range(width):
        for row in range(height):
            x = scale(col, 300, -2, 1)
            y = scale(row, 200, -1, 1)
            c = x + y*1j
            if inMSet(c, n) == True:
                image.plotPoint(col, row)   #after looping through every single pixel, its then written to the file
    
    image.saveFile()
    
if __name__ == "__main__":
    iterations = 100 # Change this to play with the picture, once everything's working
    mset(iterations)
