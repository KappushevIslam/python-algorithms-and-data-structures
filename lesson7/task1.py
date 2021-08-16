"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в
виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
from random import randint
from timeit import timeit


def bubble_sort1(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst)-n):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        n += 1
    return lst


def bubble_sort2(lst):
    n = 1
    while n < len(lst):
        changes_done = False
        for i in range(len(lst)-n):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                changes_done = True
        if not changes_done:
            return lst
        n += 1
    return lst


def bubble_sort3(lst):
    n = 1
    while n < len(lst):
        a = 0
        for i in range(len(lst)-n-a):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        a += 1
        n += 1
    return lst


numb_list = [randint(-100, 100) for i in range(100)]
sorted_list = sorted([i for i in range(-10, 10)], reverse=True)

print(timeit("bubble_sort1(numb_list[:])", globals=globals(), number=1000))  # 2.11839824
print(timeit("bubble_sort1(sorted_list[:])", globals=globals(), number=1000))  # 0.055058719999999894
print(timeit("bubble_sort2(numb_list[:])", globals=globals(), number=1000))  # 2.04256096
print(timeit("bubble_sort2(sorted_list[:])", globals=globals(), number=1000))  # 0.006890799999999864
print(timeit("bubble_sort3(numb_list[:])", globals=globals(), number=1000))  # 1.87531656
print(timeit("bubble_sort3(sorted_list[:])", globals=globals(), number=1000))  # 0.058017959999999924

# Результат есть, только если дать уже отсортированный список.
# Однако верятность такого случая ничтожна мала.
# Так же есть третий вариант, который чуть бустрее двух остальных.
# Смысл третьего метода - с каждой заменой делаем на одну итерацию прохода меньше,
# поэтому мы лишний раз не пробегаем по уже отсортированной части
