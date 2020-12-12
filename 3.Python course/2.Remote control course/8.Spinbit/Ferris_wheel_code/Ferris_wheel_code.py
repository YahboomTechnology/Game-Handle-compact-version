from microbit import *

import superbit
import radio

display.show(Image.HEART)
radio.on()
radio.config(group=1)
a = 0
flag = 0

while True:

    incoming = radio.receive()
    if incoming == 'B' and flag == 0:
        a = a - 50
        if a < 0:
            a = 0
        display.show(a)
        incoming = radio.receive()
        if incoming == 'B':
            flag = 1

    elif incoming == 'G' and flag == 0:
        a = a + 50
        if a > 250:
            a = 250
        display.show(a)
        incoming = radio.receive()
        if incoming == 'G':
            flag = 1

    elif incoming == 'R':
        superbit.motor_control(superbit.M1, a, 0)

    elif incoming == 'Y':
        superbit.motor_control(superbit.M1, -a, 0)

    elif incoming == 'T':
        flag = 0