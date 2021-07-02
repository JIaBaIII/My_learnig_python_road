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
#
#     def set_f2(self, new_f2):
#         self.f2 = new_f2
#
#
# instance_1 = MyFirstClass(4, 5)
# print(instance_1.get_f1())
# print(instance_1.set_f1(2))
# print(instance_1.get_f1())
# instance_1.f1 = 9
# print(instance_1.f1)
#
# print(instance_1.get_f2())
# instance_1.set_f2(14)
# print(instance_1.get_f2())
# instance_1.f2 = 'New line sinema'
# instance_1.f2 = -9
# print(instance_1.f2)
# print(f'{instance_1.f1 + instance_1.f2} - Как говорил один знаменитый классик: "Ну нихуя себе!"')


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


class StaticExampleClass:
    static_field = 'I\'M STATIC!'

    def __init__(self):
        self.not_static_field = 'I\'M NOT STATIC!'

    def method_example(self):
        print(self.static_field)
        print(self.not_static_field)


example = StaticExampleClass()
example.method_example()
example_2 = StaticExampleClass()
StaticExampleClass.static_field = 'NOW YOU SEE?'
example.not_static_field = 'test1'
example_2.not_static_field = 'test2'
example.method_example()
example_2.method_example()

example_2.static_field = 'SEE???'
example.method_example()
example_2.method_example()

StaticExampleClass.static_field = 'JUST MAY BE YOU BLIND'
example.method_example()
example_2.method_example()


