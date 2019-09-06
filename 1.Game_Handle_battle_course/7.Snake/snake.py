from microbit import *
from random import randint
import music

score = 0
snake = [[0, 0]]
food = [randint(1, 4), randint(1, 4)]
directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
global direction  # 0: ? 1?? 2??  3??
direction = 0


def Rocker_loop_test():
    direction = -1
    x = pin1.read_analog()
    y = pin2.read_analog()

    if x < 200:  # ?
        direction = 1
    elif x > 900:  # ?
        direction = 3
    else:
        if y < 200:  # ?
            direction = 0
        elif y > 900:  # ?
            direction = 2
    return direction


while True:
    if len(snake) == 25:
        music.play(music.CHASE)
        display.scroll("Win")
        display.scroll("Score:")
        display.scroll(str(score))
    display.clear()
    display.set_pixel(food[0], food[1], 9)
    for i in range(len(snake)):
        (display.set_pixel(snake[i][0], snake[i][1],
         int(5 - (i/len(snake)*5) % 5 + 2)))
    sleep(800)
    c = Rocker_loop_test()
    if c != -1:
        direction = c
    a = (snake[0][0] + directions[direction][0]) % 5
    b = (snake[0][1] + directions[direction][1]) % 5
    next_block = [a, b]

    if next_block in snake:
        music.play(music.CHASE)
        display.scroll("Game Over")
        display.scroll("Score:")
        display.scroll(str(score))
        break
    snake = [next_block] + snake
    if next_block == food:
        while food in snake:
            food = [randint(0, 4), randint(0, 4)]
            score = score + 1
    else:
        snake.pop()
