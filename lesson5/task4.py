"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit

order_dict = OrderedDict({i: i for i in range(1000)})
common_dict = {i: i for i in range(1000)}
my_dict = {i: i for i in range(1, 500)}

print('Заполнение, OrderedDict: ', timeit('order_dict = OrderedDict({i: i for i in range(100)})', globals=globals(),
                                          number=1000))
print('Заполнение, dict: ', timeit('my_dict= {i: i for i in range(100)}', globals=globals(), number=1000))
print('Обращение по ключу, OrderedDict: ', timeit('order_dict[10]', globals=globals(), number=1000))
print('Оюращение по ключу, dict: ', timeit('common_dict[10]', globals=globals(), number=1000))
print('Копиование, OrderedDict: ', timeit('order_dict.copy()', globals=globals(), number=1000))
print('Копирование, dict: ', timeit('common_dict.copy()', globals=globals(), number=1000))
print('Обращение к элментам, OrderedDict: ', timeit('order_dict.items()', globals=globals(), number=1000))
print('Обращение к элементам, dict: ', timeit('common_dict.items()', globals=globals(), number=1000))
print('Обновление, OrderedDict: ', timeit('order_dict.update(my_dict)', globals=globals(), number=1000))
print('Обновление, dict:', timeit('common_dict.update(my_dict)', globals=globals(), number=1000))

"""
Заполнение, OrderedDict:  0.044017479
Заполнение, dict:  0.011870427000000003
Обращение по ключу, OrderedDict:  6.350900000000326
Оюращение по ключу, dict:  7.424699999999951
Копиование, OrderedDict:  0.11053857399999999
Копирование, dict:  0.00803951
Обращение к элментам, OrderedDict:  0.0001260529999999871
Обращение к элементам, dict:  0.00015444199999997688
Обновление, OrderedDict:  0.11338905899999999
Обновление, dict: 0.01877141900000001
"""

# В итоге OrderedDict иногда даже медленне, чем dict,
# а в целом примерно одинаково, поэтому нет смысла использовать первое.
