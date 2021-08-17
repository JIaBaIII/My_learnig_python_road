import json  # подключили библиотеку для работы с json
from pprint import pprint  # подключили Pprint для красоты выдачи текста

list_of_data = []
count_of_data = 0
filename = 'D:\\Download\\6e99ffd70239_17_08.json'  # Директория нужного нам файла
with open(filename) as file:  # открыли файл с данными
    data_dict = json.load(file)  # загнали все, что получилось в переменную
    # pprint(data_dict)  # Красивый вовод нашего json'a в перменной data_dict
for txt in data_dict['items']:  # создали цикл, который будет работать построчно
    value = txt['match']['confidence']
    value_1 = int(value * 100000000) / 100000000
    list_of_data.append(value_1)  # Добавляем value ключа конфиденс в лист
    # print(f'\"confidence\" {count_of_data} : {list_of_data[count_of_data]}')  # Вывести значение confidence
    count_of_data += 1
print(f'Всего \"confidence\" = {count_of_data}')


print('-' * 60)
print('-' * 60)
print('-' * 60)


list_of_data_2 = []
count_of_data_2 = 0
filename_2 = 'D:\\Download\\6e99ffd70239.json'
with open(filename_2) as file_2:  # открыли файл с данными
    data_dict_1 = json.load(file_2)  # загнали все, что получилось в переменную
    # pprint(data_dict)  # Красивый вовод нашего json'a в перменной data_dict
for txt in data_dict_1['items']:  # создали цикл, который будет работать построчно
    value_21 = txt['match']['confidence']
    value_2 = int(value_21 * 100000000) / 100000000
    list_of_data_2.append(value_2)  # Добавляем value ключа конфиденс в лист
    # print(f'Идеальый \"confidence\" {count_of_data_2} : {list_of_data_2[count_of_data_2]} ||| ')  # Вывести значение confidence
    count_of_data_2 += 1
print(f'Всего идеальных \"confidence\" = {count_of_data_2}')

for i in range(count_of_data):
    if list_of_data[i] == list_of_data_2[i]:
        print(f'Ok идеал [{list_of_data_2[i]}] и ответ [{list_of_data[i]}]')
    else:
        print(f'Расхождение между идеалом [{list_of_data_2[i]}] и ответом [{list_of_data[i]}]')
