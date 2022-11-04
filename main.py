import random
import sys


num = 0


def generateRandomNumber():
    return random.randint((-1 * sys.maxsize), sys.maxsize)


def differenceFromAnswer(guess, answer):
    pass