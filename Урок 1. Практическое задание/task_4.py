"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""


# 1) Линейная сложность O(n)
def users_auth_1(users, user_login, user_pass):
    pass_lst = []
    is_active_lst = []
    for el in list(users.values()):
        pass_lst.append(el[0])
        is_active_lst.append(el[1])
    if user_login not in list(users.keys()) or user_pass not in pass_lst:
        return 'Неверный логин или пароль'
    elif users[user_login][1]:
        return 'Вы вошли'
    else:
        return 'Пройдите регистрацию'


# 2) Константная сложность O(1)
def users_auth_2(users, user_login, user_pass):
    if users.get(user_login):
        if users.get(user_login)[0] != user_pass:
            return 'Неверный пароль'
        elif users.get(user_login)[0] == user_pass and users.get(user_login)[1]:
            return 'Вы вошли'
        else:
            return 'Пройдите регистрацию'
    else:
        return 'Неверный логин'


users = {'1': ['12345', True],
         '2': ['54321', False],
         '3': ['11111', False]
         }

user_login = input('Введите логин: ')
user_password = input('Введите пароль: ')
print(users_auth_1(users, user_login, user_password))
print(users_auth_2(users, user_login, user_password))

# Второе решение более эффективное, потому что имеет константную сложность O(n) -> быстрее отработает
