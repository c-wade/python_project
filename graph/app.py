from campy.graphics.gwindow import GWindow


class App(object):
    DEFAULT_WIDTH = 800
    DEFAULT_HEIGHT = 800

    def __init__(self, app_name, window_width=DEFAULT_WIDTH, window_height=DEFAULT_HEIGHT):
        self._window = GWindow(width=window_width, height=window_height, title=app_name)
