from microbit import *
import random

one = Image("00000:"
            "00000:"
            "00900:"
            "00000:"
            "00000")

two = Image("00000:"
            "00090:"
            "00000:"
            "09000:"
            "00000")

three = Image("00000:"
              "09000:"
              "00900:"
              "00090:"
              "00000")

four = Image("00000:"
             "09090:"
             "00000:"
             "09090:"
             "00000")

five = Image("00000:"
             "09090:"
             "00900:"
             "09090:"
             "00000")

six = Image("00000:"
            "09990:"
            "00000:"
            "09990:"
            "00000")

while True:
    x, y, z = accelerometer.get_values()
    if x+y+z > 900:
        stochastic = random.randint(0, 5)
        if stochastic == 0:
            display.show(one)
        elif stochastic == 1:
            display.show(two)
        elif stochastic == 2:
            display.show(three)
        elif stochastic == 3:
            display.show(four)
        elif stochastic == 4:
            display.show(five)
        elif stochastic == 5:
            display.show(six)
