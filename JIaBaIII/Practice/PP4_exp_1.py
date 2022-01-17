import json

# def do_smth(arg1, arg2, arg3) -> int:
#     return arg1 + arg2 + arg3
#
#
# some_list = [22, 432, 55]
# print(do_smth(*some_list))
#
#
# def summ_args(arg1, arg2, arg3) -> int:
#     return arg1 + arg2 + arg3
#
#
# arguments = {
#     'arg1': 1,
#     'arg2': 2,
#     "arg3": 3
# }
#
# print(summ_args(**arguments))


# def do_smth():
#     print('WOW')
#
#
# def make_func_do_smth(func):
#     func()
#
#
# print(make_func_do_smth(do_smth))                                             #  wow

# def do_smth_else(arg1=5, arg2=3, arg3=5):
#     return arg1 - arg2 - arg3
#
#
# print(do_smth_else(1, 2, 3))                                                  # ??


# def count_list(list_arg):
#     i = 0
#     for iter in list_arg:
#         i += iter
#     return i
#
#
# print(count_list([2, 3]))


# def polucit_po_morde(arg_1, arg_2=100) -> int:
#     ruchka = 0
#     for elem in arg_1:
#         ruchka += elem
#     ruchka += arg_2
#     return ruchka
#
#
# print(polucit_po_morde([10, 40]))


# def create_issue(issue_source=None):
#     return Issue(issue_source)
#
#
# Issue = list
# print(create_issue('das'))


# def do_smth(*args, **kwargs):                                     # args - аргументы, привязанные к позициям,
#     print(args)                                                   # kwargs - именные аргументы без привязки к позиции
#     print(kwargs)
#
#
# do_smth(1234, 42, 'pew', arg1=2, arg2=4, arg3=666, lisa='твоой пёс')


# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)        # [1,2,3,4,5,6]

# print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))           # sorted может применяться и к дикту


# def do_smth333333():
#     print('WOW')
#
#
# def make_func_do_smth(func):
#     func()
#
#
# make_func_do_smth(do_smth333333)

# def do_smth():
#     print('WOW')
#
#
# def make_func_do_smth(func):
#     func()
#
#
# make_func_do_smth(do_smth)


# def makeChoice():
#     c = 0
#     if input() == 'yes':
#         c += 1
#         return int(c)
#
#
# def choiceMade(c):
#     if c == 1:
#         print('finally this damn thing works')
#
#
# choiceMade(makeChoice())


# def cool():
#     return "I'm coll, yea baaaaaaby"
#
#
# def make_cool():
#     while cool():
#         print(f"again and again {cool()}")
#
#
# make_cool()

