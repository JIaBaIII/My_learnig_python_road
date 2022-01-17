# from JIaBaIII.Collor_everything.Colloring import make_txt_bold, make_txt_light_blue, make_txt_italics,\
#     make_txt_underlined
from ftplib import FTP

# class MyFirstClass:
#     def __init__(self, f1, f2):
#         self.f1 = f1
#         self.f2 = f2
#
#     def get_f1(self):
#         return self.f1
#
#     def get_f2(self):
#         return self.f2
#
#     def set_f1(self, new_f1):
#         self.f1 = new_f1
#         return new_f1
#
#     def set_f2(self, new_f2):
#         self.f2 = new_f2
#         return new_f2
#
#
# instance_1 = MyFirstClass(4, 5)
# print(instance_1.get_f2())
# print(instance_1.set_f1(244122))
# instance_1.f1 = 9
# print(instance_1.f1)
# #
# print(instance_1.get_f2())
# instance_1.set_f2(14)
# print(instance_1.get_f2())
# instance_1.f2 = 'New line cinema'
# print(instance_1.f2)
# instance_1.f2 = -9
# print(instance_1.f2)
# instance_2 = instance_1.f1 + instance_1.f2
# print(f'{instance_2} - Как говорил один знаменитый классик: "Ну нихуя себе!"')

# class Skeleton:
#
# class Cock:
#     def __init__(self, claw, feathers, cockscomb):
#         self.sk = Skeleton()
#         self.claw = claw
#         self.feathers = feathers
#         self.cockscomb = cockscomb
#         self.wings = [self.sk.wings.add(feather) for feather in feathers]
#
#     def do_wings(self):
#         return self.wings.do_stuff()


# class StaticExampleClass:
#     static_field = 'I\'M STATIC!'
#
#     def __init__(self):
#         self.not_static_field = 'I\'M NOT STATIC!'
#
#     def method_example(self):
#         print(self.static_field)
#         print(self.not_static_field)
#
#
# example = StaticExampleClass()
# example.method_example()
# example_2 = StaticExampleClass()
# StaticExampleClass.static_field = 'NOW YOU SEE?'
# example.not_static_field = 'test1'
# example_2.not_static_field = 'test2'
# example.method_example()
# example_2.method_example()
#
# example_2.static_field = 'SEE???'
# example.method_example()
# example_2.method_example()
#
# StaticExampleClass.static_field = 'JUST MAY BE YOU BLIND'
# example.method_example()
# example_2.method_example()


# @make_txt_underlined
# @make_txt_italics
# @make_txt_bold
# @make_txt_light_blue
# def hello():
#     return "Красивый бирюзовый текст"
#
#
# print(hello())


# class FunctionalList:
#     """Класс-обёртка над списком с добавлением некоторой функциональной магии: head,
#     tail, init, last, drop, take."""
#
#     def __init__(self, values=None):
#         if values is None:
#             self.values = []
#         else:
#             self.values = values
#
#     def __len__(self):
#         return len(self.values)
#
#     def __getitem__(self, key):
#         # если значение или тип ключа некорректны, list выбросит исключение
#         return self.values[key]
#
#     def __setitem__(self, key, value):
#         self.values[key] = value
#
#     def __delitem__(self, key):
#         del self.values[key]
#
#     def __iter__(self):
#         return iter(self.values)
#
#     def __reversed__(self):
#         return FunctionalList(reversed(self.values))
#
#     def __call__(self, args):
#         self.append(args)
#
#     def append(self, value):
#         self.values.append(value)
#
#     def head(self):
#         # получить первый элемент
#         return self.values[0]
#
#     def tail(self):
#         # получить все элементы после первого
#         return self.values[1:]
#
#     def init(self):
#         # получить все элементы кроме последнего
#         return self.values[:-1]
#
#     def last(self):
#         # получить последний элемент
#         return self.values[-1]
#
#     def drop(self, n):
#         # все элементы кроме первых n
#         return self.values[n:]
#
#     def take(self, n):
#         # первые n элементов
#         return self.values[:n]
#
#
# some_key = [44, 11, 48, 'sigma']
# fu = FunctionalList(some_key)
# print(fu.head())
# print(fu.tail())
# print(fu.__getitem__(1))
# fu(44)
# print(fu.values)

# class Entity:
#     """Класс, описывающий объект на плоскости. "Вызываемый", чтобы обновить позицию объекта."""
#
#     def __init__(self, size, x=None, y=None):
#         self.x, self.y = x, y
#         self.size = size
#         print(self.size, x, y)
#
#     def __call__(self, x, y):                  # аналогично __set__(self, x, y) Только call не надо звать отдельно
#         """Изменить положение объекта."""
#         self.x, self.y = x, y
#         return self.size, self.x, self.y
#
#     # чик...
#
#
# eni = Entity(500, 0, 0.3)
# print(eni(11, 9))
# print(eni('Кружечка', 'на столе'))


# class Closer:
#     """Менеджер контекста для автоматического закрытия объекта вызовом метода close
#     в with-выражении."""
#
#     def __init__(self, obj):
#         self.obj = obj
#
#     def __enter__(self):
#         return self.obj  # привязка к активному объекту with-блока
#
#     def __exit__(self, exception_type, exception_val, trace):
#         try:
#             self.obj.close()
#
#         except AttributeError:  # у объекта нет метода close
#             print('Not closable.')
#             return True  # исключение перехвачено
#
#
# with Closer(FTP('ftp.somesite.com')) as conn:
#     conn.__dir__()
#
# # вывод опущен для краткости
# print(conn.dir())
#
# длинное сообщение AttributeError, невозможно использовать закрытое соединение
# with Closer(int(5)) as i:
#     while i < 10:
#         i += 1
#         print(i)

