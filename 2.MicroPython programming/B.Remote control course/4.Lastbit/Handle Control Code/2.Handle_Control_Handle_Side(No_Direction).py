# 手柄控制手柄端
from microbit import *
# 导入手手柄控制模块 Import the hand control control module
import ghandle
# 导入无线模块 Import the radio module
import radio

display.show(Image.HEART)
# 初始化无线模块 Initialize the radio module
radio.on()
# 设置无线组号 Set the radio group number
radio.config(group=1)

while True:
    # 摇杆控制 Control the joystick
    if ghandle.rocker(ghandle.up):
        radio.send('A')
    elif ghandle.rocker(ghandle.down):
        radio.send('B')
    elif ghandle.rocker(ghandle.left):
        radio.send('C')
    elif ghandle.rocker(ghandle.right):
        radio.send('D')
    # 摇杆按下 Press the joystick
    elif ghandle.rocker(ghandle.pressed):
        radio.send('I')
    elif not (ghandle.rocker(ghandle.up) or ghandle.rocker(ghandle.down) or 
              ghandle.rocker(ghandle.left) or ghandle.rocker(ghandle.right) or 
              ghandle.rocker(ghandle.pressed)):
        radio.send('0')
    # B1-B4 按钮控制 Control the servo
    if ghandle.B1_is_pressed():
        radio.send('E')
    
    if ghandle.B2_is_pressed():
        radio.send('F')
    
    if ghandle.B3_is_pressed():
        radio.send('G')
    
    if ghandle.B4_is_pressed():
        radio.send('H')
    # A/B 按钮控制
    # Control the claw
    if button_a.is_pressed():
        radio.send('N')
    elif button_b.is_pressed():
        radio.send('O')
