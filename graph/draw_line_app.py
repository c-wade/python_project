"""
File:
Name:
-------------------------
TODO:
"""
from app import App
from campy.graphics.gobjects import GOval, GLine
from campy.gui.events.mouse import onmouseclicked


class DrawLineApp(App):
    DEFAULT_APP_NAME = 'Draw Line Master App'
    DEFAULT_OVAL_SIZE = 10

    def __init__(
            self,
            app_name=DEFAULT_APP_NAME,
            window_width=App.DEFAULT_WIDTH,
            window_height=App.DEFAULT_HEIGHT,
            oval_size=DEFAULT_OVAL_SIZE
    ):
        super().__init__(app_name, window_width, window_height)
        self.__oval_size = oval_size
        self.__start_point = GOval(self.__oval_size, self.__oval_size)
        self.__should_draw_line = False

    def start(self):
        onmouseclicked(self.__draw_line)

    def __draw_line(self, event):
        if self.__should_draw_line:
            self.__connect_point(event)
            self.__should_draw_line = False
        else:
            self.__set_point(event)
            self.__should_draw_line = True

    def __set_point(self, event):
        self._window.add(self.__start_point, (event.x - self.__oval_size / 2), (event.y - self.__oval_size / 2))

    def __connect_point(self, event):
        self._window.add(
            GLine(
                (self.__start_point.x + self.__oval_size / 2),
                (self.__start_point.y + self.__oval_size / 2),
                event.x,
                event.y
            )
        )
        self._window.remove(self.__start_point)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    DrawLineApp().start()


if __name__ == "__main__":
    main()
