"""
File: green_screen.py
Author: Wade Chao
Dependencies: SimpleImage, Pillow
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage

# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.3

# Controls the upper bound for black pixel
BLACK_PIXEL = 120


def combine(background_img, figure_img):
    """
    remove figure-image's green background and combine with background-image
    """
    background_img.make_as_big_as(figure_img)
    for x in range(background_img.width):
        for y in range(background_img.height):
            figure_pixel = figure_img.get_pixel(x, y)
            total = figure_pixel.red + figure_pixel.blue + figure_pixel.green
            avg = total // 3
            if figure_pixel.green > avg*THRESHOLD and total > BLACK_PIXEL:
                bg_pixel = background_img.get_pixel(x, y)
                figure_pixel.red = bg_pixel.red
                figure_pixel.blue = bg_pixel.blue
                figure_pixel.green = bg_pixel.green
    return figure_img


def main():
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
