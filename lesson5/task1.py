"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections.
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1
Предприятия, с прибылью ниже среднего значения: Фирма_2
"""
from collections import namedtuple
number_of_companies = int(input('Введите кол-во компаний: '))
companies_db = namedtuple('companies', 'company profit')
companies_list = []
for i in range(number_of_companies):
    company_name = input(f'Введите название {i+1}-го предпрития: ')
    company_profit = input(f'Введите прибыль {company_name}через пробел за 4 квартала: ')
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
print(f'Компании с годовой прибылью больше средней: {more_than_avg} \n'
      f'Компании с годовой прибылью ниже средней: {less_than_avg}')
