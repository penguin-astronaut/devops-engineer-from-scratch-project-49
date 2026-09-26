from random import randint

import prompt

from brain_games.cli import welcome_user


def main():
    MAX_ITERATIONS = 3
    
    print('Welcome to the Brain Games!')
    
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    print('Answer "yes" if the number is even, otherwise answer "no".')
    current_iteration = 1


    while current_iteration <= MAX_ITERATIONS:
        number = randint(1, 100)
        print(f'Question: {number}')

        answer = prompt.string('Your answer: ')

        is_even = number % 2 == 0

        if is_even and answer != 'yes' or not is_even and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{'yes' if answer == 'no' else 'no'}'.\nLet's try again, {name}!")
            break

        current_iteration += 1
        print('Correct!')

    if current_iteration - 1 == MAX_ITERATIONS:
        print(f'Congratulations, {name}!')


if  __name__ == "__main__":
    main()