# backend_response = {
#     'result': [
#         {
#             'post_number': 123352,
#             'post_date': '2019-12-11',
#             'package_items_ids': [
#                 1235,
#                 234,
#                 1234,
#                 432,
#                 15,
#                 11,
#                 2
#             ],
#             'city': 'Moscow',
#             'country': 'Russia',
#             'weight': 2100,
#             'flammable': False,
#             'status': 'arrived'
#         },
#         {
#             'post_number': 12345,
#             'post_date': '2019-12-11',
#             'package_items_ids': [
#                 1235,
#                 1111,
#                 1234,
#                 432,
#                 15,
#                 2
#             ],
#             'city': 'Moscow',
#             'country': 'Russia',
#             'weight': 2100,
#             'flammable': True,
#             'status': 'arrived'
#         },
#         {
#             'post_number': 43242,
#             'post_date': '2019-12-11',
#             'package_items_ids': [
#                 23,
#                 13,
#                 22,
#                 432,
#                 44,
#                 235,
#                 2
#             ],
#             'city': 'Moscow',
#             'country': 'Russia',
#             'weight': 2000,
#             'flammable': False,
#             'status': 'arrived'
#         },
#         {
#             'post_number': 11125,
#             'post_date': '2019-12-11',
#             'package_items_ids': [
#                 43,
#                 11111,
#                 2,
#                 11,
#                 555,
#                 44,
#                 10
#             ],
#             'city': 'Moscow',
#             'country': 'Russia',
#             'weight': 3100,
#             'flammable': True,
#             'status': 'arrived'
#         },
#         {
#             'post_number': 432423,
#             'post_date': '2019-12-11',
#             'package_items_ids': [
#                 324,
#                 532,
#                 3333,
#                 2345,
#                 22,
#                 115,
#                 2
#             ],
#             'city': 'Moscow',
#             'country': 'Russia',
#             'weight': 1150,
#             'flammable': True,
#             'status': 'arrived'
#         },
#         {
#             'post_number': 32532,
#             'post_date': '2019-12-11',
#             'package_items_ids': [
#                 5436,
#                 7645,
#                 456,
#                 5357,
#                 34,
#                 54,
#                 3
#             ],
#             'city': 'Moscow',
#             'country': 'Russia',
#             'weight': 2100,
#             'flammable': False,
#             'status': 'arrived'
#         },
#         {
#             'post_number': 2323,
#             'post_date': '2019-12-11',
#             'package_items_ids': [
#                 432,
#                 5435,
#                 6546,
#                 76,
#                 45,
#                 34,
#                 3
#             ],
#             'city': 'Moscow',
#             'country': 'Russia',
#             'weight': 1201,
#             'flammable': True,
#             'status': 'arrived'
#         },
#         {
#             'post_number': 1111,
#             'post_date': '2019-12-11',
#             'package_items_ids': [
#                 654,
#                 345,
#                 44,
#                 765,
#                 9,
#                 5,
#                 1
#             ],
#             'city': 'Moscow',
#             'country': 'Russia',
#             'weight': 1100,
#             'flammable': False,
#             'status': 'arrived'
#         },
#         {
#             'post_number': 576734,
#             'post_date': '2019-12-11',
#             'package_items_ids': [
#                 546,
#                 1111,
#                 645,
#                 754,
#                 22,
#                 765,
#                 54
#             ],
#             'city': 'Moscow',
#             'country': 'Russia',
#             'weight': 1234,
#             'flammable': True,
#             'status': 'arrived'
#         }
#     ]
# }
# some_json = {
#     'result': [
#         {
#             "id": 442500000904671234,
#             "reply": 0,
#             "children": [
#                 {
#                     "id": 442500532536893440,
#                     "reply": 1,
#                     "children": [
#                         {
#                             "id": 442500826561785856,
#                             "reply": 1,
#                             "children": [
#                                 {
#                                     "id": 442501277688545280,
#                                     "reply": 1,
#                                     "children": [
#                                         {
#                                             "id": 442501561940709376,
#                                             "reply": 1,
#                                             "children": [
#                                                 {
#                                                     "id": 442501884709199872,
#                                                     "reply": 1,
#                                                     "children": [
#
#                                                     ]
#                                                 }
#                                             ]
#                                         }
#                                     ]
#                                 }
#                             ]
#                         }
#                     ]
#                 },
#                 {
#                     "id": 442500099315597312,
#                     "reply": 0,
#                     "children": [
#
#                     ]
#                 }
#             ]
#         }
#     ]
# }
# dict_01 = {'test': {'test2': {'test': 123}}}
# dict_02 = {'a': 1, 'b': {'c': {}}}  # >>> depth(d) 3
# dict_03 = {'foo': {'bar': {'baz': 0}, 'spam': {'ham': {'monty': 1}, 'eric': 'idle'}}, 'john': 'cheese'}  # depth=5??
# response = {'test': {'test': {'test': {'test': {'test': {'test': 123}}}}}}


# count_global = 0
#
#
# def find_depth(tree_dict=None, count=0):
#
#     if not tree_dict['children']:
#         global count_global
#         if count_global < count:
#             count_global = count
#
#     for child in tree_dict['children']:
#         count += 1
#         find_depth(child, count)
#
#
# find_depth(*some_json['result'])
# print(count_global)


# def depth(d, level=1):
#     if not isinstance(d, dict) or not d:
#         return level
#     return max(depth(d[k], level + 1) for k in d)
#
#
# print(depth(dict_02))
# print(json.dumps(dict_02, indent=4))


# def depth(dicti):
#     if isinstance(dicti, dict):
#         return 1 + (max(map(depth, dicti.values())) if dicti else 0)
#     return 0
#
#
# print(depth(dict_02))
# print(json.dumps(dict_02, indent=4))


# def depth(d):
#     if isinstance(d, dict):
#         return 1 + (max(map(depth, d.values())) if d else 0)
#     return 0
#
#
# print(depth(backend_response))
# print(json.dumps(backend_response, indent=4))
