from pprint import pprint
import json


def ideal_response(ideal_file):
    file_name = ideal_file
    with open(file_name) as file:
        ideal_list = json.load(file)
        # print('Идеальный response')
        # pprint(ideal_list)
    return ideal_list


def our_response(our_file):
    file_name = our_file
    with open(file_name) as file:
        our_response_list = json.load(file)
        for i in range(len(our_response_list)):
            our_response_list[i][2] = round(our_response_list[i][2], 4)
        # print('Response')
        # pprint(our_response_list)
    return our_response_list


def compare_responses(ideal_file_path, our_response_file_path):
    ideal_list = ideal_response(ideal_file_path)
    our_response_list = our_response(our_response_file_path)
    if len(ideal_list) == len(our_response_list):
        for i in range(len(ideal_list)):
            if ideal_list[i] == our_response_list[i]:
                print(f'\033[32m{ideal_list[i]} == {our_response_list[i]}\033[0m')
            else:
                my_ideal_list = ideal_list[i]
                my_response_list = our_response_list[i]
                if my_ideal_list[0] != my_response_list[0]:
                    print(f'[\033[34m{my_ideal_list[0]}\033[0m, {my_ideal_list[1]}, {my_ideal_list[2]}] '
                          f'\033[31mне равен\033[0m '
                          f'[\033[34m{my_response_list[0]}\033[0m, {my_response_list[1]}, {my_response_list[2]}]')
                elif my_ideal_list[1] != my_response_list[1]:
                    print(f'[{my_ideal_list[0]}, \033[34m{my_ideal_list[1]}\033[0m, {my_ideal_list[2]}] '
                          f'\033[31mРасхождение\033[0m '
                          f'[{my_response_list[0]}, \033[34m{my_response_list[1]}\033[0m, {my_response_list[2]}]')
                elif my_ideal_list[2] != my_response_list[2]:
                    print(f'[{my_ideal_list[0]}, {my_ideal_list[1]}, \033[34m{my_ideal_list[2]}\033[0m] '
                          f'\033[31mРасхождение\033[0m '
                          f'[{my_response_list[0]}, {my_response_list[1]}, \033[34m{my_response_list[2]}\033[0m]')


compare_responses('D:/Download/dhcp_release.json', 'D:/Download/dhcp_release_17_08.json')


