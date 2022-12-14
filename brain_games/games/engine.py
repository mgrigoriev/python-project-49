import prompt


def attempt(name, question, correct_answer):
    print(f'Question: {question}')
    user_answer = prompt.string('Your answer: ')

    if user_answer in ['exit', 'quit', 'q']:
        exit()

    if user_answer == correct_answer:
        print('Correct!')
        return True

    print(f"'{user_answer}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'.\n"
          f"Let's try again, {name}!"
          )

    return False


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    game.print_instructions()

    successful_attempts = 0
    while successful_attempts < 3:
        question, correct_answer = game.roll()
        result = attempt(name, question, correct_answer)
        if result:
            successful_attempts += 1
        else:
            exit()

    print(f'Congratulations, {name}!')
