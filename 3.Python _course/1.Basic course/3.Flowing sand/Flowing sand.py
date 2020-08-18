from microbit import *
import microbit

up = Image("00000:"
           "00000:"
           "99999:"
           "99999:"
           "99999")

down = Image("99999:"
             "99999:"
             "99999:"
             "00000:"
             "00000")

left = Image("99900:"
             "99900:"
             "99900:"
             "99900:"
             "99900")

right = Image("00999:"
              "00999:"
              "00999:"
              "00999:"
              "00999")

while True:
    gesture = accelerometer.current_gesture()
    if gesture == "face up":
        display.show(Image.HAPPY)
    elif gesture == "shake":
        display.show(Image.CHESSBOARD)
    elif gesture == "up":
        display.show(up)
    elif gesture == "down":
        display.show(down)
    elif gesture == "left":
        display.show(left)
    elif gesture == "right":
        display.show(right)

