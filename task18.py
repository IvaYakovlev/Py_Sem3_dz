# Задача 18: Требуется найти в массиве A[1..N] самый 
# близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество 
# элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5


from random import randint
len1 = int (input("Введите длину списка"))
num = [randint(1, 100) for i in range (len1)]
print ("Список", *num)
x = int (input("К какому значению ближайшее найти: "))

min_diff = num [0]
for i in num:
    ran_current = abs(i-x)
    if ran_current < min_diff:
        res = i
        mid_diff = ran_current
print(f'Результат {res}')