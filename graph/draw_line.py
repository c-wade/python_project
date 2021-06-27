"""
File: draw_line.py
Author: Wade Chao
-------------------------
** pip install campy **
Click on the window to draw lines
"""
from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
TITLE = 'Draw Line Master'
OVAL_SIZE = 10

window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, title=TITLE)
start_point = GOval(OVAL_SIZE, OVAL_SIZE)
should_draw_line = False


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(event):
    global should_draw_line
    if should_draw_line:
        connect_point(event)
        should_draw_line = False
    else:
        set_point(event)
        should_draw_line = True


def set_point(event):
    window.add(start_point, (event.x-OVAL_SIZE/2), (event.y-OVAL_SIZE/2))


def connect_point(event):
    line = GLine((start_point.x+OVAL_SIZE/2), (start_point.y+OVAL_SIZE/2), event.x, event.y)
    window.add(line)
    window.remove(start_point)


if __name__ == "__main__":
    main()
