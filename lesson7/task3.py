"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.
Задачу можно решить без сортировки исходного
массива.
"""
import random
from statistics import median
from timeit import timeit


# ------- Метод без сортировки -------
def find_median1(lst):
    for i in range(len(lst) // 2):
        lst.remove(max(lst))
    return max(lst)


n1 = int(input('Введите n: '))
lst_obj = [random.randint(1, 1000) for i in range(2*n1+1)]
print(f'Исходный список - {lst_obj}\n'
      f'Медиана списка - {find_median1(lst_obj)}\n'
      f'Медиана через модуль statistics - {median(lst_obj)}')


# ------- Метод с сортировкой -------
# Нашёл этот метод быстрой сортировки в интернете
def quicksort(alist, start, end):
    if end - start > 1:
        p = partition(alist, start, end)
        quicksort(alist, start, p)
        quicksort(alist, p + 1, end)


def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while i <= j and alist[i] <= pivot:
            i = i + 1
        while i <= j and alist[j] >= pivot:
            j = j - 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j


n2 = int(input('Введите n: '))
alist = [random.randint(1, 1000) for j in range(2*n2+1)]
quicksort(alist, 0, len(alist))
print(f'Отсортированный список: {alist}\n', end='')
print(f'Медиана списка - {alist[n2]}\n'
      f'Медиана через модуль statistics - {median(alist)}')
print(timeit('quicksort(alist[:], 0, len(alist))', globals=globals(), number=1000000))

"""
Введите n: 4
Исходный список - [16, 3, 914, 297, 910, 43, 141, 415, 210]
Медиана списка - 210
Медиана через модуль statistics - 210

Введите n: 3
Отсортированный список: [70, 349, 471, 602, 650, 753, 876]
Медиана списка - 602
Медиана через модуль statistics - 602
16.10177044
"""
