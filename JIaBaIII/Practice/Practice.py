# original = "EXAMPLE"
# removed = original.replace("E", "")
# print(removed)


# --------------------------------------------------------------------------------------------------------------------
# № 4


# def vvesti_pyfxtybt():
#     popitki = 3
#     while popitki != 0:
#         vvod = input('Введите целое число ')
#         if vvod.isnumeric() == int:
#             print('Вы молодец')
#             popitki -= 3
#             return int(vvod)
#         else:
#             popitki -= 1
#             print(f'Это не челое число, попробуйте снова. Попыток осталось -> {popitki}')
#     else:
#         print('Попытки кончились')
#
#
# vvesti_pyfxtybt()


def func_1(argument1, argument2):
    return argument1 - argument2


def func_2(drugoi_arg1, drugoi_arg2):
    return drugoi_arg1 + drugoi_arg2


print(func_1(func_1(10, 5), func_2(10, 5)))
