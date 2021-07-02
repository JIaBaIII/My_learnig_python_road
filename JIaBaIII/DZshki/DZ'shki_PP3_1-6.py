# listok = 101
# while listok != 112:
#     if listok > 100:
#         print(f'давай чуть-чуть добавим. Сейчас {listok}')
#         listok += int(input())
#     if listok > 112:
#         print(f'Не, ну тут лучше убавить.. Сейчас {listok}')
#         listok -= int(input())
#     else:
#         if listok == 112:
#             print('Ого, уже 112 ниче себе, а давай-ка завново!!!...хехехеххе')
#             listok = listok - 13
#             break
# print('Выход')


# for i in range(1, 10):
# 	if i == 2:
# 		print(i)
# 	elif i == 3:
# 		print(i)
# 	elif i == 8:
# 		print(i)
# 	else:
# 		print('Хаксли')
# -------------------------------------------------------------------------------------------------------------------
# response_json = {
#     'result': [
#         {
#             'amount': 1115.00,
#             'currency': 'RUB'
#         },
#         {
#             'amount': 65.00,
#             'currency': 'EUR'
#         },
#         {
#             'amount': 25.00,
#             'currency': 'USD'
#         }
#     ]
# }
# summ = 0
# print(f'Сумма до изменений - {summ}')
# transactions = response_json['result']
# for transaction in transactions:
#     if transaction['currency'] == 'USD':
#         summ += transaction['amount'] * 70
#     elif transaction['currency'] == 'EUR':
#         summ += transaction['amount'] * 80
#     else:
#         summ += transaction['amount']
# print(f'Сумма после изменений - {summ}')
# -----------------------------------------------------------------------------------------------------------------
# my_new_list = list()
# my_old_list = [1, 5, 9, 10, 12]
# # my_new_list = [siska + 1 for siska in my_old_list if siska % 2 == 0]
# for siska in my_old_list:
#     if siska % 2 == 0:
#         my_new_list.append(siska + 1)
# print(my_new_list)
# -----------------------------------------------------------------------------------------------------------------
# spisok = [88, 11, 5, 0, 102]
# new_spisok = [soska + 1 for soska in spisok if type(soska) == int]
# print(new_spisok)
#
# # new_spisok_01 = [piska * 10 for piska in new_spisok if piska % 2 == 0]
# # print(new_spisok_01)
# ----------------------------------------------------------------------------------------------------------------
# list_01 = [1, 8, 'ну ёбана', 44, 1, 3]
# list_02 = [i for i in list_01 if type(i) == int]
# print(list_02)
# -----------------------------------------------------------------------------------------------------------------
#                                          пацанское програмирование 3 (домашка)
# № 1 (принять список и разбить на 2 списка чет\не чет)
# spisok = [int(i) for i in input().split(',')]
# spisok_delitsa = [num for num in spisok if num % 2 == 0]
# spisok_ne_delitsa = [num2 for num2 in spisok if num2 % 2 == 1]
# print(f'Список четных {spisok_delitsa}')
# print(f'Список не четных {spisok_ne_delitsa}')
# -----------------------------------------------------------------------------------------------------------------
# № 2 (Принимать с клавиатуры числа до тех пор, пока не будет введено слово “стоп”, вывести сумму всех введенных чисел)
# summa = 0
# stop_slovo = 'стоп'
# while True:
#     vvod_01 = input()
#     if vvod_01 == stop_slovo:
#         break
#     summa += int(vvod_01)
# print(summa)
# -----------------------------------------------------------------------------------------------------------------
# № 3 (Ввести число, делить его на 2 до тех пор, пока не получится число меньше 5, выводить все подитоги в консоль)
# vvod_s_klavi = int(input())
# while vvod_s_klavi >= 5:
#     vvod_s_klavi /= 2
#     print(vvod_s_klavi)
# -----------------------------------------------------------------------------------------------------------------
# № 4 (Ввести с клавиатуры список чисел, выводить каждое второе число из списка. Использовать continue!)
# доделать что бы нечетное не выдавало ошибку
# spisok_chisel = [int(i) for i in input().split(',')]
# indexioty = 0
# for spisok_chisel[indexioty] in spisok_chisel:
#     if indexioty % 2 != 0:
#         indexioty += 1
#         continue
#     indexioty += 1
#     print(spisok_chisel[indexioty])
# print(spisok_chisel[1::2])                                                  # Прикольнааа, вместо 7-ми строк =D
# -----------------------------------------------------------------------------------------------------------------
# № 5 (Ввести список чисел, суммировать числа до тех пор, пока подытог не будет больше или равен десяти.
#                                                                                                  Использовать break!)
# spisok_chisel = [int(i) for i in list(input())]
# summa = 0
# while True:
#     if summa < 10:
#         summa += spisok_chisel[0]
#         print(spisok_chisel)
#         print(summa)
#         del spisok_chisel[0]
#     else:
#         break
# print(summa)
# -----------------------------------------------------------------------------------------------------------------
# № 6 (Ввести слово. Получить все гласные буквы этого слова в отдельный список. Вывести результат в консоль)
# glas = ['а', 'е', 'ё', "и", 'о', 'у', 'ы', 'э', 'ю', 'я',]
# stringa = list(input())
# novii_list_glas = []
# for i in glas:
#     if i in stringa:
#         novii_list_glas.append(i)
# print(novii_list_glas)
# -----------------------------------------------------------------------------------------------------------------
#  № 7,8,9 в другом файле
