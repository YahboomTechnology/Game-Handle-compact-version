from microbit import *

compass.calibrate()

while not compass.is_calibrated():
    pass

while True:
    azimuth = compass.heading()
    if azimuth >= 0 and azimuth < 45:
        display.show(Image.ARROW_NW)
    elif azimuth >= 45 and azimuth < 90:
        display.show(Image.ARROW_W)
    elif azimuth >= 90 and azimuth < 135:
        display.show(Image.ARROW_SW)
    elif azimuth >= 135 and azimuth < 180:
        display.show(Image.ARROW_S)
    elif azimuth >= 180 and azimuth < 225:
        display.show(Image.ARROW_SE)
    elif azimuth >= 225 and azimuth < 270:
        display.show(Image.ARROW_E)
    elif azimuth >= 270 and azimuth < 315:
        display.show(Image.ARROW_NE)
    elif azimuth >= 315 and azimuth < 360:
        display.show(Image.ARROW_N)