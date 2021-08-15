"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).
И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...
Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
from timeit import timeit
lst = [3, 9, 1, 8, 4, 26, 5, 1, 136]


def merge(left_side, right_side):
    fin_list = []
    i = 0
    j = 0
    while i < len(left_side) and j < len(right_side):
        if left_side[i] <= right_side[j]:
            fin_list.append(left_side[i])
            i += 1
        else:
            fin_list.append(right_side[j])
            j += 1
    fin_list += left_side[i:] + right_side[j:]
    return fin_list


def merge_sort(a):
    if len(a) <= 1:
        return a
    else:
        left = a[:len(a) // 2]
        right = a[len(a) // 2:]
    return merge(merge_sort(left), merge_sort(right))


nums = int(input("Введите число элементо в массиве: "))
nums_list = [random.random() + random.randint(0, 50) for _ in range(nums)]
nums_list = sorted(nums_list, reverse=True)
print(f"Исходный: {nums_list}\n"
      f"Отсортированный: {merge_sort(nums_list)}")

nums_list1 = [random.random() + random.randint(0, 50) for _ in range(10)]
nums_list2 = [random.random() + random.randint(0, 50) for _ in range(100)]
nums_list3 = [random.random() + random.randint(0, 50) for _ in range(1000)]

print(f'10 элементов: '
      f'{timeit("merge_sort(nums_list1[:])", globals=globals(), number=1000)}')
# 10 элементов: 0.05100428
print(f'100 элементов: '
      f'{timeit("merge_sort(nums_list2[:])", globals=globals(), number=1000)}')
# 100 элементов: 0.60060456
print(f'1000 элементов: '
      f'{timeit("merge_sort(nums_list3[:])", globals=globals(), number=1000)}')
# 1000 элементов: 8.42992432
