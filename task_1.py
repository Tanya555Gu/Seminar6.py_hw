# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

a = int(input('Введите первый элемент арифметической прогрессии -> '))
d = int(input('Укажите разность -> '))
n = int(input('Количество выводимых элементов -> '))
def progr(a, d, n):
    ar_pr = []
    for i in range(n):
        ar_pr.append(a + d * i)
    print(ar_pr)
progr(a, d, n)
