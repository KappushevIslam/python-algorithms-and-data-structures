"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Массив в этом задании строить не нужно!
Нужно решить без него!
Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75
Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def find_sum(iterations, number, needed_iterations, summ):
    return summ if iterations == needed_iterations \
     else find_sum(iterations + 1, number / -2, needed_iterations, summ + number)


print(find_sum(0, 1, 3, 0))
