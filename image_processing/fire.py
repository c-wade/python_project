"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    turn the image to gray color and highlight fires with red color
    """
    img = SimpleImage(filename)
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            avg = (pixel.red + pixel.green + pixel.blue) // 3
            if pixel.red > avg * HURDLE_FACTOR:
                pixel.red = 255
                pixel.green = 0
                pixel.blue = 0
            else:
                pixel.red = avg
                pixel.green = avg
                pixel.blue = avg
    return img


def main():
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
