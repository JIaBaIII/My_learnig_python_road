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


# def func_1(argument1, argument2):
#     return argument1 - argument2
#
#
# def func_2(drugoi_arg1, drugoi_arg2):
#     return drugoi_arg1 + drugoi_arg2
#
#
# print(func_1(func_1(10, 5), func_2(10, 5)))

class MyFirstClass:
    def __init__(self, f1, f2):
        self.f1 = f1
        self.f2 = f2
        print(f1, f2)

    def get_f1(self):
        return self.f1

    def get_f2(self):
        return self.f2

    def set_f1(self, new_f1):
        self.f1 = new_f1

    def set_f2(self, new_f2):
        self.f2 = new_f2


mfc = MyFirstClass
mfc(1, 2)

mfc.get_f1()
