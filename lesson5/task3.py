"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.
Задача:
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.
В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""
from collections import deque
from timeit import timeit


def extend_list1(lst, extend_list):
    for i in extend_list:
        lst.insert(0, i)


extend_list_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list = [i for i in range(10)]
my_deque = deque([i for i in range(10)])

print('Создание списков, list: ', timeit('my_list = [i for i in range(100)]', globals=globals()))
print('Создание списков, deque: ', timeit('my_deque = deque([i for i in range(100)])', globals=globals()))
print('Добавление в начало, list: ', timeit('my_list.insert(0, 0)', globals=globals(), number=100000))
print('Добавление в начало, deque: ', timeit('my_deque.appendleft(0)', globals=globals(), number=100000))
print('Добавление в конец, list: ', timeit('my_list.append(0)', globals=globals(), number=100000))
print('Добавление в конец, deque: ', timeit('my_deque.append(0)', globals=globals(), number=100000))
print('Удаление первого элемента, list: ', timeit('my_list.pop(0)', globals=globals(), number=100000))
print('Удаление первого элемента, deque: ', timeit('my_deque.popleft()', globals=globals(), number=100000))
print('Добавление списка в начало, list: ', timeit('extend_list1(my_list, extend_list_2)', globals=globals(), number=100000))
print('Добавление списка в начало, deque: ', timeit('my_deque.extend_list1(extend_list_2)', globals=globals(), number=100000))
print('Изменение первого элемента, list: ', timeit('my_list[0] += 1', globals=globals()))
print('Изменение первого элемента, deque:', timeit('my_deque[0] += 1', globals=globals()))

"""Создание списков, list:  4.452969810000001
Создание списков, deque:  5.3026560929999995
Добавление в начало, list:  3.492196162999999
Добавление в начало, deque:  0.011107859000000886
Добавление в конец, list:  0.01128814099999964
Добавление в конец, deque:  0.010497104999998896
Удаление первого элемента, list:  7.207801440999999
Удаление первого элемента, deque:  0.009513735999998829
"""

"""
В итоге списки отлично работают с концом, но не так хороши с началом,
а deque хорош везде.
"""
