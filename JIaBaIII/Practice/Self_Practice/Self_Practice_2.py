# 1  Посчитать сумму чисел от 1 до 10000

# max_num = 10000
# summ = max_num * (max_num + 1) // 2  # ОЧЕНЬ ВАЖНАЯ ФОРМУЛА!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# print(summ)

# --------------------------------------------------------------------------------------------------------------------
# 2   .isdigit() - если переменнная состоит только из цифр десятичной системы, возвращает True, иначе False

# perem = ''
# while perem.isdigit():
#     perem = int(input("Введите целове число: "))
# perem = int(perem)

#   -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----
# 3   проверить, что вводимые цифры в пределах от 0 до 9 включительно, при помощи кодов символа ord()

# def is_it_digit(arg1):
#     res = True
#     start_code = ord('0')
#     stop_code = ord('9')
#     p = 0
#     while p < len(arg1) and res:
#         if ord(arg1[p]) < start_code or ord(arg1[p]) > stop_code:
#             res = False
#         p += 1
#     return res
#
#
# stoka = '123456789'
# print(f'Состоит лм строка {stoka} только из цифр (True) или в ней есть символы (False)?')
# print(f'Функция вернула: {is_it_digit(stoka)}')
#
# stoka = '123.89123'
# print(f'Состоит лм строка {stoka} только из цифр (True) или в ней есть символы (False)?')
# print(f'Функция вернула: {is_it_digit(stoka)}')
#
# stoka = 'Я строка! ЛЮБИ МЕНЯ!!!'
# print(f'Состоит лм строка {stoka} только из цифр (True) или в ней есть символы (False)?')
# print(f'Функция вернула: {is_it_digit(stoka)}')
#
# start = ord('0')
# for i in range(10):
#     print(f'{chr(start + i)} = {start + i}')

#   -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----
# 4 Написать функцию, которая однозначно определит: вещественное число или нет. В вещественном может быть только
#  одна точка, остальное цифры

# example = '541.3462724'
#
#
#
# def is_it_digit_thing(arg1):
#     res = True
#     look = ord('/')
#     start_code = ord('.')
#     stop_code = ord('9')
#     p = 0
#     while p < len(arg1) and res:
#         if ord(arg1[p]) < start_code or ord(arg1[p]) > stop_code or ord(arg1[p]) == look:
#             res = False
#         p += 1
#     return res
#
#
# print(f'Состоит лм строка {example} только из цифр и точки (True) или в ней есть символы (False)?')
# print(f'Функция вернула: {is_it_digit_thing(example)}')

# --------------------------------------------------------------------------------------------------------------------
# 5 Нужно сделать выборку из строки, возвращая почищенную от ненужных символов строку.

# code_list = []
# list_1 = ''
# for i in 'WASDE0123':
#     code_list.append(ord(i))
#
# # print(code_list)
#
# command = input('Ведите команды Копатыча: ')
#
# for i in command:
#     if i.lower():
#         list_1 += i.upper()
#
# clean_command = ''
#
# for i in list_1:
#     if ord(i) in code_list:
#         clean_command += i
#
# print(f'Очищенная командная строка: {clean_command}')

# --------------------------------------------------------------------------------------------------------------------
# 6 Написать программу, которая считывает данные из файла и подсчитывает среднее арифметическое среди оценок
# каждого ученика. Вывод данных: фамилия и имя, далее среденяя оценка.

# def get_data(filename):
#     ret = []
#
#     try:
#         f = open(filename, 'r', encoding='utf-8')
#         for line in f.readlines():
#             line = line.replace('\n', '')
#             line = line.split('#')
#             ret.append(line)
#         f.close()
#     except:
#         print('Ошибка открытия файла! Убедитесь, что путь до него и имя файла верны.')
#
#     return ret
#
#
# def get_average(arg1):
#     summa = 0
#     count = 0
#
#     for i_elem in range(1, len(arg1)):
#         if arg1[i_elem].isdigit():
#
#             summa += int(arg1[i_elem])
#             count += 1
#
#     student = summa / count
#     student = int(student * 10) / 10
#     return student
#
#
#   -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----
# # Формирует в возвращает текст для записи в файл
# def get_string_to_file(arr):
#     ret = ''
#
#     for elem in range(len(arr)):
#         ret += arr[elem][0] + '#' + str(get_average(arr[elem])) + '\n'
#
#     return ret
#
#
#   -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----
# #  Записывает переданную информацию в файл
# def save_to_file(str_to_file, students_average_score):
#     try:
#         some_file = open(students_average_score, 'w', encoding='utf-8')
#         some_file.write(str_to_file)
#         some_file.close()
#     except:
#         print('Ошибка создания файла')
#
#
#   -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----
# #  основная функция
# journal = get_data('Students.dat')
# for i in range(len(journal)):
#     print(f'{journal[i][0]}, средняя оценка {get_average(journal[i])}')
#
# save_to_file(get_string_to_file(journal), 'average.dat')

# --------------------------------------------------------------------------------------------------------------------
# 7 Создаем новый файл с рандомными числами от 10 до 99

# import random
#
# n = 100
#
# try:
#     file_1 = open('test.txt', 'a', encoding='utf-8')
#
#     for i in range(n):
#         file_1.write(str(random.randint(10, 99)) + ' ')
#
#     file_1.close()
# except:
#     print('не получилось :(')

# --------------------------------------------------------------------------------------------------------------------
