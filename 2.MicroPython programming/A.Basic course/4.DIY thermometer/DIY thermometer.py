from microbit import *

while True:
    value = temperature()
    display.scroll(str(value))
    sleep(500)
