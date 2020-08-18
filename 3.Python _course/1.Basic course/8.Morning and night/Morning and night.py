from microbit import *
sun = Image("90909:"
            "09990:"
            "99999:"
            "09990:"
            "90909")

moon = Image("00990:"
             "09900:"
             "09900:"
             "09900:"
             "00990")


while True:
    value = display.read_light_level()
    if value < 20:
        display.show(moon)
    else:
        display.show(sun)
    value = 0
