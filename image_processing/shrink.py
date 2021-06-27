"""
File: shrink.py
Author: Wade Chao
Dependencies: SimpleImage, Pillow
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    get even row and column pixels to shrink the image
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width//2, img.height//2)
    for x in range(b_img.width):
        for y in range(b_img.height):
            b_img.get_pixel(x, y).red = img.get_pixel(x*2, y*2).red
            b_img.get_pixel(x, y).green = img.get_pixel(x*2, y*2).green
            b_img.get_pixel(x, y).blue = img.get_pixel(x*2, y*2).blue
    return b_img


def main():
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
