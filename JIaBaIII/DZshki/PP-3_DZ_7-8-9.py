import json

# № 7 (Дан словарь (см в конце документа) и список воспламеняемых объектов.
#              Нужно написать скрипт, который проверит все посылки на корректность параметра flammable (воспламеняемый).
#       Посылка считается воспламеняемой, если хотя бы один объект из списка package_items_ids есть в flammable_objects.
#                                                           Вывести в консоль все товары, которые доставлены корректно.)
flammable_objects = [123, 11, 22, 44, 234, 69]
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
}

# result01 = backend_response['result']
# for elem in result01:
#     for i in elem['package_items_ids']:
#         if set(elem['package_items_ids']) & set(flammable_objects) and elem['flammable'] == True:
#             print(f'Совпадения и True {elem["post_number"]}')
#             break
#         if not set(elem['package_items_ids']) & set(flammable_objects) and elem['flammable'] == False:
#             print(f'Нет совпадений и False {elem["post_number"]}')
#             break

# -----------------------------------------------------------------------------------------------------------------
# № 8 (Используя входные данные из задания 7 вернуть все посылки весом менее 2-х килограмм (вес в словаре указан в гр.)
# shtuka = backend_response['result']
# for element in shtuka:
#     if element['weight'] < 2000:
#         print(f'Посылки, весом меньше 2-х килограмм, {element["post_number"]}')
# -----------------------------------------------------------------------------------------------------------------
# № 9 (Используя словарь из задания 7, необходимо составить новый респонс, в котором будет список, состоящий из
#                post_number всех некорректных доставок и их общее число. (общее число должно идти вне списка доставок).
#                                           Теперь некорректными считаются еще и те, вес которых превышает 2 килограмма.
#                                                                Результат должен быть в формате json aka новый словарь

# result01 = backend_response['result']
# new_response = []
# new_response_01 = {'result': new_response}
# spisok_ne = []
#
# for elem in result01:
#     for i in elem['package_items_ids']:
#         if set(elem['package_items_ids']) & set(flammable_objects) and elem['flammable'] is True and \
#                 elem['weight'] < 2000:
#             break
#         if not set(elem['package_items_ids']) & set(flammable_objects) and elem['flammable'] is False and \
#                 elem['weight'] < 2000:
#             break
#     else:
#         spisok_ne.append(elem["post_number"])
#         new_response.append(elem)
#
# print(f'Некоректные доставоки -> \033[35m{spisok_ne}\033[0m, общим числом -> '
#       f'\033[1m\033[32m\033[3m{len(spisok_ne)}\033[0m')
#
# json_object = json.dumps(new_response_01, indent=4)
# print(json_object)
