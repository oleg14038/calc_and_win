"""A game where the player defeats an enemy in five turns."""

# Эта функция запрашивает у пользователя ввод и проверяет,
# хочет ли он сыграть ещё раз.
from module import is_wanting_to_play

# Строка с INTRO:
# Это переменная, содержащая строку с описанием игры и правилами,
# которая выводится игроку в начале.
INTRO = """РАССЧИТАЙ И ПОБЕДИ!
Загрузка...

Твоя цель — за 5 ходов набрать такое количество очков урона противнику,
которое попадет в диапазон +– 10 от значения здоровья противника.

Значение здоровья противника генерируется случайным образом
в диапазоне от 80 до 120 очков.

В твоём распоряжении три вида атак:
lite — урон от 2 до 5 очков;
mid — урон от 15 до 25 очков;
hard — урон от 30 до 40 очков.
ВПЕРЁД К ПОБЕДЕ!!!
"""
# Функция main():
# main — основная функция, запускающая игру.


def main() -> None:
    """Main function that runs the game."""
    print(INTRO)
    # переменной replay присваивается True,
    # чтобы активировать цикл while replay
    replay = True
    while replay:
        # replay = is_wanting_to_play() выполняется вызов функции
        # is_wanting_to_play, которая спрашивает у пользователя,
        # хочет ли он сыграть ещё раз.
        replay = is_wanting_to_play()


if __name__ == "__main__":
    main()
