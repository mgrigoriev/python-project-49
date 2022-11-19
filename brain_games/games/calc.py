from random import randint, choice


def roll():
    operation = choice(['+', '-', '*'])
    x = randint(1, 100)
    y = randint(1, 100)

    question = f'{x} {operation} {y}'
    answer = str(eval(question))

    return question, answer


def print_instructions():
    print('What is the result of the expression?')
