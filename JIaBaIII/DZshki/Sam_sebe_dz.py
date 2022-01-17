# import json  # подключили библиотеку для работы с json
#
#
# def find_response_confidence(our_file_name):
#     list_of_data = []
#     count_of_data = 0
#     filename = f'D:/Download/{our_file_name}.json'  # Директория нужного нам файла
#     with open(filename) as file:  # открыли файл с данными
#         data_dict = json.load(file)  # загнали все, что получилось в переменную
#         # pprint(data_dict)  # Красивый вовод нашего json'a в перменной data_dict
#     for i in range(len(data_dict['items'])):  # создали цикл, который будет работать построчно
#         value = data_dict['items'][i]['match']['confidence']
#         value_1 = int(value * 10000000) / 10000000
#         list_of_data.append(value_1)  # Добавляем value ключа конфиденс в лист
#         # print(f'\"confidence\" {count_of_data} : {list_of_data[count_of_data]}')  # Вывести значение confidence
#         count_of_data += 1
#     print(f'Всего \"confidence\" в ответе = {count_of_data}')
#     print('-' * 60)
#     return list_of_data
#
#
# def find_ideal_confidence(ideal_file_name):
#     list_of_data_2 = []
#     count_of_data_2 = 0
#     filename_2 = f'D:/Download/{ideal_file_name}.json'
#     with open(filename_2) as file_2:  # открыли файл с данными
#         data_dict_1 = json.load(file_2)  # загнали все, что получилось в переменную
#         # pprint(data_dict)  # Красивый вовод нашего json'a в перменной data_dict
#     for txt in data_dict_1['items']:  # создали цикл, который будет работать построчно
#         value = txt['match']['confidence']
#         value_2 = int(value * 10000000) / 10000000
#         list_of_data_2.append(value_2)  # Добавляем value ключа конфиденс в лист
#         # Вывести ниже значение confidence
#         # print(f'Идеальый \"confidence\" {count_of_data_2} : {list_of_data_2[count_of_data_2]} ||| ')
#         count_of_data_2 += 1
#     print('-' * 60)
#     print(f'Всего \"confidence\" в идеале = {count_of_data_2}')
#     return list_of_data_2
#
#
# def compare_confidences(ideal, response):
#     ideal_list = find_ideal_confidence(ideal)
#     response_list = find_response_confidence(response)
#     for i in range(len(ideal_list)):
#         if ideal_list[i] == response_list[i]:
#             print(f'\033[35mOk\033[0m идеал [{ideal_list[i]}] и ответ [{response_list[i]}]')
#         else:
#             print(f'\033[31m!!Расхождение!!\033[0m Идеал [{ideal_list[i]}] и ответ [{response_list[i]}]')
#
#
# # Сюда в качестве аргумента подставляешь имя идеального файла и ответа
# compare_confidences('lt-pcretest', 'lt-pcretest')

