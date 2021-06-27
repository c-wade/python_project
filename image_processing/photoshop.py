"""
File: photoshop.py
Author: Wade Chao
Description: Remove people in the pictures and get pretty photos.
Dependencies: SimpleImage, Pillow
----------------------------------------------
!!IMPORTANT!!
To run the program, open the terminal and get to the directory of this folder, input:
- Mac
1. python3 photoshop.py clock-tower
2. python3 photoshop.py hoover
3. python3 photoshop.py math-corner
4. python3 photoshop.py monster

- Windows
1. py photoshop.py clock-tower
2. py photoshop.py hoover
3. py photoshop.py math-corner
4. py photoshop.py monster
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    return ((red-pixel.red)**2+(green-pixel.green)**2+(blue-pixel.blue)**2)**0.5


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    r_total, g_total, b_total = 0, 0, 0
    for pixel in pixels:
        r_total += pixel.red
        g_total += pixel.green
        b_total += pixel.blue

    return [r_total//len(pixels), g_total//len(pixels), b_total//len(pixels)]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    pixel_avg = get_average(pixels)
    best_pixel = pixels[0]
    best_pixel_dist = get_pixel_dist(pixels[0], pixel_avg[0], pixel_avg[1], pixel_avg[2])
    for pixel in pixels[1:]:
        dist = get_pixel_dist(pixel, pixel_avg[0], pixel_avg[1], pixel_avg[2])
        if dist < best_pixel_dist:
            best_pixel = pixel

    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    for x in range(result.width):
        for y in range(result.height):
            pixels_list = []
            for img in images:
                pixel = img.get_pixel(x, y)
                pixels_list.append(pixel)
            best_pixel = get_best_pixel(pixels_list)
            result.get_pixel(x, y).red = best_pixel.red
            result.get_pixel(x, y).green = best_pixel.green
            result.get_pixel(x, y).blue = best_pixel.blue
            pixels_list.clear()
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
