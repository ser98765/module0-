# код по оценке средего количества попыток

import numpy as np
import math

def game_core_v1(number):
    count = 50    # число, с которого начинается угадывание
    count2 = 1
    count3 = 1    # счетчик попыток

    while True:  # бесконечный цикл
        if number == count:
            break
        elif number < count:
            count2 = count2 * 2
            count = count - math.ceil(50/count2)
            count3 = count3 + 1
        else:
            count2 = count2 * 2
            count = count + math.ceil(50/count2)
            count3 = count3 + 1
    return count3

def score_game(game_core):
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)

score_game(game_core_v1)