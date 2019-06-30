# A simple guess the number processing method


def processguess(a, b):
    if a > b:
        print("You're too high!")
    if a < b:
        print("You're too low!")
    if a == b:
        print("You got it!!")
        return 0
    return 1

