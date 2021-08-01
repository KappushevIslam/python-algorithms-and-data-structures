"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух) разной!! сложности
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""

companies = {
    'google': 5000,
    'yandex': 3500,
    'apple': 800,
    'facebook': 4500,
    'space_x': 3750,
    'BMW': 5500,
    'microsoft': 7000,
    'amazon': 2000
}

# Первый способ
# Сложность: O(N log N)
companies_list = list(companies.items())
companies_list.sort(key=lambda l: l[1], reverse=True)
for i in range(3):
    print(companies_list[i][0], '-', companies_list[i][1])

# Второй способ
# Сложность - O(N)
companies_list2 = list(companies.items())
my_list = companies_list2[0]
result2 = []
for l in range(3):
    for i in companies_list2:
        if i[1] > my_list[1]:
            my_list = i
            companies_list2.remove(my_list)
    result2.append(my_list)

print(result2)


# Наилучшим из 2 вариантов является второй, так как затрачивается меньше времени на выполнение
# и отсутсвуют лишние сортировки
