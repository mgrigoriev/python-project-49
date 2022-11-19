from random import randint
from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


def roll():
    x = randint(1, 100)

    question = x
    answer = 'yes' if is_prime(x) else 'no'

    return question, answer


def print_instructions():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
