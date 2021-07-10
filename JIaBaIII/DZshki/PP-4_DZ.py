# № 1 (Написать функцию, которая рассчитывает факториал от принятого в нее целочисленного значения (n! или 1*2*3*4*…*n))

# def do_facto(some_munb):
#     rest = 1
#     for i in range(1, some_munb + 1):
#         rest *= i
#     print(rest)
#     return int(rest)


# do_facto(52)
# ---     ------      ---     ------      ---     ------      ---     ------      ---     ------      ---     ------
#  № 2 (Написать функцию, которая принимает в себя список функций и исполняет каждую из них)

# def f_for_use_words():
#     print('бедных негрятят пошли купаться в море, ')
#
#
# def f_for_use_words_2():
#     print(f'\033[32m{1}\033[0m из них ебанулся и пошел на концерт Аллы Пугачевы')
#
#
# def f_for_ret_num(hug):
#     rest = 1
#     for i in range(1, hug + 1):
#         rest *= i
#     print(f'\033[31m{rest - 1}\033[0m бедных негрятят остались купаться в море....')
#
#
# def ispolnit_func(*args):
#     for func in args:
#         func()
#
#
# ispolnit_func(do_facto(5), f_for_use_words, f_for_use_words_2, f_for_ret_num(5))  # ну хз конечно....

# --------------------------------------------------------------------------------------------------------------------
# № 3 (написать функцию, которая принимает в себя нефиксированное количество аргументов и считает,
#                                                             сколько было передано позиционных, а сколько  именованных

# def schitalochka_arg(*args, **kwargs):
#     counts_1 = 0
#     counts_2 = 0
#     for i in args:
#         counts_1 += 1
#     print(f'{counts_1} - \033[33mПозиционных\033[0m аргументов')
#     for i in kwargs:
#         counts_2 += 1
#     print(f'{counts_2} - \033[34mИменованных\033[0m аргументов')
#
#
# schitalochka_arg(12, 41, 55, 81, 11111111, some_day='твоя нога', you=1)

# --------------------------------------------------------------------------------------------------------------------
# № 4 (Написать две функции, одна возвращает результат ввода с клавиатуры и проверяет, что было передано целочисленное
# значение, в случае если нет, просит ввести еще раз и так пока не будет введено целочисленное значение или количество
# попыток не превысит три. Вторая будет принимать целочисленное значение и возвращать количество разрядов в этом числе.)

# def klava_vvod():
#     popitki = 3
#     while popitki > 0:
#         znachenie = input('Введите целочисленное значение ')
#         try:
#             if type(int(znachenie)) is int:
#                 print(f'Значение \033[35m{znachenie}\033[0m принято!')
#                 popitki -= 3
#                 return int(znachenie)
#         except ValueError:
#             popitki -= 1
#             print(f'Это явно не целочисленное значение, давай по новой...'
#                   f' Попыток осталось \033[31m{popitki}\033[0m')
#     else:
#         print(f'\033[3m\033[31mПопытки кончились. Это фиаско, братан.\033[0m')
#
#
# def kol_razradov(func):
#     i = 0
#     while type(func) == int:
#         if func > 9 or func != 0:
#             func //= 10
#             i += 1
#         else:
#             print(f'Количество разрядов -> {i}')
#             break
#     else:
#         print('\033[3m\033[36mНет тела - нет разрядов)\033[0m')
#
#
# kol_razradov(klava_vvod())

# --------------------------------------------------------------------------------------------------------------------

# № 5 (Написать функцию, которая возвращает глубину переданного в нее джейсона (глубину вложенных словарей, например
#                                                           {‘test': {‘test2':{‘test': 123}}} имеет глубину вложения 3)

