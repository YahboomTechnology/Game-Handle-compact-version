from microbit import *
import superbit
import radio
import neopixel

radio.on()
radio.config(group=1)
display.show(Image.HAPPY)
np = neopixel.NeoPixel(pin12, 4)
flag = 0
a = 0

while True:
    incoming = radio.receive()
    if incoming == 'up':
        superbit.motor_control_dual(superbit.M1, superbit.M3, -255, 255, 0)
        superbit.motor_control_dual(superbit.M2, superbit.M4, -255, 255, 0)
    if incoming == 'down':
        superbit.motor_control_dual(superbit.M1, superbit.M3, 255, -255, 0)
        superbit.motor_control_dual(superbit.M2, superbit.M4, 255, -255, 0)
    if incoming == 'left':
        superbit.motor_control_dual(superbit.M1, superbit.M3, 255, 255, 0)
        superbit.motor_control_dual(superbit.M2, superbit.M4, -255, -255, 0)
    if incoming == 'right':
        superbit.motor_control_dual(superbit.M1, superbit.M3, -255, -255, 0)
        superbit.motor_control_dual(superbit.M2, superbit.M4, 255, 255, 0)
    if incoming == 'left_rear':
        superbit.motor_control_dual(superbit.M1, superbit.M3, 255, 0, 0)
        superbit.motor_control_dual(superbit.M2, superbit.M4, 0, -255, 0)
    if incoming == 'right_after':
        superbit.motor_control_dual(superbit.M1, superbit.M3, 0, -255, 0)
        superbit.motor_control_dual(superbit.M2, superbit.M4, 255, 0, 0)
    if incoming == 'left_front':
        superbit.motor_control_dual(superbit.M1, superbit.M3, 0, 255, 0)
        superbit.motor_control_dual(superbit.M2, superbit.M4, -255, 0, 0)
    if incoming == 'right_front':
        superbit.motor_control_dual(superbit.M1, superbit.M3, 0, 255, 0)
        superbit.motor_control_dual(superbit.M2, superbit.M4, -255, 0, 0)
    if incoming == 'turn_off':
        superbit.motor_control_dual(superbit.M1, superbit.M3, 0, 0, 0)
        superbit.motor_control_dual(superbit.M2, superbit.M4, 0, 0, 0)
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