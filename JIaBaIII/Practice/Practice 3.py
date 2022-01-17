# 1

# print('\033[34mДавай начнем со дня твоего рождения. Когда он там?')
# your_day = int(input())
# print('\033[34mАга... А месяц какой? В виде двухзначного числа')
# your_month = input()
# print('\033[34mИиииии остался год. В виде 4-х значного числа')
# your_year = int(input())
# print(f'Что ж, данные для мфц готовы!! \033[35m{your_day}.{your_month}.{your_year}')
# print('\033[32m\Вы великолепны')

# 2(кривой)

# numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# huenic = input()
# sonic = list(huenic)
# print(sonic)
# if sonic[0] in numbers:
#     print(f'Ты песью инту написал \033[32m{huenic}')
# else:
#     print(f'Стрингист херов \033[35m{huenic}')

# 3 (типо 1 )------------------------------------------------------------------------

# a = int(input())
# b = int(input())
#
# if a > b:
#     print(f'\033[35m\033[1m\033[4m{a} > {b}')
# elif a < b:
#     print(f'\033[33m\033[1m\033[4m{a} < {b}')
# else:
#     print(f'\033[31m\033[1m\033[4m{a} = {b}')

# 4 (типо 2 )------------------------------------------------------------------------

# pervii = int(input())
# vtoroii = int(input())
#
# # if pervii is vtoroii+135:
# #     print('\033[35mYes')
# # elif vtoroii is pervii+135:
# #     print('\033[33mYes')
# # else:
# #     print('\033[31mNo')
#
# if abs(pervii - vtoroii) == 135:
#     print('сука блиат, получилось!! Разница ровно 135 и не важно с минусом или без')
# else:
#     print('ну ты и тупооооой, разница точно не 135!')

# 5 (типо 4 )------------------------------------------------------------------------

# print('Введите номер месяца от 1 до 12, а я скажу какой это сезон ;)')
# poszovatel = int(input())
# zima = 1, 2, 12
# vesna = 3, 4, 5
# leto = 6, 7, 8
# osen = 9, 10, 11
# if poszovatel in zima:
#     print('Холодно же, ты офигел зиму писать??')
# elif poszovatel in vesna:
#     print('Уже лучше, но чет слякотно весной-то...')
# elif poszovatel in leto:
#     print('Вооооот это збс, жаркое лееееето!!!')
# elif poszovatel in osen:
#     print('Ну такое себе, осенние дожди(((')
# else:
#     print(f'Ты чё, пёс? Такого месяца с номером \033[31m\033[1m{poszovatel}\033[0m -нет!'
#           f'Сказали же, от 1 до 12. Попробуй еще раз')

# 6 (типо 5 )------------------------------------------------------------------------

# print('Введите первое число')
# vvod_1 = int(input())
# print('Введите второе число')
# vvod_2 = int(input())
# print('Введите третье число')
# vvod_3 = int(input())
#
# if vvod_1 > 10 and vvod_2 > 10 and vvod_3 > 10:
#     print('\033[32mYes\033[0m, all your numbers are higher then 10! Good boy!')
# else:
#     print('\033[31mNo\033[0m, u lose=(')

# 7 (типо 6 )------------------------------------------------------------------------

# print('Введите 3 числа')
# count_plus = 0
# count_chisla = 0
# while count_chisla < 3:
#     dano_1 = int(input())
#     if dano_1 > 0:
#         count_plus += 1
#         count_chisla += 1
#     else:
#         count_chisla += 1
# print(f'Количество положительных чисел \033[35m{count_plus}')

# 7.1 (типо тоже 6 )------------------------------------------------------------------------

# print('Введите первое число')
# dano_1 = list(input())
# print('Введите второе число')
# dano_2 = list(input())
# print('Введите третье число')
# dano_3 = list(input())
# Polozi = 3-(dano_1+dano_2+dano_3).count("-")
# print(f'Кол-во положительных числел {Polozi}')

# 8 (типо 7 )------------------------------------------------------------------------

# print('Напишите сколько Вам полных лет')
# Data_age_year = int(input())
# print('Напишите сколько полных месяцев прошло с крайнего года до сегодняшего времени')
# Data_age_month = int(input())
# convert_year = Data_age_year*12*29
# convert_month = Data_age_month*29
# print(f'Вот столько \033[35m{convert_month + convert_year}\033[0m дней прошло за ваши'
#       f' {Data_age_year} лет(года) и {Data_age_month} месяцев(а)')

# 9 (типо 3 )------------------------------------------------------------------------

# print('Напишите число')
# cislo = int(input())
# if cislo > 100 or cislo < -100:
#     print("-")
# else:
#     print('+')
