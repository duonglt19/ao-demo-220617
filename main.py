import math
import os


def add(a, b):
    return math.floor(a + b)


def to_sentence(s):
    s = s.capitalize()

    if s.endswith('.'):
        return s
    else:
        return s + '.'
