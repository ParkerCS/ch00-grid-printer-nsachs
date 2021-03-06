# nice work.  Shouldn't need the print() statement between the calls.  This should be part of the function.

'''
Grid Printer Exercise
Printing a Grid (adapted from Downey, “Think Python”, ex. 3.5)

Goal:
Write a function that draws a grid like the following:

+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
hints
A couple features to get you started...

use print("+", end = " ") to print continuous line without carriage return

A print function with no arguments ends the current line and goes to the next line:

Simple string manipulation:
You can put two strings together with the plus operator:

"this" + "that" ===>  'thisthat'
Particularly useful if they have been assigned names:
plus = '+'
minus = '-'

You can also multiply strings:
'+' * 10 ===> '++++++++++'
'''

# just playing around and testing how I could create a some grids without functions.
print("This first box is just a test.")

print(("+" + (" -" * 4) + (" +" + (" -" * 4) + "+")))
print((("|" + (" " * 8)) * 2) + "|")
print((("|" + (" " * 8)) * 2) + "|")
print((("|" + (" " * 8)) * 2) + "|")
print((("|" + (" " * 8)) * 2) + "|")
print((" +" + (" -" * 4) * 2))
print((("|" + (" " * 8)) * 2) + "|")
print((("|" + (" " * 8)) * 2) + "|")
print((("|" + (" " * 8)) * 2) + "|")
print((("|" + (" " * 8)) * 2) + "|")
print(("+" + (" -" * 4) + "+") * 2)

print()

'''
Part 2
Making it more general

Make it a function
One of the points of writing functions is so you can write code that does similar things, but customized to input parameters. So what if we want to be able to print that grid at an arbitrary size?

Write a function print_grid(n) that takes one integer argument and prints a grid just like before, BUT the size of the grid is given by the argument.

For example,

print_grid(3) would print a small grid:

+ - + - +
|   |   |
+ - + - +
|   |   |
+ - + - +
print_grid(15) prints a larger grid:

+ - - - - - - - + - - - - - - - +
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
+ - - - - - - - + - - - - - - - +
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
|               |               |
+ - - - - - - - + - - - - - - - +
'''
# I struggled with getting the boxes all the right size (shrinking them)
def print_grid(n):
    for i in range(2):
        print("+" + ((" -" * int(n)) + " +") * 2, end=" ")
        print()
        for j in range(int(n)):
            print("|" + (("  " * int(n)) + " |") * 2, end = " ")
            print()
    print("+" + ((" -" * int(n)) + " +") * 2, end=" ")

print_grid(8)
print()
print_grid(3)
print()
print_grid(15)
print()

print()

'''
Part 3:
Even more general...

A function with two parameters
Write a function that draws a similar grid with a specified number of rows and columns, and each cell a given size.

for example, print_grid2(3,4) results in:

+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
|         |         |         |
|         |         |         |
|         |         |         |
|         |         |         |
+ - - - - + - - - - + - - - - +
What to do about rounding? – you decide.

Another example: print_grid2(5,3):

+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
|       |       |       |       |       |
|       |       |       |       |       |
|       |       |       |       |       |
+ - - - + - - - + - - - + - - - + - - - +
'''
def print_grid2(a, b):
    for j in range(int(a)): #a represenets the width/height dimensions
        print("+" + ((" -" * int(b)) + " +") * int(a), end = " ")
        print()
        for i in range(int(b)): #b represents the number of "-" or "|" in each smaller box
            print("|" + (("  " * int(b)) + " |")* int(a), end = " ")
            print()
    print("+" + ((" -" * int(b)) + " +") * int(a), end=" ")
    print()

print_grid2(3,4)
#print()
print_grid2(5, 3)
#print()

