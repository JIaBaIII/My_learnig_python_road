#                                                    Что делает Кирилл?
import random
import time


def find_kirill():
    name = 'Кирилл'
    activity = ['ест сладкие груши',
                'веселится с Настюшей',
                'истерично хохочет',
                'пипиську он дрочит',
                'флиртует с цветами',
                'шелестит волосами',
                'танцует хард-баc',
                'он в каждом из нас=)']
    colors_of = ["\033[1m\033[3m\033[31m",
                 "\033[1m\033[3m\033[32m",
                 "\033[1m\033[3m\033[33m",
                 "\033[1m\033[3m\033[34m",
                 "\033[1m\033[3m\033[35m",
                 "\033[1m\033[3m\033[36m"]
    while True:
        r_activity = random.randint(0, len(activity) - 1)
        ra_coloring = random.randint(0, len(colors_of) - 1)
        my_sting = f'           {name} - {activity[r_activity]}'
        for i in range(40):
            time.sleep(0.23)
            print(colors_of[ra_coloring] + "\r{}".format(my_sting[i:i + 10]), end='')


find_kirill()
