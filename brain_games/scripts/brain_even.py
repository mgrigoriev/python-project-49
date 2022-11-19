import prompt
from random import randint


def attempt(name):
    number = randint(1, 1000)
    correct_answer = 'yes' if number % 2 == 0 else 'no'

    print(f'Question: {number}')
    user_answer = prompt.string('Your answer: ')

    if user_answer == correct_answer:
        print('Correct!')
        return True

    print(f"'{user_answer}' is wrong answer ;(. Correct answer was 'no'.")
    print(f"Let's try again, {name}!")
    return False


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    successful_attempts = 0
    while successful_attempts < 3:
        result = attempt(name)
        if result:
            successful_attempts += 1
        else:
            successful_attempts = 0

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
