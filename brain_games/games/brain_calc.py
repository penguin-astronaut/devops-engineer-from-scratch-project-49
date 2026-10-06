from operator import add, mul, sub
from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 100

OPERATIONS = {
    '+': add,
    '-': sub,
    '*': mul,
}


def generate_round():
    first = randint(MIN_NUMBER, MAX_NUMBER)
    second = randint(MIN_NUMBER, MAX_NUMBER)
    symbol = choice(list(OPERATIONS))

    question = f'{first} {symbol} {second}'
    correct_answer = OPERATIONS[symbol](first, second)

    return question, str(correct_answer)
