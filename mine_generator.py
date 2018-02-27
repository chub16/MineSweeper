#import bottom_field.py
import random


##Testing input
field = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
x = 4
y = 4
mines_cnt = 5


#check mines conut !> size of field
if mines_cnt >= (x * y):
    print("mines > then field")


#coordinate random function

""" This function return coordinates of random cell
The first argument, which function return is a column number (x line coordinate)
The second arg is a line number (y line coordinate)"""

def random_cell(x, y):
    column = random.randint(0, x - 1)
    line = random.randint(0, y - 1)
    return column, line


#insert mines into bottom field
i = 0
while i < mines_cnt:
    #check is already mine present?
    column, line = random_cell(x, y)
    if field[line][column] == "*":
        None
    else:
        field[line][column] = "*"
        i += 1

