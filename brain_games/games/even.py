from random import randint


def roll():
    question = randint(1, 1000)
    answer = 'yes' if question % 2 == 0 else 'no'

    return question, answer


def print_instructions():
    print('Answer "yes" if the number is even, otherwise answer "no".')
