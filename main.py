# добавить мультизыяность
import random


words = ['олово', 'волна', 'шапка', 'короб', 'дверь', 'книга',
         'взлет', 'штора', 'капот', 'сплав', 'эпоха', 'титан', 'аркан']
answer = random.choice(words)

COUNT_ROUND = 5


def start_print():
    text = (
        'Для начала игры нажми Enter\n'
        'Для настроек нажми s и Enter\n'
        'Для выхода напиши exit и нажми Enter'
    )
    print(text, end='')


def color_print(s: str, color: str = None):
    if color == 'yellow':
        print(f'\033[93m{s}\033[0m', end='')
    elif color == 'red':
        print(f'\033[91m{s}\033[0m', end='')
    elif color == 'green':
        print(f'\033[32m{s}\033[0m', end='')
    else:
        print(s, end='')


def space_print():
    print(' ', end='')


def print_word(word: list, answer: list) -> bool:
    flag = True
    d_answer = {}
    for item in answer:
        if item not in d_answer:
            d_answer[item] = 0
        d_answer[item] += 1
    res_color = [None for i in range(len(answer))]
    i = 0
    for item1, item2 in zip(word, answer):
        if item1 == item2:
            d_answer[item2] -= 1
            res_color[i] = 'green'
        else:
            flag = False
        i += 1
    i = 0
    for item1, item2 in zip(word, answer):
        if item1 != item2:
            if item1 in d_answer and d_answer[item1] > 0:
                res_color[i] = 'yellow'
                d_answer[item1] -= 1
            else:
                res_color[i] = 'red'
        i += 1
    for i, item in enumerate(word):
        color = res_color[i]
        color_print(item, color)
    return flag


def word_str_to_lst(word: str):
    return list(word)

while True:
    answer = word_str_to_lst(word=answer)
    start_print()
    inp = input('\n>>> ')
    count_round = 0
    if inp == '':
        print('Старт игры')
        while True:
            word = input('>>>>> ')
            if len(word) != 5:
                print('\nОшибка ввода. Введи слово из 5 букв.', end='')
                continue
            count_round += 1
            word = word_str_to_lst(word=word)
            if print_word(word=word, answer=answer):
                print(f'\nТы выиграл за {count_round} ходов!\n')
                break
            if count_round >= COUNT_ROUND:
                print(f'\nТы проиграл!!! Ты не выиграл за {COUNT_ROUND} ходов!\n')
                break
            print()

    elif inp == 's':
        text = (
            '\nНастройки.\n'
            'Тут можно будет выбрать длину слов, цвета букв и т.д.\n'
            'Введи c для настройки цветов.\n'
            'Введи l для настройки длины слов.\n'
            'Введи q для выхода в меню'
        )
        print(text)
        while True:
            s = input('>>>>> ')
            if s == 'c':
                print('\nНастройки цвета')
            elif s == 'l':
                print('\nНастройки длины слов')
            elif s == 'q':
                break
    elif inp == 'exit':
        break
