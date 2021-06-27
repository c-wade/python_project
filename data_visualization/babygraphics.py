"""
File: babygraphics.py
Author: Wade Chao
Overview:
    - Description: This program arranges the data of baby names ranking from 1900 to 2010
                   and displays the statistical data with line chart
    - Dependencies: tkinter
    - Test input: Jennifer Lucy Wade
    - To test it: Enter the test input in the Names searching bar in the upper-left corner of the gui window
    - Data sources: https://www.ssa.gov/OACT/babynames/
----------------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
GRAPH_MARGIN_SIZE = 20
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
MAX_RANK = 1000
TEXT_DX = 2
FIXED_LINE_WIDTH = 2
FIXED_LINE_COLOR = 'black'
FIXED_FONT = 'times 14'
COLORS = ['red', 'purple', 'green', 'blue']
LINE_WIDTH = 1
FONT = 'times 12'


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    area_width = width - 2 * GRAPH_MARGIN_SIZE
    gap = area_width // len(YEARS)

    return GRAPH_MARGIN_SIZE + (gap * year_index)


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # draw top horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=FIXED_LINE_WIDTH, fill=FIXED_LINE_COLOR)
    # draw bot horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, width=FIXED_LINE_WIDTH, fill=FIXED_LINE_COLOR)
    # draw years indicators text
    for i in range(len(YEARS)):
        x_coord = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_coord, 0, x_coord, CANVAS_HEIGHT, width=FIXED_LINE_WIDTH, fill=FIXED_LINE_COLOR)
        canvas.create_text(x_coord, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW,
                           font=FIXED_FONT, fill=FIXED_LINE_COLOR)


def get_y_coordinate(rank_number):
    """
    Given the rank number, return the y coordinate
    """
    if rank_number is None:
        return CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
    else:
        y_area = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK
        y_coord = y_area * (rank_number - 1) + 20
        return y_coord


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # Write your code below this line
    #################################
    for name in lookup_names:
        color_index = lookup_names.index(name) % len(COLORS)
        if name in name_data:
            draw_text(canvas, name_data, name, COLORS[color_index])
            draw_line(canvas, name_data, name, COLORS[color_index])


def draw_text(canvas, name_data, name, color):
    """
    Draw the text (name and rank) at the position in the graphic
    according to the year and rank of the name in the data list.

    :param canvas: (Tkinter Canvas) The canvas on which we are drawing.
    :param name_data: (dict) Dictionary holding baby name data
    :param name: (str) The name in the name_data
    :param color: The color of the text
    :return: This function does not return any value.
    """
    for i in range(len(YEARS)):
        year = str(YEARS[i])
        rank = int(name_data[name][year]) if year in name_data[name] else None
        text = f'{name}, {rank}' if rank is not None else f'{name}, *'
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX,
                           get_y_coordinate(rank),
                           text=text,
                           anchor=tkinter.SW,
                           font=FONT,
                           fill=color)


def draw_line(canvas, name_data, name, color):
    """
    Draw the lines in the graphic according to the years and ranks of
    the name in the data list.

    :param canvas: (Tkinter Canvas) The canvas on which we are drawing.
    :param name_data: (dict) Dictionary holding baby name data
    :param name: (str) The name in the name_data
    :param color: The color of the text
    :return: This function does not return any value.
    """
    for i in range(len(YEARS) - 1):
        year = str(YEARS[i])
        next_year = str(YEARS[i + 1])
        rank = int(name_data[name][year]) if year in name_data[name] else None
        next_rank = int(name_data[name][next_year]) if next_year in name_data[name] else None
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i),
                           get_y_coordinate(rank),
                           get_x_coordinate(CANVAS_WIDTH, i + 1),
                           get_y_coordinate(next_rank),
                           width=LINE_WIDTH,
                           fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
