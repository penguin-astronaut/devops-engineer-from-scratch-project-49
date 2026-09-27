from operator import add, mul, sub
from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'

OPERATIONS = {
    '+': add,
    '-': sub,
    '*': mul,
}


def generate_round():
    first = randint(1, 100)
    second = randint(1, 100)
    symbol = choice(list(OPERATIONS))

    question = f'{first} {symbol} {second}'
    correct_answer = OPERATIONS[symbol](first, second)

    return question, str(correct_answer)