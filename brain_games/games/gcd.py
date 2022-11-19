from random import randint
from math import gcd


def roll():
    x = randint(1, 100)
    y = randint(1, 100)

    question = f'{x} {y}'
    answer = str(gcd(x, y))

    return question, answer


def print_instructions():
    print('Find the greatest common divisor of given numbers.')
