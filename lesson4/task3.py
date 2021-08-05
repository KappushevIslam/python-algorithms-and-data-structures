"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Обязательно предложите еще свой вариант решения и также запрофилируйте!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
Без аналитики задание считается не принятым
"""
from timeit import timeit
import cProfile


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


enter_num = int(input('Введите ваше число: '))
revers_1(enter_num, revers_num=0)
revers_2(enter_num, revers_num=0)
revers_3(enter_num)
revers_4(enter_num)


print(
    'Рекурсия: ',
    timeit(
        f'revers_1({enter_num})',
        globals=globals(),
        number=100000))
print(
    'Цикл: ',
    timeit(
        f'revers_2({enter_num})',
        globals=globals(),
        number=100000))
print(
    'Срез: ',
    timeit(
        f'revers_3({enter_num})',
        globals=globals(),
        number=100000))
print(
    'join + reverse: ',
    timeit(
        f'revers_4({enter_num})',
        globals=globals(),
        number=10000))

cProfile.run('revers_1(1000000000000)')
cProfile.run('revers_2(1000000000000)')
cProfile.run('revers_3(1000000000000)')
cProfile.run('revers_4(1000000000000)')

"""
Рекурсия:  0.13299816700000022
Цикл:  0.08686512299999993
Срез:  0.056186963000000034
join + reverse:  0.009539868000000062
четвертый метод оказалс самым быстрым,
так как используются внутренние функции.
Так же неплохое у среза, который оказался вторым
"""