# dict_01 = {'test': {'test2': {'test': 123}}}
# dict_06 = {'test': {'test': {'test': {'test': {'test': {'test': 123}}}}}}
backend_response = {
    'result': [
        {
            'post_number': 123352,
            'post_date': '2019-12-11',
            'package_items_ids': [
                1235,
                234,
                1234,
                432,
                15,
                11,
                2
            ],
            'city': 'Moscow',
            'country': 'Russia',
            'weight': 2100,
            'flammable': False,
            'status': 'arrived'
        },
        {
            'post_number': 12345,
            'post_date': '2019-12-11',
            'package_items_ids': [
                1235,
                1111,
                1234,
                432,
                15,
                2
            ],
            'city': 'Moscow',
            'country': 'Russia',
            'weight': 2100,
            'flammable': True,
            'status': 'arrived'
        },
        {
            'post_number': 43242,
            'post_date': '2019-12-11',
            'package_items_ids': [
                23,
                13,
                22,
                432,
                44,
                235,
                2
            ],
            'city': 'Moscow',
            'country': 'Russia',
            'weight': 2000,
            'flammable': False,
            'status': 'arrived'
        },
        {
            'post_number': 11125,
            'post_date': '2019-12-11',
            'package_items_ids': [
                43,
                11111,
                2,
                11,
                555,
                44,
                10
            ],
            'city': 'Moscow',
            'country': 'Russia',
            'weight': 3100,
            'flammable': True,
            'status': 'arrived'
        },
        {
            'post_number': 432423,
            'post_date': '2019-12-11',
            'package_items_ids': [
                324,
                532,
                3333,
                2345,
                22,
                115,
                2
            ],
            'city': 'Moscow',
            'country': 'Russia',
            'weight': 1150,
            'flammable': True,
            'status': 'arrived'
        },
        {
            'post_number': 32532,
            'post_date': '2019-12-11',
            'package_items_ids': [
                5436,
                7645,
                456,
                5357,
                34,
                54,
                3
            ],
            'city': 'Moscow',
            'country': 'Russia',
            'weight': 2100,
            'flammable': False,
            'status': 'arrived'
        },
        {
            'post_number': 2323,
            'post_date': '2019-12-11',
            'package_items_ids': [
                432,
                5435,
                6546,
                76,
                45,
                34,
                3
            ],
            'city': 'Moscow',
            'country': 'Russia',
            'weight': 1201,
            'flammable': True,
            'status': 'arrived'
        },
        {
            'post_number': 1111,
            'post_date': '2019-12-11',
            'package_items_ids': [
                654,
                345,
                44,
                765,
                9,
                5,
                1
            ],
            'city': 'Moscow',
            'country': 'Russia',
            'weight': 1100,
            'flammable': False,
            'status': 'arrived'
        },
        {
            'post_number': 576734,
            'post_date': '2019-12-11',
            'package_items_ids': [
                546,
                1111,
                645,
                754,
                22,
                765,
                54
            ],
            'city': 'Moscow',
            'country': 'Russia',
            'weight': 1234,
            'flammable': True,
            'status': 'arrived'
        }
    ]
}                                           # С третьего пацанского програмирования json спыздел


# def find_dict_dno(ny_pognali):
#     if isinstance(ny_pognali, dict):
#         return 1 + (max(map(find_dict_dno, ny_pognali.values())) if ny_pognali else 0)
#     return 0
#
#
# print(find_dict_dno(dict_01))

# --------------------------------------------------------------------------------------------------------------------
# № 6 (ULTRA HARD MODE: Написать функцию, которая принимает в себя два аргумента: response, который принимает в себя
# словарь, и return_type, который принимает в себя тип. Вернуть словарь, составленный из пар ключ/значение, таких,
#                                                   в которых тип значения совпадает с типом, переданным в return_type.

only_result = backend_response['result']
dictovshina = [{
            'post_number': 123352,
            'post_date': '2019-12-11',
            'package_items_ids': [
                1235,
                234,
                1234,
                432,
                15,
                11,
                2
            ],
            'city': 'Moscow',
            'country': 'Russia',
            'weight': 2100,
            'flammable': False,
            'status': 'arrived'
        },
        {
            'post_number': 12345,
            'post_date': '2019-12-11',
            'package_items_ids': [
                1235,
                1111,
                1234,
                432,
                15,
                2
            ],
            'city': 'Moscow',
            'country': 'Russia',
            'weight': 2100,
            'flammable': True,
            'status': 'arrived'
        }]

# def return_dict_by_type(response, return_type):
#     xena = -1
#     for elem in response:
#         xena += 1
#         for some_type in elem:
#             if type(response[xena][some_type]) == return_type:
#                 new_dict[some_type] = elem.values()
#     print(new_dict)
#
#
# return_dict_by_type(only_result, str)                         # Лютый пиздец тут наколдовал)


def take_dict_and_return(response, return_type):
    new_dict = {'result': 'Посмотрим на результат'}
    for elem in response:
        sikr = elem.items()
        print(type(sikr))
        for lift in sikr:
            print(type(lift))


take_dict_and_return(dictovshina, int)
