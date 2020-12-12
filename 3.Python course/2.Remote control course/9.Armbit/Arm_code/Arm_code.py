from microbit import *
import superbit
import radio
import neopixel

radio.on()
radio.config(group=1)


display.show(Image.HEART)

np = neopixel.NeoPixel(pin12, 4)

while True:
    incoming = radio.receive()
    if incoming == 'up':
        superbit.motor_control(superbit.M2, 255, 0)

    elif incoming == 'down':
        superbit.motor_control(superbit.M2, -255, 0)

    elif incoming == 'left':
        superbit.motor_control(superbit.M4, 180, 0)

    elif incoming == 'right':
        superbit.motor_control(superbit.M4, -180, 0)

    elif incoming == 'stop':
        superbit.motor_control(superbit.M1, 0, 0)
        superbit.motor_control(superbit.M2, 0, 0)
        superbit.motor_control(superbit.M3, 0, 0)
        superbit.motor_control(superbit.M4, 0, 0)

    if incoming == 'R':
        superbit.motor_control(superbit.M1, 255, 0)

    elif incoming == 'G':
        superbit.motor_control(superbit.M3, -255, 0)

    elif incoming == 'B':
        superbit.motor_control(superbit.M3, 255, 0)

    elif incoming == 'Y':
        superbit.motor_control(superbit.M1, -255, 0)

