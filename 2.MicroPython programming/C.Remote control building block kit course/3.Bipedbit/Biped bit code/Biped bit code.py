from microbit import *
import superbit
import radio
import neopixel
import music

radio.on()
radio.config(group=1)
display.show(Image.HAPPY)
np = neopixel.NeoPixel(pin12, 4)
flag = 0
a = 0


while True:
    incoming = radio.receive()

    if incoming == 'up' and flag == 1 and a == 0:
        superbit.motor_control(superbit.M1, -255, 0)

    if incoming == 'down' and flag == 1 and a == 0:
        superbit.motor_control(superbit.M1, 255, 0)

    if incoming == 'up' and flag == 0 and a == 0:
        superbit.motor_control(superbit.M1, -255, 0)

    if incoming == 'down' and flag == 0 and a == 0:
        superbit.motor_control(superbit.M1, 255, 0)

    if incoming == 'turn_off' and a == 0:
        superbit.motor_control(superbit.M1, 0, 0)
        music.play("C4:4")
        np.clear()
        if flag == 1:
            flag = 0
        else:
            flag += 1
    if incoming == 'down':
        a = 1
    if incoming == 'up':
        a = 1
    if incoming == 'turn_off':
        a = 1
    if incoming == 'T' and flag == 0:
        superbit.motor_control(superbit.M1, 0, 0)
        a = 0
    elif incoming == 'T':
        a = 0
    display.show(flag)

    if incoming == 'R':
        np.clear()
        np[0] = (255, 0, 0)
        np[1] = (255, 0, 0)
        np[2] = (255, 0, 0)
        np[3] = (255, 0, 0)
        np.show()

    elif incoming == 'G':
        np[0] = (0, 255, 0)
        np[1] = (0, 255, 0)
        np[2] = (0, 255, 0)
        np[3] = (0, 255, 0)
        np.show()

    elif incoming == 'B':
        np[0] = (0, 0, 255)
        np[1] = (0, 0, 255)
        np[2] = (0, 0, 255)
        np[3] = (0, 0, 255)
        np.show()

    elif incoming == 'Y':
        np.clear()
        np[0] = (255, 255, 0)
        np[1] = (255, 255, 0)
        np[2] = (255, 255, 0)
        np[3] = (255, 255, 0)
        np.show()