import bottom_field.py
import random

#Проверяем можем ли мы разместить все мины на поле
if mines_cnt >= (x * y):
    print("Мин больше чем клеток на поле")


#Функция генерирует случайную координату на поле
""" This function return coordinates of random cell
The first argument, which function return is a column number (x line coordinate)
The second arg is a line number (y line coordinate)"""

def random_cell(x, y):
    column = random.randint(0, x - 1)
    line = random.randint(0, y - 1)
    return column, line


#Минируем наше нижнее поле
i = 0
while i < mines_cnt:
    column, line = random_cell(x, y)
    
    #Проверяем не заминирована ли ячейка. 
    #Если мина есть - ничего не делаем 
    #Если мин нет то минируем ячейку и увеличиваем итератор.
    if field[line][column] == "*":
        None
    else:
        field[line][column] = "*"
        i += 1
