import memory_profiler
from sys import getsizeof
from numpy import array
import timeit
from collections import namedtuple
from recordclass import recordclass


def count_mem_and_time(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        t1 = timeit.default_timer()
        res = func(*args)
        t2 = timeit.default_timer()
        m2 = memory_profiler.memory_usage()
        time_diff = f'{t2 - t1} sec'
        mem_diff = m2[0] - m1[0]
        return res, str(mem_diff) + ' MiB', time_diff
    return wrapper


# ----- Скрипт 1 -----

@count_mem_and_time
def gen1():
    a = [i for i in range(1000000)]
    b = []
    for i in a:
        i += 1
        b.append(i)
    return b  # 39.82421875 MiB 0.64365864 sec


@count_mem_and_time
def gen2():
    a = [i for i in range(1000000)]
    b = []
    for i in a:
        i += 1
        b.append(i)
    yield b  # 0.0078125 MiB 1.399999999995849 sec


@count_mem_and_time
def gen3():
    a = [i for i in range(1000000)]
    b = []
    for i in a:
        i += 1
        b.append(i)
    return array(b)  # 3.9375 MiB 0.8204824 sec


# Получатеся экономия в ~5000 раз, использовав вместо return yield.
# То есть теперь мы получаем результат функции по запросу, жертвую при этом временем.
# При использовании модуля numpy экономия в 10 раз, что тоже весьма неплохо.
# А по времени с numpy выходит почти в 2 раза меньше времени, чем с генератором.

# ----- Скрипт 2 -----
"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


# Было так
class HexNumber1:
    def __init__(self, num):
        self.num = list(num)

    def __add__(self, other):
        return ''.join(list(hex(int(''.join(self.num), 16) + int(''.join(other.num), 16)))[2:]).upper()

    def __mul__(self, other):
        return ''.join(list(hex(int(''.join(self.num), 16) * int(''.join(other.num), 16)))[2:]).upper()


# Стало
class HexNumber2:
    __slots__ = array(['num'])

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return ''.join(list(hex(int(''.join(self.num), 16) + int(''.join(other.num), 16)))[2:]).upper()

    def __mul__(self, other):
        return ''.join(list(hex(int(''.join(self.num), 16) * int(''.join(other.num), 16)))[2:]).upper()


x1 = HexNumber1('A2')
y1 = HexNumber1('C4F')
x2 = HexNumber2('A2')
y2 = HexNumber2('C4F')
print(f'Сумма чисел: {x1+y1}\nПроизведение чисел: {x1*y1}')
print(f'Сумма чисел: {x2+y2}\nПроизведение чисел: {x2*y2}')
print(f'Размер - {getsizeof(x1.__dict__)}')   # Размер - 104
print(f'Размер - {getsizeof(x2.__slots__)}')   # Размер - 64

# В итоге словарь оказался экономнее на 60%.
# Так как словари весят очень много из-за борьбы с коллизиями,
# разумнее использовать список

# ----- Скрипт 3 -----
"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


# Было:
class DivisionToNull1:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_to_null(divider, denominator):
        if denominator == 0:
            return f"Деление на ноль недопустимо"
        return divider / denominator


class DivisionToNull2:
    __slots__ = ['divider', 'denominator']

    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_to_null(divider, denominator):
        if denominator == 0:
            return f"Деление на ноль недопустимо"
        return divider / denominator


d1 = DivisionToNull1(5, 5)
print(getsizeof(d1.__dict__))  # 104 b
d2 = DivisionToNull2(5, 5)
print(getsizeof(d2.__slots__))  # 72 b

# По тем же причинам использование __slots__ будет оптимизировать память

# ----- Скрипт 3 -----
"""
Урок 5, задание 1. Пользователь вводит данные о количестве предприятий, их наименования
и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

# Было
def var1():
    number_of_companies = int(input('Введите кол-во компаний: '))
    companies_db = namedtuple('companies', 'company profit')
    companies_list = []
    for i in range(number_of_companies):
        company_name = input(f'Введите название {i+1}-го предпрития: ')
        company_profit = input(f'Введите прибыль {company_name} через пробел за 4 квартала: ')
        companies_list.append(companies_db(company_name, sum(list(map(lambda x: int(x), company_profit.split(maxsplit=3))))))
        avg_profit = 0
    for q in companies_list:
        avg_profit += q.profit
    avg_profit //= number_of_companies
    print(f'Средняя годовая прибыль всех компаний - {avg_profit}')
    more_than_avg = []
    less_than_avg = []
    for s in companies_list:
        if s.profit > avg_profit:
            more_than_avg.append(s)
        else:
            less_than_avg.append(s)
    print(f'Размер с namedtuple - {getsizeof(companies_list)}')
    print(f'Компании с годовой прибылью больше средней: {more_than_avg} \n'
          f'Компании с годовой прибылью ниже средней: {less_than_avg}')


# Стало
def var2():
    number_of_companies = int(input('Введите кол-во компаний: '))
    companies_db = recordclass('companies', 'company profit')
    companies_list = []
    for i in range(number_of_companies):
        company_name = input(f'Введите название {i+1}-го предпрития: ')
        company_profit = input(f'Введите прибыль {company_name} через пробел за 4 квартала: ')
        companies_list.append(companies_db(company_name, sum(list(map(lambda x: int(x), company_profit.split(maxsplit=3))))))
        avg_profit = 0
    for q in companies_list:
        avg_profit += q.profit
    avg_profit //= number_of_companies
    print(f'Средняя годовая прибыль всех компаний - {avg_profit}')
    more_than_avg = []
    less_than_avg = []
    for s in companies_list:
        if s.profit > avg_profit:
            more_than_avg.append(s)
        else:
            less_than_avg.append(s)
    print(f'Размер с recordclass - {getsizeof(companies_list)}')
    print(f'Компании с годовой прибылью больше средней: {more_than_avg} \n'
          f'Компании с годовой прибылью ниже средней: {less_than_avg}')


# var1 - 88 b
# var2 - 88 b
# recordclass и namedtuple дали одинаковый результат.
# Возможно, что-то не так в моём коде.
