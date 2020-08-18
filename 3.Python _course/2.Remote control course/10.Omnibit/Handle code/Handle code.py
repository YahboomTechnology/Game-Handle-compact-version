from microbit import *
import ghandle
import radio

display.show(0)
radio.on()
radio.config(group=1)

while True:
    x = pin2.read_analog() * -1 + 512
    y = pin1.read_analog() * -1 + 512
    if ghandle.rocker(ghandle.up):
        radio.send('up')
        display.show(Image.ARROW_N)
    elif ghandle.rocker(ghandle.down):
        radio.send('down')
        display.show(Image.ARROW_S)
    elif ghandle.rocker(ghandle.left):
        radio.send('left')
        display.show(Image.ARROW_W)
    elif ghandle.rocker(ghandle.right):
        radio.send('right')
        display.show(Image.ARROW_E)
    elif ghandle.rocker(ghandle.pressed):
        radio.send('turn_off')
        display.show(Image.NO)
    elif x < -100 and y < -100:
        radio.send('left_rear')
    elif x > 100 and y < -100:
        radio.send('right_after')
    elif x < -100 and y > 100:
        radio.send('left_front')
    elif x > 100 and y > 100:
        radio.send('right_front')
    else:
        radio.send('stop')
        display.clear()
    if ghandle.B1_is_pressed():
        radio.send('R')
        display.show("R")
    if ghandle.B2_is_pressed():
        radio.send('G')
        display.show("G")
    if ghandle.B3_is_pressed():
        radio.send('B')
        display.show("B")
    if ghandle.B4_is_pressed():
        radio.send('Y')
        display.show("Y")
