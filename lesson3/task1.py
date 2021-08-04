"""
Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка
    и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

from time import time

my_list = []
my_dict = {}


def count_time_decorator(function):
    def count_time(*args, **kwargs):
        start_time = time()
        func = function(*args, **kwargs)
        end_time = time()
        print(f'Время выполнения функции - {end_time - start_time}')
        return func
    return count_time


@count_time_decorator
def append_list(list1, number):
    for i in range(number):
        list1.append(i)   # Сложность - O(1)


@count_time_decorator
def insert_list(list1, number):
    for i in range(number):
        list1.insert(0, i)   # Сложность - O(N)


@count_time_decorator
def fulfill_dictionary(dictionary, number):
    for i in range(number):
        dictionary[i] = i   # Сложность - O(1)


append_list(my_list, 100000)
insert_list(my_list, 100000)  # Значительно медленнее чем другие 2 функции
fulfill_dictionary(my_dict, 100000)


@count_time_decorator
def list_pop(list1):
    for i in range(100000):
        list1.pop(i)   # Сложность - O(N)


@count_time_decorator
def dict_pop(dictionary):
    for i in range(100000):
        dictionary.pop(i)   # Сложность -  O(1)


list_pop(my_list) # Значительно медленнее, чем со словарем
dict_pop(my_dict)
