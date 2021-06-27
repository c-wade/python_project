"""
File: bouncing_ball.py
Author: Wade Chao
Dependencies: campy
-------------------------
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
ball.filled = True
chance_to_play = 3
speed = GRAVITY
num_of_rebound = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    init_ball_position()
    onmouseclicked(drop_ball)


def drop_ball(event):
    """
    pre-condition:
        The ball is at the starting position
    post-condition:
        The ball has been dropped for three times, put it back at the starting position and stop the game
    """
    global chance_to_play, num_of_rebound
    out_of_window = False
    while not out_of_window and chance_to_play:
        if ball.x >= window.width:
            out_of_window = True
            chance_to_play -= 1
            init_ball_position()
        elif ball.y >= window.height - SIZE:
            num_of_rebound += 1
            reduce = calculate_reduce_ratio()
            bounce(reduce)
        else:
            drop()


def drop():
    """
    Drop the ball and increase the speed
    """
    global speed
    while ball.x < window.width and ball.y < window.height - SIZE:
        ball.x += VX
        if ball.y + speed > window.height - SIZE:
            ball.y = window.height - SIZE
        else:
            ball.y += speed
            speed += GRAVITY
        pause(DELAY)


def bounce(reduce):
    """
    The ball rebound from the ground,
    going up until run out of the energy (speed)
    :param reduce: ratio for reducing the speed
    """
    global speed
    while ball.x < window.width and speed >= 0:
        ball.x += VX
        ball.y -= speed
        speed -= GRAVITY/reduce
        pause(DELAY)


def calculate_reduce_ratio():
    """
    Get reduce ratio for rebound
    """
    reduce = 1
    for i in range(num_of_rebound):
        reduce *= REDUCE
    return reduce


def init_ball_position():
    """
    Initialize ball position, speed of drop/bounce, and number of rebound
    :return:
    """
    global speed, num_of_rebound
    window.remove(ball)
    window.add(ball, START_X, START_Y)
    speed = GRAVITY
    num_of_rebound = 0


if __name__ == "__main__":
    main()
