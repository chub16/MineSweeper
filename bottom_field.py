x = input("Сколько клеток на поле по ширине ")
y = input("Какая высота поля? ")

#Меняем тип переменных из строки на числа
x = int(x)
y = int(y)

#Поле может быть построено только если размер осей х-у больше 0
if x < 0 or y < 0:
   print("Size of a field can not be less then 0!")
#Создаем переменную поля с минимально возможным размером
row = [0]
field = []

while y > len(row):
   row.extend([0])

field = [row]

while x > len(field):
   field.extend([row])

print(field)
