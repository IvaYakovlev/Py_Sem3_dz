# Задача 16: Требуется вычислить, сколько раз встречается некоторое 
# число X в массиве A[1..N]. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1
from random import randint
len1 = int (input("Введите длину списка"))
num = [randint(1, 100) for i in range(len1)]
print ("Список", *num)
x = int (input("Какое число найти: "))

print (f'{x} встречается в списке {num.count(x)} раз')