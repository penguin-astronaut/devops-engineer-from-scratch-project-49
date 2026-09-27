from random import randint

DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def generate_progression(start, step, length):
    return [start + index * step for index in range(length)]


def generate_round():
    start = randint(1, 100)
    step = randint(1, 10)
    progression = generate_progression(start, step, PROGRESSION_LENGTH)
    hidden_index = randint(0, PROGRESSION_LENGTH - 1)
    correct_answer = str(progression[hidden_index])
    question = [str(number) for number in progression]
    question[hidden_index] = '..'
    return ' '.join(question), correct_answer
