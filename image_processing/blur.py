"""
File: blur.py
Author: Wade Chao
Dependencies: SimpleImage, Pillow
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage
BLUR_LEVEL = 5


def blur(img):
    blurred_img = img.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            r_avg, g_avg, b_avg = get_rgb_avg(img, x, y)
            blurred_img.get_pixel(x, y).red = r_avg
            blurred_img.get_pixel(x, y).green = g_avg
            blurred_img.get_pixel(x, y).blue = b_avg
    return blurred_img


def get_rgb_avg(img, x, y):
    pixels_count = 0
    r_total, g_total, b_total = 0, 0, 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 < x+i < img.width and 0 < y+j < img.height:
                pixel = img.get_pixel(x+i, y+j)
                r_total += pixel.red
                g_total += pixel.green
                b_total += pixel.blue
                pixels_count += 1
    return r_total//pixels_count, g_total//pixels_count, b_total//pixels_count


def main():
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(BLUR_LEVEL):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
