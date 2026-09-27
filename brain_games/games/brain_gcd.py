from math import gcd
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    first = randint(1, 100)
    second = randint(1, 100)
    return f'{first} {second}', str(gcd(first, second))
