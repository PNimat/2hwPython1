"""
Задание 4. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""

my_lst = list(map(int, input('Введите значения через пробел ').split()))
save = 0
step = 0

for i in my_lst:
    if (step + 1) % 2 == 1:
        save = my_lst[step]
        my_lst[step] = my_lst[step + 1]
        my_lst[step + 1] = save
    step += 1
print(my_lst)
