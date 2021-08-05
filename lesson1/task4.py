"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""

users_base = {'user1': {'password': '11111', 'activation': True},
            'user2': {'password': '22222', 'activation': False}
            }


# Первое решение
# Сложность - O(1)
def sign_in1(base_of_users, user_name, user_password):
    if base_of_users.get(user_name):
        if base_of_users[user_name]['password'] == user_password and base_of_users[user_name]['activation']:
            return 'Аутентификация успешно пройдена'
        elif base_of_users[user_name]['password'] != user_password:
            return 'Пароль неверный'
        elif base_of_users[user_name]['password'] == user_password and not base_of_users[user_name]['activation']:
            return 'Учетка не активирована. Следует пройти активацию'
    else:
        return 'Вы ввели не существуещего пользователя'


def sign_in2(base_of_users, user_name, user_password):
    for key, value in base_of_users.items:
        if key == user_name:
            if value['password'] == user_password and value['activation']:
                return 'Аутентификация успешно пройдена'
            elif value['password'] == user_password and not value['activation']:
                return 'Учетка не активирована. Следует пройти активацию'
            elif value['password'] != user_password:
                return 'Пароль неверный'
        else:
            return 'Вы ввели не существущего пользователя'
