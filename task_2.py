# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint
n = int(input('Введите количество элементов в массиве -> '))
list1 = []
for i in range(n):
    list1.append(randint(-10, 10))
print(list1)
minX = int(input('Введите минимальное значение диапазона -> '))
maxX = int(input('Введите максимальное значение диапазона -> '))
def diap(listA, minA, maxA):
    listB = []
    for i in range(len(listA)):
        if minA <= listA[i] <= maxA:
            listB.append(i)
    return listB
print(diap(list1, minX, maxX))

