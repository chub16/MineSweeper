#нужно унаследовать все переменные с bottom_field.py

#Создаем переменную поля с минимально возможным размером
row_top = []
field_top = []

#генерируем первую строку верхнего поля
while y > len(row_top):
   row_top.append('[]')

#генерируем игровое поле путем добавления строк
while x > len(field_top):
   field_top.extend([row_top])

