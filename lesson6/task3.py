"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
import memory_profiler
import timeit

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


@count_mem_and_time
def wrapped_reverse(n):
    """Функция делает реверс чисел. Получив 1234 вернет 4321 через рекурсию"""
    def reverse_number(number):
        return str(number) if number < 10 else str(number % 10) + reverse_number(number // 10)
    return reverse_number(n)


res, mem_diff, time_diff = wrapped_reverse(1234)
print(mem_diff)  # 0.0078125
print(res)  # 4321
print(time_diff)  # 3.611999999997284 sec

# Чтобы профилировать рекурсивную функцию требуется завернуть её в другую функцию
# и профилировать вторую. Ведь если этого не сделать, то память будет подсчитыватся снова
# и снова с каждым вызовом функции
