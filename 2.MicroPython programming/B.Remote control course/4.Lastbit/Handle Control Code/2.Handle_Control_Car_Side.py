# 导入无线模块 Import the radio module
import radio
# 导入小车模块 Import the car module
from lastbit import LASTBIT
from microbit import *
from utime import ticks_ms

Lastbit = LASTBIT()


g_speed = 255
SERVO_STEP = 2
SERVO_INTERVAL_MS = 25


s1 = 90  # 夹爪
s2 = 90  # 俯仰
s3 = 90  # 左右

servo_action = None
servo_time = 0
# 显示笑脸 Show the happy face
display.show(Image.HAPPY)
# 初始化无线模块 Initialize the radio module
radio.on()
# 设置无线组号 Set the radio group number
radio.config(group=1)
# 初始化舵机 Initialize the servo
Lastbit.set_servo('S1', s1)
Lastbit.set_servo('S2', s2)
Lastbit.set_servo('S3', s3)
sleep(1000)
# 显示"T" Show the "T"
display.show(Image("99999:""00900:""00900:""00900:""00900"))

# 舵机控制 Control the servo
def servo_control():
    global servo_time, s1, s2, s3

    now = ticks_ms()
    if now - servo_time < SERVO_INTERVAL_MS:
        return
    servo_time = now

    if servo_action == "S1+":
        s1 = min(165, s1 + SERVO_STEP)
        Lastbit.set_servo('S1', s1)
    elif servo_action == "S1-":
        s1 = max(60, s1 - SERVO_STEP)
        Lastbit.set_servo('S1', s1)

    elif servo_action == "S2+":
        s2 = min(150, s2 + SERVO_STEP)
        Lastbit.set_servo('S2', s2)
    elif servo_action == "S2-":
        s2 = max(60, s2 - SERVO_STEP)
        Lastbit.set_servo('S2', s2)

    elif servo_action == "S3+":
        s3 = min(170, s3 + SERVO_STEP)
        Lastbit.set_servo('S3', s3)
    elif servo_action == "S3-":
        s3 = max(20, s3 - SERVO_STEP)
        Lastbit.set_servo('S3', s3)


while True:
    # 接收无线信号 Receive the radio signal
    value = radio.receive()
    now = ticks_ms()

    # 如果没有收到信号，停止小车 If no signal is received, stop the car
    if value is None:
        Lastbit.stop_motor()
        servo_action = None
        continue

    # 小车运动方向控制 Control the direction
    if value == "A":
        Lastbit.car_control('FORWARD', g_speed)
    elif value == "B":
        Lastbit.car_control('BACKWARD', g_speed)
    elif value == "C":
        Lastbit.car_control('SPINLEFT', g_speed)
    elif value == "D":
        Lastbit.car_control('SPINRIGHT', g_speed)

    # 舵机夹爪控制 Control the servo claw
    elif value == "N":
        servo_action = "S1+"
    elif value == "O":
        servo_action = "S1-"
    # 舵机俯仰控制 Control the servo pitch
    elif value == "F":
        servo_action = "S2+"
        Lastbit.all_lights_set_color(0, 70, 0)
    elif value == "G":
        servo_action = "S2-"
        Lastbit.all_lights_set_color(0, 0, 70)
    # 舵机左右控制 Control the servo left and right
    elif value == "E":
        servo_action = "S3+"
        Lastbit.all_lights_set_color(70, 0, 0)
    elif value == "H":
        servo_action = "S3-"
        Lastbit.all_lights_set_color(70, 70, 0)
    # 摇杆按下 Press the joystick
    elif value == "I":
        Lastbit.all_lights_off()

    servo_control()