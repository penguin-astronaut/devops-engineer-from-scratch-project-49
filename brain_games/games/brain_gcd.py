from math import gcd
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_round():
    first = randint(MIN_NUMBER, MAX_NUMBER)
    second = randint(MIN_NUMBER, MAX_NUMBER)
    return f'{first} {second}', str(gcd(first, second))
