"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.
Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается
И прошу вас обратить внимание, что то, что часто ошибочно называют генераторами списков,
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" - list comprehension.
"""
import timeit


# Сложность - O(N)
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# Сложность - O(N)
def func_2(nums):
    return [i for i, numbers in enumerate(nums) if numbers % 2 == 0]


nums_list = [i for i in range(10000)]

print(timeit.timeit("func_1(nums_list)", globals=globals(), number=1000))
print(timeit.timeit("func_2(nums_list)", globals=globals(), number=1000))  # На 30% быстрее

# func_1() - 1.6976770369999998
# func_2() - 1.209727711

# В итоге list comprehension быстрее, чем обычное заполнение списков через итератор
