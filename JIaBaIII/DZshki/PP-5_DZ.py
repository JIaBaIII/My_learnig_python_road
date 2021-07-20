# 1 Написать класс, имеющий статические и нестатические поля. А также гет методы, возвращающие не статические поля
# класса (для каждого поля свой)

# class SomeInterestingClass:
#     static_field_01 = 42
#     static_field_02 = '- Ответ на главный вопрос жизни, пространства и всего'
#
#     def __init__(self, n1, n2):
#         self.not_static_field_1 = n1
#         self.not_static_field_at_all = n2
#
#     def get_n1(self):
#         return self.not_static_field_1
#
#     def get_n2(self):
#         return self.not_static_field_at_all
#
#     def set_n1(self, new_n1):
#         self.not_static_field_1 = new_n1
#
#     def set_n2(self, new_n2):
#         self.not_static_field_at_all = new_n2
#
#
# sic = SomeInterestingClass(4, 2)
# print(sic.static_field_01, sic.static_field_02)
# print((sic.get_n1() * sic.get_n2()) // 10)
# sic.set_n1('-Можно Машку')
# sic.set_n2('За ляшку!')
# print(f'Можна? {sic.get_n1()} {sic.get_n2()}')

# --------------------------------------------------------------------------------------------------------------------
# 2 Дан класс Pupil
# Добавьте метод, который позволит ученику забыть какую то часть знаний (не все сразу).

# class Pupil:
#     def __init__(self):
#         self.knowledge = []
#
#     def take(self, info):
#         self.knowledge.append(info)
#         print(self.knowledge)
#
#     def forget(self):
#         self.knowledge.pop()
#         print(self.knowledge)
#
#
# pupil = Pupil()
#
# pupil.take(123)
# pupil.take(88)
# pupil.take(0)
# pupil.take(16)
#
# pupil.forget()
# pupil.forget()
# pupil.forget()
# pupil.forget()

# --------------------------------------------------------------------------------------------------------------------
# 3 Дан класс Кошка. Кошка имеет вес, имя и пол. Переопределить магический метод __add__() таким образом, чтобы при
# сложении двух кошек (и только кошек!), в случае если они противоположного пола получалась новая кошка, имеющая
# половину от среднего веса родителей и имя, состоящее из имен родителей. Пол должен выбираться в зависимости от левого
# аргумента сложения.
# При попытке сложить двух однополых кошек, в консоль должно выводиться сообщение о неприемлимости навязывания
# гомосексуализма котятам и возвращаться None.

# class Cat:
#     def __init__(self, name, sex, weight):
#         self.name = name
#         self.sex = sex
#         self.weight = weight
#
#     def __str__(self):
#         if self.sex == 'male' or self.sex == 'M' or self.sex == 'm':
#             return 'Кошак (Имя: {}, Пол: {}, Вес: {} гр.)'.format(self.name, self.sex, self.weight)
#         else:
#             return 'Кошка (Имя: {}, Пол: {}, Вес: {} гр.)'.format(self.name, self.sex, self.weight)
#
#     def __add__(self, gen2):
#         if self.sex == gen2.sex:
#             print('Мы тут таких не любим... Котятки могут быть только у гетеро пары, попробуй еще')
#             return None
#         else:
#             if self.sex == 'male' or self.sex == 'M' or self.sex == 'm':
#                 child_name_start = gen2.name[:3]
#                 child_name_end = self.name[-3:]
#                 return Cat(child_name_start + child_name_end, self.sex, int((self.weight + gen2.weight) / 2))
#             else:
#                 child_name_start = gen2.name[:3]
#                 child_name_end = self.name[-4:]
#                 return Cat(child_name_start + child_name_end, self.sex, int((self.weight + gen2.weight) / 2))
#
#
# cat_1 = Cat('Эпифинья', 'female', 1000)
# cat_2 = Cat('Сучок', 'male', 10000)
#
# print(cat_1)
# print(cat_2)
# print(f'Котенок: {cat_1 + cat_2}')

# --------------------------------------------------------------------------------------------------------------------
# 4 Написать программу, которая будет сравнивать произвольное количество кошек и сортировать их в порядке возрастания
# по параметру вес. Эффективность - поебать, но чем больше тем лучше.

