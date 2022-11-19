from random import randint


def roll():
    start = randint(1, 100)
    step = randint(1, 5)
    length = randint(5, 10)
    hidden_index = randint(0, length - 1)

    progression = []
    for i in range(0, length):
        if i == 0:
            current_number = start
        else:
            current_number = progression[i - 1] + step

        progression.append(current_number)

    hidden_number = progression[hidden_index]
    progression[hidden_index] = '..'

    question = ' '.join(map(str, progression))
    answer = str(hidden_number)

    return question, answer


def print_instructions():
    print('What number is missing in the progression?')
