"""
File: breakoutgraphics.py
Author: Wade Chao
----------------------------------------
** pip install campy **
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao
"""
from time import time
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.
DEFAULT_BRICK_COLORS_LIST = ['red', 'orange', 'yellow', 'green', 'blue']
FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3  # Number of attempts


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 brick_color_list=None, title='Breakout'):
        self.__ball_radius = ball_radius
        self.__paddle_width = paddle_width
        self.__paddle_height = paddle_height
        self.__paddle_offset = paddle_offset
        self.__brick_rows = brick_rows
        self.__brick_cols = brick_cols
        self.__brick_width = brick_width
        self.__brick_height = brick_height
        self.__brick_offset = brick_offset
        self.__brick_spacing = brick_spacing
        self.__brick_color_list = brick_color_list if brick_color_list is not None else DEFAULT_BRICK_COLORS_LIST
        self.__title = title
        self.__num_lives = NUM_LIVES
        self.__score = 0

        # Create all elements
        self.__window = self.__create_window()
        self.__paddle = self.__create_paddle()
        self.__ball = self.__create_ball()
        self.__bricks_total = 0
        self.__record = self.__get_record_board()
        self.__init_elements_on_window()
        # Default initial velocity for the ball
        self.__playing = False
        self.__set_ball_velocity()

    """
    Entry function, invoke to start the game
    """

    def start(self):
        # Initialize mouse listeners to start the game
        onmouseclicked(self.__handle_click)
        onmousemoved(self.__handle_mouse_move)

    """
    Create all elements
    """

    def __create_window(self):
        window_width = self.__brick_cols * (self.__brick_width + self.__brick_spacing) - self.__brick_spacing
        window_height = self.__brick_offset + 3 * (
                self.__brick_rows * (self.__brick_height + self.__brick_spacing) - self.__brick_spacing)
        return GWindow(width=window_width, height=window_height, title=self.__title)

    def __create_paddle(self):
        rect = GRect(self.__paddle_width, self.__paddle_height)
        rect.filled = True
        return rect

    def __create_ball(self):
        ball = GOval(self.__ball_radius, self.__ball_radius)
        ball.filled = True
        return ball

    def __create_brick(self, color='black'):
        brick = GRect(self.__brick_width, self.__brick_height)
        brick.filled = True
        brick.fill_color = color
        return brick

    def __get_record_board(self):
        record = GLabel(f'Score: {self.__score}  Lives: {self.__num_lives}')
        return record

    """
    Put all elements on window
    """

    def __init_elements_on_window(self):
        # put paddle
        self.__set_paddle_position()
        # put ball
        self.__set_ball_position()
        # put bricks
        self.__put_bricks_on_window()
        # put score board
        self.__set_record_board()

    def __put_bricks_on_window(self):
        """
        Create all bricks with color in the color list
        Put bricks on window
        """
        offset_x = 0
        offset_y = self.__brick_offset
        color_index = 0
        for i in range(self.__brick_rows):
            if i > 0 and i % 2 == 0:
                color_index = color_index + 1 if color_index + 1 < len(self.__brick_color_list) else 0
            for j in range(self.__brick_cols):
                self.__window.add(self.__create_brick(color=self.__brick_color_list[color_index]), offset_x, offset_y)
                self.__bricks_total += 1
                offset_x += self.__brick_width + self.__brick_spacing
            offset_y += self.__brick_height + self.__brick_spacing
            offset_x = 0

    def __set_ball_position(self):
        """
        Put the ball at the center of the window
        """
        self.__window.remove(self.__ball)
        self.__window.add(self.__ball, (self.__window.width - self.__ball.width) / 2,
                          (self.__window.height - self.__ball.height) / 2)

    def __set_paddle_position(self):
        """
        Put the paddle in the middle of the window
        """
        self.__window.remove(self.__paddle)
        self.__window.add(self.__paddle, (self.__window.width - self.__paddle.width) / 2,
                          self.__window.height - self.__paddle_offset)

    def __set_ball_velocity(self):
        """
        Set the velocity for the movement of the ball
        """
        self.__dx = random.randint(1, MAX_X_SPEED) if random.random() < 0.5 else -random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED

    def __set_record_board(self):
        record_position_x = 5
        record_position_y = self.__window.height - self.__record.height
        self.__window.remove(self.__window.get_object_at(record_position_x, record_position_y))
        self.__window.add(self.__get_record_board(), record_position_x, record_position_y)

    """
    Handle events
    """

    def __handle_click(self, event):
        """
        Handle the click event, move the pall if:
        1. The ball is freeze at the center of the window
        2. Number of bricks are greater than 0
        3. Number of lives are greater than 0
        """
        if not self.__playing and self.__bricks_total > 0 and self.__num_lives > 0:
            self.__playing = True
            self.__move_ball()

    def __handle_mouse_move(self, event):
        """
        Handle the mouse move event, user is allowed to control the paddle when:
        1. The ball is moving in the window
        2. Number of bricks are greater than 0
        3. Number of lives are greater than 0
        """
        if not self.__game_is_over():
            paddle_x = event.x - (self.__paddle.width / 2)
            if paddle_x <= 0:
                self.__paddle.x = 0
            elif paddle_x + self.__paddle.width >= self.__window.width:
                self.__paddle.x = self.__window.width - self.__paddle.width
            else:
                self.__paddle.x = paddle_x

    def __move_ball(self):
        """
        Moving the ball if game is not over
        Handle the collision of the ball
        """
        while not self.__game_is_over():
            self.__ball.move(self.__dx, self.__dy)
            self.__handle_wall_collision()
            if self.__num_lives == 0:
                self.__game_over_picture()
                break
            elif self.__bricks_total == 0:
                self.__game_over_picture('You Win!!')
                break
            pause(FRAME_RATE)

    def __handle_wall_collision(self):
        """
        Handle rebound when the ball hit the wall, paddle, and bricks
        """
        if self.__ball.x <= 0 or self.__ball.x + self.__ball.width >= self.__window.width:
            self.__dx = - self.__dx

        next_target_top = self.__window.get_object_at(self.__ball.x + self.__dx*1.5, self.__ball.y + self.__dy*1.5)
        next_target_bot = self.__window.get_object_at(self.__ball.x + self.__ball.width + self.__dx*1.5,
                                                      self.__ball.y + self.__ball.height + self.__dy*1.5)

        if self.__hit_paddle(next_target_top) or self.__hit_paddle(next_target_bot):
            self.__dy = - abs(self.__dy)
            if self.__ball.x <= self.__paddle.x + 20:
                # The ball will fly left if hit the left of the paddle
                self.__dx = - abs(self.__dx)
            elif self.__ball.x > self.__paddle.x + self.__paddle.width - 20:
                # The ball will fly right if hit the right of the paddle
                self.__dx = abs(self.__dx)
        elif self.__hit_bricks(next_target_top) or self.__hit_bricks(next_target_bot):
            target_brick = next_target_top if next_target_top else next_target_bot
            self.__remove_brick(target_brick)
            self.__dy = - self.__dy
        elif self.__ball.y <= 0:
            self.__dy = - self.__dy
        elif self.__ball.y + self.__ball.height >= self.__window.height:
            self.__num_lives -= 1
            self.__playing = False
            self.__set_ball_position()
            self.__set_paddle_position()
            self.__set_ball_velocity()
            self.__set_record_board()

    def __remove_brick(self, g_object):
        """
        Remove a brick which has been hitted by the ball
        """
        if type(g_object) == GRect:
            self.__window.remove(g_object)
            self.__bricks_total -= 1
            self.__score += 1
            self.__set_record_board()

    def __game_is_over(self):
        """
        To see if the
        :return: bool
        """
        return not (self.__playing and self.__bricks_total > 0 and self.__num_lives > 0)

    def __game_over_picture(self, txt='Game Over'):
        label = GLabel(txt)
        self.__window.clear()
        self.__bricks_total = 0
        self.__num_lives = 0
        self.__playing = False
        self.__window.add(label, (self.__window.width - label.width) / 2, (self.__window.height - label.height) / 2)

    def __hit_paddle(self, g_object):
        """
        To see if the ball hit the paddle
        :return: bool
        """
        return g_object == self.__paddle

    def __hit_bricks(self, g_object):
        """
        To see if the ball hit the bricks
        :return:  bool
        """
        return type(g_object) == GRect and g_object != self.__paddle