# import emoji
# import random
#
# # import random
# #
# #
# # class RandomCatAmount:
# #     def __init__(self, arg1, weight=None):
# #         self.weight = weight
# #         self.arg1 = arg1
# #
# #     def __int__(self):
# #         list_of_cats = []
# #         if self.weight is None:
# #             for new_cat in range(0, self.arg1):
# #                 weight = random.randint(2000, 10000)
# #                 list_of_cats.append(weight)
# #         return list_of_cats
# #
# #
# # def comb_sort(list_of_smth):                                             # Вангую - Успешный успех. Я и сам в шоке..
# #     len_of = len(list_of_smth)
# #     step = (len_of * 10 // 13) if len_of > 1 else 0
# #     while step:
# #         if step < step < len_of:
# #             step = len_of
# #         swapped = False
# #         for i in range(len_of - step):
# #             if list_of_smth[i + step] < list_of_smth[i]:
# #                 list_of_smth[i], list_of_smth[i + step] = list_of_smth[i + step], list_of_smth[i]
# #                 swapped = True
# #         step = (step * 10 // 13) or swapped
# #
# #
# # rca = RandomCatAmount(20)
# # list_of_some_cats = rca.__int__()
# # comb_sort(list_of_some_cats)
# # print(list_of_some_cats)                                                      # Супер ванильное решение
#
#   -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----
#
# class RandomCatAmount:
#     def __init__(self, arg1, weight=None):
#         self.weight = weight
#         self.arg1 = arg1
#
#     def __int__(self):
#         list_of_cats = []
#         if self.weight is None:
#             for new_cat in range(0, self.arg1):
#                 weight = random.randint(2000, 10000)
#                 list_of_cats.append(weight)
#         return list_of_cats
#
#     def __getitem__(self, item):
#         return int(self.arg1)
#
#
# def point_origin_pussy(arg3):                                            # Еще чуть-чуть добавочноый функции
#     new_dict = {}
#     for every_cat in range(len(arg3)):
#         every_orig_cats = every_cat + 1
#         # print(emoji.emojize(f'{arg3[every_cat]} <- :cat: была {every_orig_cats}', variant='emoji_type'))
#         new_dict[f'{arg3[every_cat]}'] = f'{every_orig_cats}'
#     return new_dict
#
#
# def point_pussy(arg2):                                                   # Добавочная функция
#     for every_cat in range(len(arg2)):
#         every_cats = every_cat + 1
#         cat_elem = arg2[every_cat]
#         print(emoji.emojize(f"{cat_elem} <- Эта :cat: {every_cats} в списке!"
#                             f" (А была {origin_dict[f'{cat_elem}']})"))
#         del origin_dict[f'{cat_elem}']
#
#
# rca = RandomCatAmount(20)
#
#
# def comb_sort(list_of_smth):                                            # Вангую - Успешный успех. Я и сам в шоке..
#     len_of = len(list_of_smth)
#     step = (len_of * 10 // 13) if len_of > 1 else 0
#     while step:
#         if step < step < len_of:
#             step = len_of
#         swapped = False
#         for i in range(len_of - step):
#             if list_of_smth[i + step] < list_of_smth[i]:
#                 list_of_smth[i], list_of_smth[i + step] = list_of_smth[i + step], list_of_smth[i]
#                 swapped = True
#         step = (step * 10 // 13) or swapped
#
#
# list_of_some_cats = rca.__int__()
# origin_dict = point_origin_pussy(list_of_some_cats)
# comb_sort(list_of_some_cats)
# point_pussy(list_of_some_cats)

# --------------------------------------------------------------------------------------------------------------------
# 5  Hard Mode. Задачу нагло спиздил, если честно, но она клевая.
# Напишите программу по следующему описанию. Есть класс "Warrior". От него создаются два экземпляра-юнита.
# Каждому устанавливается здоровье в 100 очков. В случайном порядке они бьют друг друга. Тот, кто бьет, здоровья
# не теряет. У того, кого бьют, оно уменьшается на 20 очков от одного удара. После каждого удара надо выводить
# сообщение, какой юнит атаковал, и сколько у противника осталось здоровья. Как только у кого-то заканчивается ресурс
# здоровья, программа завершается сообщением о том, кто одержал победу.

# import random
#
#
# class Warrior:
#     def __init__(self, name, hp=100):
#         self.name = name
#         self.hp = hp
#
#     def __and__(self, other):
#         while self.hp > 0 and other.hp > 0:
#             turn = random.randint(1, 2)
#             print(turn)
#             if turn == 1:
#                 other.hp -= 20
#                 print(f' Бесстрашный воин {self.name} бьет беднягу \033[35m{other.name}\033[0m на 20 единиц урона!!!!'
#                       f' Отчего у \033[35m{other.name}\033[0m остается \033[35m{other.hp}\033[0m здоровья')
#             elif turn == 2:
#                 self.hp -= 20
#                 print(f'Ооооох, {other.name} совершает сокрушительную атаку, отнимая у \033[34m{self.name}\033[0m'
#                       f' целых 20 единиц '
#                       f' урона!!! Напряжение наростает, в то время как у \033[34m{self.name}\033[0m осталось'
#                       f' \033[34m{self.hp}\033[0m здоровья')
#         else:
#             if self.hp > other.hp:
#                 print(f' У нас победиль !! \033[34m{self.name}\033[0m устоявший на ногах с'
#                       f' \033[34m{self.hp}\033[0m запасом здоровья!')
#             else:
#                 print(f'У нас победиль !! \033[35m{other.name}\033[0m устоявший на ногах с'
#                       f' \033[35m{other.hp}\033[0m запасом здоровья!')
#
#
# war_1 = Warrior('Пафнутий')
# war_2 = Warrior('Игорь')
#
# war_1 & war_2
