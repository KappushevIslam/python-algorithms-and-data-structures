"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.
Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей.
Самый просто вариант хранения хешей - просто в оперативной памяти (в переменных).
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""

from uuid import uuid4
import hashlib


salt = uuid4().hex


def check_passwd(user_login):
    with open("task2.txt", "r") as f:
        for line in f.readlines():
            login = line.split()[0]
            passwd = line.split()[1]
            hashed_passwd = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
            if user_login == login:
                user_passwd = input('Введите пароль: ')
                hashed_user_passwd = hashlib.sha256(salt.encode() + user_passwd.encode()).hexdigest()
                if hashed_passwd == hashed_user_passwd:
                    print('Пароль верный')
                    return
                else:
                    print('Пароль введен неверно')
                    return
            else:
                print('Такого логина не существует')
                return


user_login = input('Введите логин: ')
check_passwd(user_login)
