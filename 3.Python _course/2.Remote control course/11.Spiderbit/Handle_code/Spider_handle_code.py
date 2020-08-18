# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor

from microbit import *
import ghandle
import microbit
import radio

display.show(Image("09090:09090:00900:09090:09090"))
microbit.sleep(1000)
radio.on()
radio.config(group=1)

while True:

    if ghandle.rocker(ghandle.up):
        radio.send("up")
        display.show(Image.ARROW_N)
    elif ghandle.rocker(ghandle.down):
        radio.send("down")
        display.show(Image.ARROW_S)
    elif ghandle.rocker(ghandle.left):
        radio.send("left")
        display.show(Image.ARROW_W)
    elif ghandle.rocker(ghandle.right):
        radio.send("right")
        display.show(Image.ARROW_E)
    elif ghandle.rocker(ghandle.pressed):
        radio.send("turn_off")
        display.show(Image.NO)
    elif ghandle.B1_is_pressed():
        radio.send("R")
        display.show("R")
    elif ghandle.B2_is_pressed():
        radio.send("G")
        display.show("G")
    elif ghandle.B3_is_pressed():
        radio.send("B")
        display.show("B")
    elif ghandle.B4_is_pressed():
        radio.send("Y")
        display.show("Y")
    else:
        radio.send("T")
        display.show(Image("09090:09090:00900:09090:09090"))
