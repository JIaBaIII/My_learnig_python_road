#                                            генератор бредовых фраз
import random


def crazy_frenzy():
    container_for_all = [['Мотыга', 'Балон', 'Карамзит', 'Циркуль', 'Фейхоа', 'Пися', 'Заяц', 'Киркоров', 'Ладья',
                          'Кресло', 'Петух', 'Транзистор', 'Бомжара', 'Кирилл', 'Денис', 'Артур', 'Пельмешка', 'Хлеб',
                          'Шляпка', 'Шалун', 'Шалаш', 'Сатана', 'Контент', 'Казахстан'],
                         ['глубоко', 'красиво', 'безнадежно', 'самозабвенно', 'истерически', 'злобно', 'мудро',
                          'фантезийно', 'скромно', 'к всеобщему шоку', 'игриво', 'флиртуя', 'шокирующе', 'агрессивно',
                          'мечтательно', 'с подозрением', 'с призрением', 'шаловливо', 'сгорая от нетерпения',
                          'ухмыляясь', 'соблазнительно', 'усердно'],
                         ['бежит', 'дышит', 'дрочит', 'молчит', 'убегает', 'летит', 'разговаривает', 'хохочет',
                          'издеввается', 'звонит', 'подвывает', 'плывет', 'отстреливается', 'матерится',
                          'покупает в магазине молоко', 'кушает', 'жарит', 'жанглирует', 'жужжит как не в себя',
                          'стонет', 'прыгает', 'манипулирует сеткой новостей', 'фонтанирует собой']
                         ]

    random_noun_index = random.randint(0, len(container_for_all[0]) - 1)
    random_adj_index = random.randint(0, len(container_for_all[1]) - 1)
    random_verb_index = random.randint(0, len(container_for_all[2]) - 1)

    print(container_for_all[0][random_noun_index] + " " + container_for_all[1][random_adj_index]
          + " " + container_for_all[2][random_verb_index])


crazy_frenzy()
