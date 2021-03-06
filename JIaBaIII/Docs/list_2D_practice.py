# ********************************************************************************************************************
#                                         >>>>> Двумерные списки <<<<<
# ********************************************************************************************************************
# Двумерные списки:

# journal = []  # Переменная для хранения наших списков в списке
# line = ["Ананасова Софья", 5, 0, 3, 0, 4]  # создаем список, как бы "нулевую строку"
# journal.append(line)  # Добавляем нашу "нулевую строку" в хранилище
# line = ["Вешняков Петр", 5, 0, 4, 0, 5]
# journal.append(line)  # используем ту же переменную line, она каждый раз будет перезаписываться новыми данными
# line = ["Герасимова Жанна", 0, 5, 5, 0, 5]
# journal.append(line)
# line = ["Журавлев Кирилл", 5, 0, 3, 2, 2]
# journal.append(line)
# line = ["Кровавый Кхорн", 5, 5, 5, 5, 5]
# journal.append(line)
#
# print(journal)
# print(journal[1][3])

#                                   Вариант 2 с .append
# journal_2 = []
# journal_2.append(["Ананасова Софья", 5, 0, 3, 0, 4])
# journal_2.append(["Вешняков Петр", 5, 0, 4, 0, 5])
# journal_2.append(["Герасимова Жанна", 0, 5, 5, 0, 5])
# journal_2.append(["Журавлев Кирилл", 5, 0, 3, 2, 2])
# journal_2.append(["Кровавый Кхорн", 5, 5, 5, 5, 5])
#
# print(journal_2)
# print(journal_2[1][3])

#                                   Вариант 3, при инициализации хранилища
# journal_3 = [["Ананасова Софья", 5, 0, 3, 0, 4],
#              ["Вешняков Петр", 5, 0, 4, 0, 5],
#              ["Герасимова Жанна", 0, 5, 5, 0, 5],
#              ["Журавлев Кирилл", 5, 0, 3, 2, 2],
#              ["Кровавый Кхорн", 5, 5, 5, 5, 5]]
#
# print(journal_3)

#                                          Красивый вывод данных
# for i in range(len(journal_3)):
#     print(journal_3[i][0],
#           journal_3[i][1],
#           journal_3[i][2],
#           journal_3[i][3],
#           journal_3[i][4],
#           journal_3[i][5])

#                                        Более красивый вывод данных
# for i in range(len(journal_3)):
#     for j in range(len(journal_3[i])):
#         print(f'{journal_3[i][j]}', end=' ')
#     print()

# --------------------------------------------------------------------------------------------------------------------
#                              Двумерные списки можно, аналогично одномерным - резать
# a = [10, 20, 30, 40, 50]
# print(a[3:5][1])  # пример слайса по выбранному промежутку. Тут слайс [3:5] возвращает [40, 50], а [1] тут это 50!

# list_2d = [[10, 11, 12, 13, 14],
#            [20, 21, 22, 23, 24],
#            [30, 31, 32, 33, 34]]
#
# print(list_2d[0:2][0][2:5])

# --------------------------------------------------------------------------------------------------------------------

#                                       Пишем метод для красивого вывода двумерных списков


def print_list_2d(lst):
    for elem in range(len(lst)):  # Формируем внешний цикл, для количества строк
        for eternal_elem in range(len(lst[elem])):  # Цикл до длинны текущей строки len[elem]
            # Выводим eternal_elem-тый элетемент elem-той строки, здесь
            # Возникакет перечисление 0 1, 0 2, 0 3 до последнего элемента,
            # После перечисление: 1 1, 1 2, 1 3 до последнего элемента
            # И так далее до последней строки
            print(f'{lst[elem][eternal_elem]}', end=' ')
        print()

# --------------------------------------------------------------------------------------------------------------------
# #  9                                    Задача по двумерным спискам при помощи input()
#
# n_strok = int(input('Введите количество строк: '))
# s_stolb = int(input('Введите количество столбцов: '))
#
# list_of_faith = []
#
# for i in range(n_strok):
#     list_of_faith.append([])
#     for j in range(s_stolb):
#         vvod = int(input(f'Задайте число для [{i}][{j}]: '))
#         list_of_faith[i].append(vvod)
#
# print_list_2d(list_of_faith)

# --------------------------------------------------------------------------------------------------------------------
