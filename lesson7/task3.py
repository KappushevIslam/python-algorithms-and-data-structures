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
def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot - 1)
        _quicksort(array, pivot + 1, end)

    return _quicksort(array, begin, end)


n2 = int(input('Введите n: '))
alist = [random.randint(1, 1000) for j in range(2*n2+1)]
quick_sort(alist)
print(f'Отсортированный список: {alist}\n', end='')
print(f'Медиана списка - {alist[n2]}\n'
      f'Медиана через модуль statistics - {median(alist)}')

print(timeit('quick_sort(alist[:])', globals=globals(), number=1000000))
print(timeit('find_median1(lst_obj[:])', globals=globals(), number=1000000))
print(timeit('median(alist[:])', globals=globals(), number=1000000))


"""
Введите n: 4
Исходный список - [16, 3, 914, 297, 910, 43, 141, 415, 210]
Медиана списка - 210
Медиана через модуль statistics - 210

Введите n: 3
Отсортированный список: [70, 349, 471, 602, 650, 753, 876]
Медиана списка - 602
Медиана через модуль statistics - 602

9.29877296 - quick_sort
2.773033999999999 - find_median
1.53841624 - median

Median быстрее остальных. Своя свобственная функция тоже весьма неплоха.
А решение через быструю сортировку наиболее большое и медленное.
"""
