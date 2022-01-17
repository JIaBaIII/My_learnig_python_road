from JIaBaIII.Docs.list_2D_practice import print_list_2d

# ********************************************************************************************************************
#                                          >>>>> LIST.something <<<<<
# ********************************************************************************************************************

spisok = [10, 9, 7, 6, 5]  # [10, 9, 7, 6, 5]
print(spisok)  # [10, 9, 7, 6, 5]
print(len(spisok))  # 5
spisok_strange = ['агуша', 4, 71, 'агуша', 9, 4, 4]


spisok.insert(2, 8)                                  # .insert
print(spisok)  # [10, 9, 8, 7, 6, 5]
print('-' * 80)

spisok_copy = spisok.copy()                          # .copy
print(spisok_copy)  # -||-
print('-' * 80)

spisok.sort()                                        # .sort
print(spisok)  # [5, 6, 7, 8, 9, 10]
print('-' * 80)

spisok.sort(reverse=True)                            # .sort(reverse=True)
print(spisok)  # [10, 9, 8, 7, 6, 5]
print('-' * 80)

spisok.pop(1)                                        # .pop
print(spisok)  # [10, 8, 7, 6, 5]
print('-' * 80)

if 6 in spisok:
    spisok.remove(6)                                 # .remove
    print(spisok)  # [10, 8, 7, 5]
print('-' * 80)

count = spisok_strange.count('агуша')                # .count
print(count)  # 2
print('-' * 80)

s = 'АБВГДЕ'
spisok_copy.extend(s)                                # .extend   Добавляет в список поэлементно
print(spisok_copy)  # [10, 9, 8, 7, 6, 5, 'А', 'Б', 'В', 'Г', 'Д', 'Е']
print('-' * 80)

index = spisok.index(8)                              # .index
print(index)  # 1
print('-' * 80)

spisok_copy.reverse()                                # .reverse
print(spisok_copy)  # ['Е', 'Д', 'Г', 'В', 'Б', 'А', 5, 6, 7, 8, 9, 10]
print('-' * 80)

spisok.clear()                                       # .clear
print(spisok)

# ********************************************************************************************************************
#                                          >>>>> Generator for <<<<<
# ********************************************************************************************************************

generate_list = [i for i in range(100)]  # Генератор значений для одномерного списка, записаный в 1 строчку в листе
print(generate_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ............... 98, 99]
print('-' * 80)

gen_2d_list = [[0 for i in range(5)] for j in range(5)]  # Генератор заполняет нулями поле 5х5
print_list_2d(gen_2d_list)
print('-' * 80)

gen_2d_list = [[j for i in range(3)] for j in range(3)]  # Генератор заполняет нулями 1 строку, единицами 2 и двойками
# 3 строку
print_list_2d(gen_2d_list)
print('-' * 80)

table_of_multiplication = [[(i * j) for i in range(1, 10)] for j in range(1, 10)]
print_list_2d(table_of_multiplication)                    # "Просто" таблица умножения =DDD
print('-' * 80)


# ********************************************************************************************************************
#                 >>>>> Разбить строку по символам - СТРОКА.split(СИМВОЛ, [maxsplit=ЧИСЛО] <<<<<
# ********************************************************************************************************************

# примеры:

a = 'Привет#, #Мир#!!'
a = a.split('#')
print(a)  # ['Привет', ', ', 'Мир', '!!']


b = 'Привет#, #Мир#!!'
b = b.split('#', maxsplit=1)
print(b)  # ['Привет', ', #Мир#!!']


c = 'Hi everyone!\nNeed to so sry\n And i!!'
c = c.split('\n')
print(c)
