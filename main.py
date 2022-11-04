import random
import sys


num = 0


def generateRandomNumber():
    return random.randint((-1 * sys.maxsize), sys.maxsize)


def differenceFromAnswer(guess, answer = generateRandomNumber()):
    print(answer)
    try:  
        if int(guess) < answer:
            return 'Too low'
        elif int(guess) > answer:
            return 'Too high'
        else:
            return 'Correct'
    except:
      return 'Invalid'