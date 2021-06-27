"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width, img.height * 2)
    for x in range(img.width):
        for y in range(img.height):
            b_img.get_pixel(x, y).red = img.get_pixel(x, y).red
            b_img.get_pixel(x, y).blue = img.get_pixel(x, y).blue
            b_img.get_pixel(x, y).green = img.get_pixel(x, y).green
            b_img.get_pixel(x, b_img.height - 1 - y).red = img.get_pixel(x, y).red
            b_img.get_pixel(x, b_img.height - 1 - y).blue = img.get_pixel(x, y).blue
            b_img.get_pixel(x, b_img.height - 1 - y).green = img.get_pixel(x, y).green

    return b_img


def main():
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
