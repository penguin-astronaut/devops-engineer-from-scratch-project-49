from random import randint

DESCRIPTION = 'What number is missing in the progression?'
MIN_NUMBER = 1
MAX_NUMBER = 100
PROGRESSION_LENGTH = 10
MIN_STEP = 1
MAX_STEP = 10


def generate_progression(start, step, length):
    return [start + index * step for index in range(length)]


def generate_round():
    start = randint(MIN_NUMBER, MAX_NUMBER)
    step = randint(MIN_STEP, MAX_STEP)
    progression = generate_progression(start, step, PROGRESSION_LENGTH)
    hidden_index = randint(0, PROGRESSION_LENGTH - 1)
    correct_answer = str(progression[hidden_index])
    question = [str(number) for number in progression]
    question[hidden_index] = '..'
    return ' '.join(question), correct_answer
