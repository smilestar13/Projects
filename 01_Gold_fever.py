import random

while True:

    def get_game(rows_count):
        game = []  # Создаем список для игры
        for i in range(rows_count):  # Добавляем рядов столько, сколько user указал в rows_count
            row = []
            for j in range(i + 1):  # Добавляем значений == номер ряда (в 3-й ряд 3 значения)
                row.append(random.randint(1, 99))  # Добавить рандомное значение, можно менять под "уровень сложности"
            game.append(row)  # Добавить ряд в список с игрой
        return game


    def print_game(game):  # Вывод игры в формате полу-пирамидки на экран
        for row in game:
            print(row)


    def get_max_gold(game):
        rows_count = len(game)
        max_gold = game[0][0]  # Переменная для суммы золота
        i = 0  # Индексы для рядов (i - 1 => вниз; i + 1 => вверх)
        j = 0  # Индексы для значений (j - 1 => влево; j + 1 => вправо)
        while i < rows_count - 1:  # Идем по всем до предпоследнего ряда
            i += 1  # Вниз идем в любом случае
            gold_down = game[i][j]  # Берем значение, если идти вниз
            gold_down_right = game[i][j + 1]  # Берем значение, если идти вниз и вправо
            if gold_down > gold_down_right:  # Если вниз больше, чем вниз и вправо - идем вниз
                max_gold += gold_down
            else:  # Если нет - наоборот
                max_gold += gold_down_right
                j += 1  # Тут идем вправо
        return max_gold


    game = get_game(int(input('\nМайнер, сколько рядов ты готов осилить в этот раз? ')))  # Можно менять кол-во рядов
    print('\n•ᴗ•')
    print_game(game)
    user_gold = int(input('\nСколько золота у тебя вышло собрать? '))

    if user_gold < get_max_gold(game):
        print(f'\nЯ собрал {get_max_gold(game)} и победил! Попробуй еще...')
    elif user_gold == get_max_gold(game):
        print(f'\nОтработали на равных, у меня тоже {get_max_gold(game)}!')
    else:
        print(f'\nОго... У меня всего {get_max_gold(game)}, ты победил!')

    user_repeat = input('\nХочешь сыграть еще раз? (Да/ Нет): ')
    user_repeat = user_repeat.lower()

    if user_repeat == 'да':
        continue
    else:
        print('\nИгра окончена!')
        break
