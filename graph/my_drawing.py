"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLine
from campy.graphics.gwindow import GWindow
import random

window = GWindow(width=1000, height=650, title="Outer Space")
PIXEL_SIZE = 10

RED_1 = '#F77343'
RED_2 = '#E35504'
BLACK = '#000'
BODY = '#D6E5E7'
BODY_SHADOW = '#9DA9AB'
WINDOW_BLUE = '#78F5FA'
WINDOW_SHADOW = '#2BD7D7'
FIRE_YELLOW = '#FFDD00'
FIRE_RED = '#F85601'
FIRE_ORANGE = '#F6AA00'
NIGHT_BLACK = '#0F121C'
PLANET_1_OUTLINE = '#3E67E6'
PLANET_2_OUTLINE = '#842E2E'
PLANET_2_LIGHT = '#E9D3C6'
PLANET_2_LIGHT_1 = '#E9E1E1'
PLANET_2_LIGHT_2 = '#E38585'
PLANET_2_MID = '#E38585'
PLANET_2_MID_1 = '#AF5555'
PLANET_2_MID_2 = '#C74B39'
PLANET_2_MID_3 = '#C75454'
PLANET_2_MID_4 = '#C93737'
PLANET_2_ORANGE = '#C97F45'
PLANET_2_MUD = '#C6C245'
PLANET_2_GOLD = '#F4D577'
PLANET_2_MAROON = '#742E2E'
PLANET_2_SALMON = 'salmon'
PLANET_2_DARK = '#AF3232'
PLANET_2_DARK_1 = '#844F4F'
STAR_COLOR = ['#ABE8F1', '#475B63', '#F8DDFC', '#F8FED0']


def main():
    create_outer_space()
    pixel_rocket()
    create_astronaut()
    create_blue_planet()
    create_red_planet()
    create_green_planet()


def create_outer_space():
    night = GRect(window.width, window.height)
    night.filled = True
    night.fill_color = NIGHT_BLACK
    night.color = NIGHT_BLACK
    window.add(night)

    for i in range(50, random.randint(150, 180)):
        create_rect(random.randint(0, window.width), random.randint(0, window.height), random.choice(STAR_COLOR),
                    random.randint(1, 8))


def pixel_rocket():
    create_rocket_head()
    create_rocket_body()
    create_rocket_bottom()


def create_rocket_head():
    create_rect(490, 50, BLACK)
    # left
    create_rect(480, 60, BLACK)
    create_rect(470, 70, BLACK)
    create_rect(460, 80, BLACK)
    create_rect(450, 90, BLACK)
    create_rect(440, 100, BLACK)
    create_rect(440, 110, BLACK)
    # right
    create_rect(500, 60, BLACK)
    create_rect(510, 70, BLACK)
    create_rect(520, 80, BLACK)
    create_rect(530, 90, BLACK)
    create_rect(540, 100, BLACK)
    create_rect(540, 110, BLACK)
    # fill color
    create_rect(490, 60, RED_2)
    create_rect(480, 70, RED_1)
    create_rect(470, 80, RED_1)
    create_rect(460, 90, RED_1)
    create_rect(450, 100, RED_1)
    create_rect(450, 110, RED_1)
    for i in range(490, 510, 10):
        create_rect(i, 70, RED_2)
    for i in range(480, 520, 10):
        create_rect(i, 80, RED_2)
    for i in range(470, 530, 10):
        create_rect(i, 90, RED_2)
    for i in range(460, 540, 10):
        create_rect(i, 100, RED_2)
    for i in range(460, 540, 10):
        create_rect(i, 110, RED_2)


def create_rocket_body():
    for i in range(450, 540, 10):
        create_rect(i, 120, BLACK)
    # left
    create_rect(430, 120, BLACK)
    create_rect(420, 130, BLACK)
    create_rect(410, 140, BLACK)
    create_rect(410, 150, BLACK)
    create_rect(400, 160, BLACK)
    create_rect(400, 170, BLACK)
    create_rect(400, 180, BLACK)
    create_rect(390, 190, BLACK)
    create_rect(390, 200, BLACK)
    create_rect(390, 210, BLACK)
    create_rect(390, 220, BLACK)
    create_rect(380, 230, BLACK)
    create_rect(380, 240, BLACK)
    create_rect(380, 250, BLACK)
    create_rect(380, 260, BLACK)
    create_rect(380, 270, BLACK)
    create_rect(370, 280, BLACK)
    create_rect(370, 290, BLACK)
    create_rect(370, 300, BLACK)
    create_rect(370, 310, BLACK)
    create_rect(370, 320, BLACK)
    create_rect(370, 330, BLACK)
    create_rect(370, 340, BLACK)
    # right
    create_rect(550, 120, BLACK)
    create_rect(560, 130, BLACK)
    create_rect(570, 140, BLACK)
    create_rect(570, 150, BLACK)
    create_rect(580, 160, BLACK)
    create_rect(580, 170, BLACK)
    create_rect(580, 180, BLACK)
    create_rect(590, 190, BLACK)
    create_rect(590, 200, BLACK)
    create_rect(590, 210, BLACK)
    create_rect(590, 220, BLACK)
    create_rect(600, 230, BLACK)
    create_rect(600, 240, BLACK)
    create_rect(600, 250, BLACK)
    create_rect(600, 260, BLACK)
    create_rect(600, 270, BLACK)
    create_rect(610, 280, BLACK)
    create_rect(610, 290, BLACK)
    create_rect(610, 300, BLACK)
    create_rect(610, 310, BLACK)
    create_rect(610, 320, BLACK)
    create_rect(610, 330, BLACK)
    create_rect(610, 340, BLACK)

    # fill color
    # 120
    create_rect(440, 120, BODY)
    create_rect(540, 120, BODY_SHADOW)
    # 130
    for i in range(430, 560, 10):
        if i == 550:
            create_rect(i, 130, BODY_SHADOW)
        else:
            create_rect(i, 130, BODY)
    # 140 150
    for i in range(420, 570, 10):
        if 460 < i < 520:
            create_rect(i, 140, BLACK)
            if i == 470:
                create_rect(i, 150, 'white')
        elif i == 560:
            create_rect(i, 140, BODY_SHADOW)
            create_rect(i, 150, BODY_SHADOW)
        else:
            create_rect(i, 140, BODY)
            create_rect(i, 150, BODY)

        if i == 460 or i == 520:
            create_rect(i, 150, BLACK)
        elif 470 < i < 520:
            create_rect(i, 150, WINDOW_BLUE)
    # 160
    for i in range(410, 580, 10):
        if i == 450 or i == 530:
            create_rect(i, 160, BLACK)
        elif 460 < i < 530:
            create_rect(i, 160, WINDOW_BLUE)
        elif i == 460:
            create_rect(i, 160, 'white')
        else:
            if i == 570:
                create_rect(i, 160, BODY_SHADOW)
            elif i != 460:
                create_rect(i, 160, BODY)
    # 170
    for i in range(410, 580, 10):
        if i == 440 or i == 540:
            create_rect(i, 170, BLACK)
        elif 450 < i < 540:
            create_rect(i, 170, WINDOW_BLUE)
        elif i == 450:
            create_rect(i, 170, 'white')
        else:
            if i == 570:
                create_rect(i, 170, BODY_SHADOW)
            elif i != 450:
                create_rect(i, 170, BODY)
    # 180~270
    for i in range(390, 600, 10):
        if i == 430 or i == 550:
            create_rect(i, 180, BLACK)
            create_rect(i, 190, BLACK)
            create_rect(i, 200, BLACK)
            create_rect(i, 210, BLACK)
            create_rect(i, 220, BLACK)
            create_rect(i, 230, BLACK)
            create_rect(i, 240, BLACK)
        elif 430 < i < 550:
            color = WINDOW_SHADOW if i == 540 else WINDOW_BLUE
            if i > 440:
                create_rect(i, 180, color)
            elif i == 440:
                create_rect(i, 180, 'white')
            create_rect(i, 190, color)
            create_rect(i, 200, color)
            create_rect(i, 210, color)
            create_rect(i, 220, color)
            create_rect(i, 230, color)
            create_rect(i, 240, color)
        elif i == 590:
            create_rect(i, 230, BODY_SHADOW)
            create_rect(i, 240, BODY_SHADOW)
        else:
            create_rect(i, 230, BODY)
            create_rect(i, 240, BODY)
            if 390 < i < 580:
                if 400 < i < 570:
                    create_rect(i, 180, BODY)
                elif i == 570:
                    create_rect(i, 180, BODY_SHADOW)
                create_rect(i, 190, BODY)
                create_rect(i, 200, BODY)
                create_rect(i, 210, BODY)
                create_rect(i, 220, BODY)
            elif i == 580:
                create_rect(i, 190, BODY_SHADOW)
                create_rect(i, 200, BODY_SHADOW)
                create_rect(i, 210, BODY_SHADOW)
                create_rect(i, 220, BODY_SHADOW)
                create_rect(i, 230, BODY_SHADOW)

        if i == 440 or i == 540:
            create_rect(i, 250, BLACK)
        elif 440 < i < 540:
            if i == 530:
                create_rect(i, 250, WINDOW_SHADOW)
            else:
                create_rect(i, 250, WINDOW_BLUE)
        elif i == 590:
            create_rect(i, 250, BODY_SHADOW)
        else:
            create_rect(i, 250, BODY)
        if i == 450 or i == 530:
            create_rect(i, 260, BLACK)
        elif 450 < i < 530:
            if i == 520:
                create_rect(i, 260, WINDOW_SHADOW)
            else:
                create_rect(i, 260, WINDOW_BLUE)
        elif i == 590:
            create_rect(i, 260, BODY_SHADOW)
        else:
            create_rect(i, 260, BODY)
        if i == 460 or i == 520:
            create_rect(i, 270, BLACK)
        elif 460 < i < 520:
            create_rect(i, 270, WINDOW_SHADOW)
        elif i == 590:
            create_rect(i, 270, BODY_SHADOW)
        else:
            create_rect(i, 270, BODY)
    # 280~300
    for i in range(380, 590, 10):
        if i == 460 or i == 520:
            create_rect(i, 280, BODY)
        elif 470 <= i <= 510:
            create_rect(i, 280, BLACK)
        else:
            create_rect(i, 280, BODY)
        create_rect(i, 290, BODY)
        create_rect(i, 300, BODY)

    for i in range(590, 610, 10):
        for j in range(280, 310, 10):
            create_rect(i, j, BODY_SHADOW)

    create_rect(380, 310, BLACK)
    create_rect(390, 310, BLACK)
    create_rect(590, 310, BLACK)
    create_rect(600, 310, BLACK)
    for i in range(400, 590, 10):
        create_rect(i, 310, BODY)

    create_rect(380, 320, RED_2)
    create_rect(390, 320, RED_2)
    create_rect(590, 320, RED_2)
    create_rect(600, 320, RED_2)
    for i in range(400, 590, 10):
        create_rect(i, 320, BLACK)

    create_rect(380, 330, BLACK)
    create_rect(390, 330, RED_2)
    create_rect(400, 330, RED_2)
    create_rect(410, 330, BLACK)
    create_rect(420, 330, RED_2)
    create_rect(430, 330, RED_2)
    create_rect(440, 330, RED_2)
    create_rect(450, 330, BLACK)
    create_rect(460, 330, RED_2)
    create_rect(470, 330, RED_2)
    create_rect(480, 330, RED_2)
    create_rect(490, 330, BLACK)
    create_rect(500, 330, RED_2)
    create_rect(510, 330, RED_2)
    create_rect(520, 330, RED_2)
    create_rect(530, 330, BLACK)
    create_rect(540, 330, RED_2)
    create_rect(550, 330, RED_2)
    create_rect(560, 330, RED_2)
    create_rect(570, 330, BLACK)
    create_rect(580, 330, RED_2)
    create_rect(590, 330, RED_2)
    create_rect(600, 330, BLACK)

    for i in range(380, 610, 10):
        if i == 380 or i == 600:
            create_rect(i, 340, BODY)
        else:
            create_rect(i, 340, BLACK)


def create_rocket_bottom():
    # 350 360
    for i in range(380, 610, 10):
        if i == 380 or i == 600:
            create_rect(i, 350, BLACK)
            create_rect(i, 360, BLACK)
        elif i == 590:
            create_rect(i, 350, BODY_SHADOW)
            create_rect(i, 360, BODY_SHADOW)
        else:
            create_rect(i, 350, BODY)
            create_rect(i, 360, BODY)
    # 370
    for i in range(370, 620, 10):
        if 370 <= i <= 380 or 600 <= i <= 610:
            create_rect(i, 370, BLACK)
        elif i == 590:
            create_rect(i, 370, BODY_SHADOW)
        else:
            create_rect(i, 370, BODY)
    # 380
    for i in range(360, 630, 10):
        if i == 360 or i == 620 or i == 380 or i == 600 or i == 490:
            create_rect(i, 380, BLACK)
        elif i == 590:
            create_rect(i, 380, BODY_SHADOW)
        elif i == 370 or i == 610:
            create_rect(i, 380, RED_1)
        else:
            create_rect(i, 380, BODY)
    # 390
    for i in range(350, 640, 10):
        if i == 350 or i == 630 or i == 380 or i == 600 or i == 500 or i == 480:
            create_rect(i, 390, BLACK)
        elif i == 590 or i == 580:
            create_rect(i, 390, BODY_SHADOW)
        elif i == 370 or i == 610 or i == 490:
            create_rect(i, 390, RED_2)
        elif i == 360 or i == 620:
            create_rect(i, 390, RED_1)
        else:
            create_rect(i, 390, BODY)
    # 400 410
    for i in range(340, 650, 10):
        if i == 340 or i == 640 or i == 390 or i == 590 or i == 500 or i == 480:
            create_rect(i, 400, BLACK)
            create_rect(i, 410, BLACK)
        elif i == 580:
            create_rect(i, 400, BODY_SHADOW)
            create_rect(i, 410, BODY_SHADOW)
        elif 360 <= i <= 380 or 600 <= i <= 620 or i == 490:
            create_rect(i, 400, RED_2)
            create_rect(i, 410, RED_2)
        elif i == 350 or i == 630:
            create_rect(i, 400, RED_1)
            create_rect(i, 410, RED_1)
        else:
            create_rect(i, 400, BODY)
            create_rect(i, 410, BODY)
    # 420
    for i in range(340, 650, 10):
        if i == 340 or i == 640 or i == 400 or i == 580 or i == 500 or i == 480:
            create_rect(i, 420, BLACK)
        elif i == 570 or i == 560:
            create_rect(i, 420, BODY_SHADOW)
        elif 360 <= i <= 390 or 590 <= i <= 620 or i == 490:
            create_rect(i, 420, RED_2)
        elif i == 350 or i == 630:
            create_rect(i, 420, RED_1)
        else:
            create_rect(i, 420, BODY)
    # 430
    for i in range(340, 650, 10):
        if i == 340 or i == 640 or i == 410 or i == 570 or i == 500 or i == 480:
            create_rect(i, 430, BLACK)
        elif i == 560 or i == 550:
            create_rect(i, 430, BODY_SHADOW)
        elif 360 <= i <= 400 or 580 <= i <= 620 or i == 490:
            create_rect(i, 430, RED_2)
        elif i == 350 or i == 630:
            create_rect(i, 430, RED_1)
        else:
            create_rect(i, 430, BODY)
    # 440
    for i in range(350, 640, 10):
        if i == 350 or i == 630 or 390 <= i <= 480 or 500 <= i <= 590:
            create_rect(i, 440, BLACK)
        else:
            create_rect(i, 440, RED_2)
    # 450
    for i in range(350, 640, 10):
        if i == 350 or i == 630 or 370 <= i <= 380 or i == 410 or i == 480 or i == 500 or i == 570 or 600 <= i <= 610:
            create_rect(i, 450, BLACK)
        elif i == 360 or i == 620 or 510 <= i <= 560 or i == 490:
            create_rect(i, 450, RED_2)
        elif 420 <= i <= 470:
            create_rect(i, 450, RED_1)
    # 460
    for i in range(350, 640, 10):
        if i == 360 or i == 620 or 420 <= i <= 480 or 500 <= i <= 560:
            create_rect(i, 460, BLACK)
        elif i == 490:
            create_rect(i, 460, RED_2)
    # 470 480
    for i in range(450, 540, 10):
        if i == 450 or i == 480 or i == 500 or i == 530:
            create_rect(i, 470, BLACK)
            create_rect(i, 480, BLACK)
        elif i == 490:
            create_rect(i, 470, RED_2)
            create_rect(i, 480, RED_2)
        else:
            create_rect(i, 470, FIRE_YELLOW)
            create_rect(i, 480, FIRE_YELLOW)
    # 490
    for i in range(440, 550, 10):
        if i == 440 or i == 540 or i == 490:
            create_rect(i, 490, BLACK)
        else:
            create_rect(i, 490, FIRE_YELLOW)
    # 500
    for i in range(420, 560, 10):
        if i == 420 or i == 430 or i == 550:
            create_rect(i, 500, BLACK)
        elif i == 470 or i == 510:
            create_rect(i, 500, FIRE_RED)
        else:
            create_rect(i, 500, FIRE_YELLOW)
    # 510
    for i in range(410, 570, 10):
        if i == 410 or i == 560:
            create_rect(i, 510, BLACK)
        elif 470 <= i <= 510:
            create_rect(i, 510, FIRE_RED)
        elif i == 450 or i == 460 or i == 520:
            create_rect(i, 510, FIRE_ORANGE)
        else:
            create_rect(i, 510, FIRE_YELLOW)
    # 520
    for i in range(420, 580, 10):
        if i == 420 or i == 430 or i == 570:
            create_rect(i, 520, BLACK)
        elif 480 <= i <= 500:
            create_rect(i, 520, FIRE_RED)
        elif 450 <= i <= 540:
            create_rect(i, 520, FIRE_ORANGE)
        else:
            create_rect(i, 520, FIRE_YELLOW)
    # 530
    for i in range(430, 580, 10):
        if i == 430 or i == 570:
            create_rect(i, 530, BLACK)
        elif i == 490:
            create_rect(i, 530, FIRE_RED)
        elif 450 <= i <= 510:
            create_rect(i, 530, FIRE_ORANGE)
        else:
            create_rect(i, 530, FIRE_YELLOW)
    # 540
    for i in range(420, 580, 10):
        if i == 420 or i == 540 or i == 570:
            create_rect(i, 540, BLACK)
        elif 450 <= i <= 510:
            create_rect(i, 540, FIRE_ORANGE)
        else:
            create_rect(i, 540, FIRE_YELLOW)
    # 550
    for i in range(420, 570, 10):
        if i == 420 or i == 550 or i == 560:
            create_rect(i, 550, BLACK)
        elif 460 <= i <= 470 or 500 <= i <= 520:
            create_rect(i, 550, FIRE_ORANGE)
        else:
            create_rect(i, 550, FIRE_YELLOW)
    # 560
    for i in range(430, 560, 10):
        if i == 430 or i == 550:
            create_rect(i, 560, BLACK)
        else:
            create_rect(i, 560, FIRE_YELLOW)
    # 570
    for i in range(440, 560, 10):
        if i == 440 or i == 470 or i == 510 or i == 550:
            create_rect(i, 570, BLACK)
        else:
            create_rect(i, 570, FIRE_YELLOW)
    # 580
    for i in range(450, 550, 10):
        if i != 470 and i != 510 and i != 530:
            create_rect(i, 580, BLACK)
        if i == 530:
            create_rect(i, 580, FIRE_YELLOW)
    # 590
    create_rect(530, 590, BLACK)


def create_astronaut():
    # 300
    create_rect(750, 300, '#E0E5E3', 5)
    create_rect(755, 300, '#E0E5E3', 5)
    create_rect(760, 300, '#E0E5E3', 5)
    create_rect(765, 300, '#E0E5E3', 5)
    create_rect(770, 300, '#E0E5E3', 5)
    create_rect(775, 300, '#E0E5E3', 5)
    create_rect(780, 300, '#E0E5E3', 5)
    create_rect(785, 300, '#E0E5E3', 5)
    create_rect(790, 300, '#E0E5E3', 5)
    # 305
    create_rect(745, 305, '#E0E5E3', 5)
    create_rect(750, 305, '#E0E5E3', 5)
    create_rect(755, 305, '#E0E5E3', 5)
    create_rect(760, 305, '#E0E5E3', 5)
    create_rect(765, 305, '#E0E5E3', 5)
    create_rect(770, 305, '#E0E5E3', 5)
    create_rect(775, 305, '#E0E5E3', 5)
    create_rect(780, 305, '#FCFFFD', 5)
    create_rect(785, 305, '#FCFFFD', 5)
    create_rect(790, 305, '#FCFFFD', 5)
    create_rect(795, 305, '#D8D5DA', 5)
    # 310
    create_rect(740, 310, '#E0E5E3', 5)
    create_rect(745, 310, '#E0E5E3', 5)
    create_rect(750, 310, '#4B4B64', 5)
    create_rect(755, 310, '#4B4B64', 5)
    create_rect(760, 310, '#3A3F56', 5)
    create_rect(765, 310, '#3A3F56', 5)
    create_rect(770, 310, '#3A3F56', 5)
    create_rect(775, 310, '#3A3F56', 5)
    create_rect(780, 310, '#FCFFFD', 5)
    create_rect(785, 310, '#FCFFFD', 5)
    create_rect(790, 310, '#FCFFFD', 5)
    create_rect(795, 310, '#FCFFFD', 5)
    create_rect(800, 310, '#D6D2DA', 5)
    # 315
    create_rect(740, 315, '#E0E5E3', 5)
    create_rect(745, 315, '#4B4B64', 5)
    create_rect(750, 315, '#4B4B64', 5)
    create_rect(755, 315, '#4B4B64', 5)
    create_rect(760, 315, '#3A3F56', 5)
    create_rect(765, 315, '#3A3F56', 5)
    create_rect(770, 315, '#3A3F56', 5)
    create_rect(775, 315, '#3A3F56', 5)
    create_rect(780, 315, '#3A3F56', 5)
    create_rect(785, 315, '#FCFFFD', 5)
    create_rect(790, 315, '#FCFFFD', 5)
    create_rect(795, 315, '#FCFFFD', 5)
    create_rect(800, 315, '#FCFFFD', 5)
    create_rect(805, 315, '#D7D3DD', 5)
    # 320
    create_rect(735, 320, '#E0E5E3', 5)
    create_rect(740, 320, '#4B4B64', 5)
    create_rect(745, 320, '#4B4B64', 5)
    create_rect(750, 320, '#4B4B64', 5)
    create_rect(755, 320, '#4B4B64', 5)
    create_rect(760, 320, '#3A3F56', 5)
    create_rect(765, 320, '#3A3F56', 5)
    create_rect(770, 320, '#3A3F56', 5)
    create_rect(775, 320, '#3A3F56', 5)
    create_rect(780, 320, '#3A3F56', 5)
    create_rect(785, 320, '#3A3F56', 5)
    create_rect(790, 320, '#FCFFFD', 5)
    create_rect(795, 320, '#FCFFFD', 5)
    create_rect(800, 320, '#FCFFFD', 5)
    create_rect(805, 320, '#D7D3DD', 5)
    create_rect(810, 320, '#6C6C6C', 5)
    # 325
    create_rect(735, 325, '#E0E5E3', 5)
    create_rect(740, 325, '#4B4B64', 5)
    create_rect(745, 325, '#4B4B64', 5)
    create_rect(750, 325, '#4B4B64', 5)
    create_rect(755, 325, '#4B4B64', 5)
    create_rect(760, 325, '#3A3F56', 5)
    create_rect(765, 325, '#3A3F56', 5)
    create_rect(770, 325, '#3A3F56', 5)
    create_rect(775, 325, '#3A3F56', 5)
    create_rect(780, 325, '#3A3F56', 5)
    create_rect(785, 325, '#3A3F56', 5)
    create_rect(790, 325, '#FCFFFD', 5)
    create_rect(795, 325, '#FCFFFD', 5)
    create_rect(800, 325, '#FCFFFD', 5)
    create_rect(805, 325, '#D7D3DD', 5)
    create_rect(810, 325, '#6C6C6C', 5)
    create_rect(815, 325, '#6C6C6C', 5)
    # 330
    create_rect(735, 330, '#E0E5E3', 5)
    create_rect(740, 330, '#4B4B64', 5)
    create_rect(745, 330, '#4B4B64', 5)
    create_rect(750, 330, '#4B4B64', 5)
    create_rect(755, 330, '#4B4B64', 5)
    create_rect(760, 330, '#3A3F56', 5)
    create_rect(765, 330, '#3A3F56', 5)
    create_rect(770, 330, '#3A3F56', 5)
    create_rect(775, 330, '#3A3F56', 5)
    create_rect(780, 330, '#3A3F56', 5)
    create_rect(785, 330, '#3A3F56', 5)
    create_rect(790, 330, '#FCFFFD', 5)
    create_rect(795, 330, '#FCFFFD', 5)
    create_rect(800, 330, '#FCFFFD', 5)
    create_rect(805, 330, '#D7D3DD', 5)
    create_rect(810, 330, '#6C6C6C', 5)
    create_rect(815, 330, '#6C6C6C', 5)
    # 335
    create_rect(735, 335, '#E0E5E3', 5)
    create_rect(740, 335, '#4B4B64', 5)
    create_rect(745, 335, '#4B4B64', 5)
    create_rect(750, 335, '#4B4B64', 5)
    create_rect(755, 335, '#4B4B64', 5)
    create_rect(760, 335, '#3A3F56', 5)
    create_rect(765, 335, '#3A3F56', 5)
    create_rect(770, 335, '#3A3F56', 5)
    create_rect(775, 335, '#3A3F56', 5)
    create_rect(780, 335, '#3A3F56', 5)
    create_rect(785, 335, '#3A3F56', 5)
    create_rect(790, 335, '#FCFFFD', 5)
    create_rect(795, 335, '#FCFFFD', 5)
    create_rect(800, 335, '#FCFFFD', 5)
    create_rect(805, 335, '#D7D3DD', 5)
    create_rect(810, 335, '#6C6C6C', 5)
    create_rect(815, 335, '#6C6C6C', 5)
    # 340
    create_rect(740, 340, '#E0E5E3', 5)
    create_rect(745, 340, '#4B4B64', 5)
    create_rect(750, 340, '#4B4B64', 5)
    create_rect(755, 340, '#4B4B64', 5)
    create_rect(760, 340, '#3A3F56', 5)
    create_rect(765, 340, '#3A3F56', 5)
    create_rect(770, 340, '#3A3F56', 5)
    create_rect(775, 340, '#3A3F56', 5)
    create_rect(780, 340, '#3A3F56', 5)
    create_rect(785, 340, '#FCFFFD', 5)
    create_rect(790, 340, '#FCFFFD', 5)
    create_rect(795, 340, '#FCFFFD', 5)
    create_rect(800, 340, '#DBDADD', 5)
    create_rect(805, 340, '#6C6C6C', 5)
    create_rect(810, 340, '#6C6C6C', 5)
    create_rect(815, 340, '#6C6C6C', 5)
    # 345
    create_rect(745, 345, '#E0E5E3', 5)
    create_rect(750, 345, '#4B4B64', 5)
    create_rect(755, 345, '#4B4B64', 5)
    create_rect(760, 345, '#3A3F56', 5)
    create_rect(765, 345, '#3A3F56', 5)
    create_rect(770, 345, '#3A3F56', 5)
    create_rect(775, 345, '#3A3F56', 5)
    create_rect(780, 345, '#FCFFFD', 5)
    create_rect(785, 345, '#FCFFFD', 5)
    create_rect(790, 345, '#FCFFFD', 5)
    create_rect(795, 345, '#DBDADD', 5)
    create_rect(800, 345, '#6C6C6C', 5)
    create_rect(805, 345, '#88A2A8', 5)
    create_rect(810, 345, '#88A2A8', 5)
    create_rect(815, 345, '#6C6C6C', 5)
    # 350
    create_rect(745, 350, '#E0E5E3', 5)
    create_rect(750, 350, '#E0E5E3', 5)
    create_rect(755, 350, '#E0E5E3', 5)
    create_rect(760, 350, '#D3D0D6', 5)
    create_rect(765, 350, '#D3D0D6', 5)
    create_rect(770, 350, '#D3D0D6', 5)
    create_rect(775, 350, '#D3D0D6', 5)
    create_rect(780, 350, '#FCFFFD', 5)
    create_rect(785, 350, '#FCFFFD', 5)
    create_rect(790, 350, '#FCFFFD', 5)
    create_rect(795, 350, '#6C6C6C', 5)
    create_rect(800, 350, '#6C6C6C', 5)
    create_rect(805, 350, '#6C6C6C', 5)
    create_rect(810, 350, '#88A2A8', 5)
    create_rect(815, 350, '#6C6C6C', 5)
    # 355
    create_rect(750, 355, '#E0E5E3', 5)
    create_rect(755, 355, '#E0E5E3', 5)
    create_rect(760, 355, '#D3D0D6', 5)
    create_rect(765, 355, '#D3D0D6', 5)
    create_rect(770, 355, '#D3D0D6', 5)
    create_rect(775, 355, '#D3D0D6', 5)
    create_rect(780, 355, '#FCFFFD', 5)
    create_rect(785, 355, '#FCFFFD', 5)
    create_rect(795, 355, '#6C6C6C', 5)
    create_rect(800, 355, '#6C6C6C', 5)
    create_rect(805, 355, '#6C6C6C', 5)
    create_rect(810, 355, '#6C6C6C', 5)
    create_rect(815, 355, '#88A2A8', 5)
    # 360
    create_rect(750, 360, '#000', 5)
    create_rect(755, 360, '#000', 5)
    create_rect(760, 360, '#000', 5)
    create_rect(765, 360, '#000', 5)
    create_rect(770, 360, '#000', 5)
    create_rect(775, 360, '#000', 5)
    create_rect(780, 360, '#000', 5)
    create_rect(790, 360, '#6C6C6C', 5)
    create_rect(795, 360, '#6C6C6C', 5)
    create_rect(800, 360, '#6C6C6C', 5)
    create_rect(805, 360, '#6C6C6C', 5)
    create_rect(810, 360, '#6C6C6C', 5)
    create_rect(815, 360, '#6C6C6C', 5)
    create_rect(820, 360, '#88A2A8', 5)
    # 365
    create_rect(740, 365, '#FCFFFD', 5)
    create_rect(745, 365, '#FCFFFD', 5)
    create_rect(750, 365, '#FCFFFD', 5)
    create_rect(755, 365, '#FCFFFD', 5)
    create_rect(760, 365, '#FCFFFD', 5)
    create_rect(765, 365, '#A5A7A9', 5)
    create_rect(770, 365, '#A5A7A9', 5)
    create_rect(775, 365, '#A5A7A9', 5)
    create_rect(780, 365, '#A5A7A9', 5)
    create_rect(785, 365, '#E0DCE4', 5)
    create_rect(790, 365, '#E0DCE4', 5)
    create_rect(795, 365, '#E0DCE4', 5)
    create_rect(800, 365, '#6C6C6C', 5)
    create_rect(805, 365, '#6C6C6C', 5)
    create_rect(810, 365, '#6C6C6C', 5)
    create_rect(825, 365, '#88A2A8', 5)
    # 370
    create_rect(735, 370, '#FCFFFD', 5)
    create_rect(740, 370, '#FCFFFD', 5)
    create_rect(745, 370, '#FCFFFD', 5)
    create_rect(750, 370, '#A77644', 5)
    create_rect(755, 370, '#FCFFFD', 5)
    create_rect(760, 370, '#FCFFFD', 5)
    create_rect(765, 370, '#A5A7A9', 5)
    create_rect(770, 370, '#566B8F', 5)
    create_rect(775, 370, '#6F91BA', 5)
    create_rect(780, 370, '#A5A7A9', 5)
    create_rect(785, 370, '#E0DCE4', 5)
    create_rect(790, 370, '#E0DCE4', 5)
    create_rect(795, 370, '#E0DCE4', 5)
    create_rect(800, 370, '#E0DCE4', 5)
    create_rect(805, 370, '#6C6C6C', 5)
    create_rect(810, 370, '#6C6C6C', 5)
    create_rect(820, 370, '#88A2A8', 5)
    # 375
    create_rect(720, 375, '#FCFFFD', 5)
    create_rect(725, 375, '#000', 5)
    create_rect(730, 375, '#FCFFFD', 5)
    create_rect(735, 375, '#FCFFFD', 5)
    create_rect(740, 375, '#D5D5D3', 5)
    create_rect(745, 375, '#FCFFFD', 5)
    create_rect(750, 375, '#E3AD60', 5)
    create_rect(755, 375, '#FCFFFD', 5)
    create_rect(760, 375, '#FCFFFD', 5)
    create_rect(765, 375, '#A5A7A9', 5)
    create_rect(770, 375, '#566B8F', 5)
    create_rect(775, 375, '#6F91BA', 5)
    create_rect(780, 375, '#A5A7A9', 5)
    create_rect(785, 375, '#E0DCE4', 5)
    create_rect(790, 375, '#858887', 5)
    create_rect(795, 375, '#E0DCE4', 5)
    create_rect(800, 375, '#E0DCE4', 5)
    create_rect(805, 375, '#E0DCE4', 5)
    create_rect(810, 375, '#6C6C6C', 5)
    create_rect(815, 375, '#88A2A8', 5)
    # 380
    create_rect(715, 380, '#FCFFFD', 5)
    create_rect(720, 380, '#FCFFFD', 5)
    create_rect(725, 380, '#000', 5)
    create_rect(730, 380, '#FCFFFD', 5)
    create_rect(735, 380, '#FCFFFD', 5)
    create_rect(740, 380, '#D5D5D3', 5)
    create_rect(745, 380, '#FCFFFD', 5)
    create_rect(750, 380, '#ECD77C', 5)
    create_rect(755, 380, '#FCFFFD', 5)
    create_rect(760, 380, '#FCFFFD', 5)
    create_rect(765, 380, '#A5A7A9', 5)
    create_rect(770, 380, '#A5A7A9', 5)
    create_rect(775, 380, '#A5A7A9', 5)
    create_rect(780, 380, '#A5A7A9', 5)
    create_rect(785, 380, '#E0DCE4', 5)
    create_rect(790, 380, '#858887', 5)
    create_rect(795, 380, '#858887', 5)
    create_rect(800, 380, '#E0DCE4', 5)
    create_rect(805, 380, '#E0DCE4', 5)
    create_rect(810, 380, '#E0DCE4', 5)
    # 385
    create_rect(715, 385, '#FCFFFD', 5)
    create_rect(720, 385, '#FCFFFD', 5)
    create_rect(725, 385, '#FCFFFD', 5)
    create_rect(730, 385, '#000', 5)
    create_rect(735, 385, '#D5D5D3', 5)
    create_rect(740, 385, '#D5D5D3', 5)
    create_rect(745, 385, '#FCFFFD', 5)
    create_rect(750, 385, '#FCFFFD', 5)
    create_rect(755, 385, '#FCFFFD', 5)
    create_rect(760, 385, '#FCFFFD', 5)
    create_rect(765, 385, '#A5A7A9', 5)
    create_rect(770, 385, '#5CB587', 5)
    create_rect(775, 385, '#5CB587', 5)
    create_rect(780, 385, '#A5A7A9', 5)
    create_rect(785, 385, '#E0DCE4', 5)
    create_rect(790, 385, '#858887', 5)
    create_rect(795, 385, '#000', 5)
    create_rect(800, 385, '#E0DCE4', 5)
    create_rect(805, 385, '#E0DCE4', 5)
    create_rect(810, 385, '#E0DCE4', 5)
    # 390
    create_rect(745, 390, '#FCFFFD', 5)
    create_rect(750, 390, '#FCFFFD', 5)
    create_rect(755, 390, '#FCFFFD', 5)
    create_rect(760, 390, '#FCFFFD', 5)
    create_rect(765, 390, '#A5A7A9', 5)
    create_rect(770, 390, '#5CB587', 5)
    create_rect(775, 390, '#5CB587', 5)
    create_rect(780, 390, '#A5A7A9', 5)
    create_rect(785, 390, '#E0DCE4', 5)
    create_rect(790, 390, '#FFFFFF', 5)
    create_rect(795, 390, '#FFFFFF', 5)
    create_rect(800, 390, '#000', 5)
    create_rect(805, 390, '#E0DCE4', 5)
    create_rect(810, 390, '#6C6C6C', 5)
    # 395
    create_rect(745, 395, '#5C7DB5', 5)
    create_rect(750, 395, '#5C7DB5', 5)
    create_rect(755, 395, '#5C7DB5', 5)
    create_rect(760, 395, '#5C7DB5', 5)
    create_rect(765, 395, '#5C7DB5', 5)
    create_rect(770, 395, '#5C7DB5', 5)
    create_rect(775, 395, '#5C7DB5', 5)
    create_rect(780, 395, '#5C7DB5', 5)
    create_rect(785, 395, '#5C7DB5', 5)
    create_rect(790, 395, '#FFFFFF', 5)
    create_rect(795, 395, '#FFFFFF', 5)
    create_rect(800, 395, '#FFFFFF', 5)
    create_rect(805, 395, '#000', 5)
    create_rect(810, 395, '#6C6C6C', 5)
    # 400
    create_rect(740, 400, '#D0CEDB', 5)
    create_rect(745, 400, '#EEEEEE', 5)
    create_rect(750, 400, '#EEEEEE', 5)
    create_rect(755, 400, '#EEEEEE', 5)
    create_rect(760, 400, '#D3D3D3', 5)
    create_rect(765, 400, '#D3D3D3', 5)
    create_rect(770, 400, '#D3D3D3', 5)
    create_rect(775, 400, '#D7D7D7', 5)
    create_rect(780, 400, '#D7D7D7', 5)
    create_rect(785, 400, '#D7D7D7', 5)
    for i in range(790, 810, 5):
        create_rect(i, 400, '#6C6C6C', 5)
    # 405
    create_rect(735, 405, '#D0CEDB', 5)
    create_rect(740, 405, '#EEEEEE', 5)
    create_rect(745, 405, '#EEEEEE', 5)
    create_rect(750, 405, '#EEEEEE', 5)
    create_rect(755, 405, '#979797', 5)
    create_rect(760, 405, '#D3D3D3', 5)
    create_rect(765, 405, '#D3D3D3', 5)
    create_rect(770, 405, '#D3D3D3', 5)
    create_rect(775, 405, '#AFAFAF', 5)
    create_rect(780, 405, '#AFAFAF', 5)
    for i in range(785, 810, 5):
        create_rect(i, 405, '#6C6C6C', 5)
    # 410
    create_rect(730, 410, '#D0CEDB', 5)
    create_rect(735, 410, '#EEEEEE', 5)
    create_rect(740, 410, '#EEEEEE', 5)
    create_rect(745, 410, '#EEEEEE', 5)
    create_rect(750, 410, '#979797', 5)
    create_rect(755, 410, '#D3D3D3', 5)
    create_rect(760, 410, '#D3D3D3', 5)
    create_rect(765, 410, '#D3D3D3', 5)
    create_rect(770, 410, '#D3D3D3', 5)
    create_rect(775, 410, '#AFAFAF', 5)
    for i in range(780, 805, 5):
        create_rect(i, 410, '#6C6C6C', 5)
    # 415
    create_rect(730, 415, '#000', 5)
    create_rect(735, 415, '#000', 5)
    create_rect(740, 415, '#000', 5)
    create_rect(745, 415, '#979797', 5)
    create_rect(750, 415, '#000', 5)
    create_rect(755, 415, '#000', 5)
    create_rect(760, 415, '#000', 5)
    create_rect(765, 415, '#000', 5)
    create_rect(770, 415, '#D3D3D3', 5)
    create_rect(775, 415, '#AFAFAF', 5)
    for i in range(780, 800, 5):
        create_rect(i, 415, '#6C6C6C', 5)
    # 420
    create_rect(725, 420, '#D0CEDB', 5)
    create_rect(730, 420, '#EEEEEE', 5)
    create_rect(735, 420, '#EEEEEE', 5)
    create_rect(740, 420, '#979797', 5)
    create_rect(745, 420, '#979797', 5)
    create_rect(750, 420, '#D3D3D3', 5)
    create_rect(755, 420, '#D3D3D3', 5)
    create_rect(760, 420, '#D3D3D3', 5)
    create_rect(765, 420, '#000', 5)
    create_rect(770, 420, '#000', 5)
    for i in range(775, 800, 5):
        create_rect(i, 420, '#6C6C6C', 5)
    # 425
    create_rect(725, 425, '#D0CEDB', 5)
    create_rect(730, 425, '#EEEEEE', 5)
    create_rect(735, 425, '#EEEEEE', 5)
    create_rect(740, 425, '#979797', 5)
    create_rect(745, 425, '#979797', 5)
    create_rect(750, 425, '#D3D3D3', 5)
    create_rect(755, 425, '#D3D3D3', 5)
    create_rect(760, 425, '#D3D3D3', 5)
    create_rect(765, 425, '#AFAFAF', 5)
    for i in range(770, 790, 5):
        create_rect(i, 425, '#6C6C6C', 5)
    # 430
    create_rect(730, 430, '#D0CEDB', 5)
    create_rect(735, 430, '#EEEEEE', 5)
    create_rect(740, 430, '#EEEEEE', 5)
    create_rect(745, 430, '#979797', 5)
    create_rect(755, 430, '#D3D3D3', 5)
    create_rect(760, 430, '#D3D3D3', 5)
    create_rect(765, 430, '#D3D3D3', 5)
    create_rect(770, 430, '#AFAFAF', 5)
    # 435
    create_rect(730, 435, '#D0CEDB', 5)
    create_rect(735, 435, '#79797B', 5)
    create_rect(740, 435, '#79797B', 5)
    create_rect(755, 435, '#79797B', 5)
    create_rect(760, 435, '#79797B', 5)
    create_rect(765, 435, '#79797B', 5)
    create_rect(770, 435, '#AFAFAF', 5)
    # 440
    create_rect(725, 440, '#79797B', 5)
    create_rect(730, 440, '#A8A6A7', 5)
    create_rect(735, 440, '#A8A6A7', 5)
    create_rect(740, 440, '#A8A6A7', 5)
    create_rect(755, 440, '#A8A6A7', 5)
    create_rect(760, 440, '#A8A6A7', 5)
    create_rect(765, 440, '#A8A6A7', 5)
    create_rect(770, 440, '#79797B', 5)
    # 445
    create_rect(720, 445, '#545454', 5)
    create_rect(725, 445, '#545454', 5)
    create_rect(730, 445, '#545454', 5)
    create_rect(735, 445, '#545454', 5)
    create_rect(740, 445, '#545454', 5)
    create_rect(750, 445, '#333333', 5)
    create_rect(755, 445, '#333333', 5)
    create_rect(760, 445, '#333333', 5)
    create_rect(765, 445, '#333333', 5)
    create_rect(770, 445, '#333333', 5)


def create_green_planet():
    # 100
    create_rect(780, 100, '#659138', 5)
    create_rect(785, 100, '#659138', 5)
    create_rect(790, 100, '#659138', 5)
    create_rect(795, 100, '#659138', 5)
    # 105
    create_rect(775, 105, '#659138', 5)
    create_rect(780, 105, '#EDEDAC', 5)
    create_rect(785, 105, '#D9DB98', 5)
    create_rect(790, 105, '#D5DB15', 5)
    create_rect(795, 105, '#A99A59', 5)
    create_rect(800, 105, '#659138', 5)
    # 110
    create_rect(770, 110, '#659138', 5)
    create_rect(775, 110, '#EDEDAC', 5)
    create_rect(780, 110, '#D5DB15', 5)
    create_rect(785, 110, '#E2E39F', 5)
    create_rect(790, 110, '#94BE64', 5)
    create_rect(795, 110, '#C6C649', 5)
    create_rect(800, 110, '#467116', 5)
    create_rect(805, 110, '#659138', 5)
    # 115
    create_rect(770, 115, '#659138', 5)
    create_rect(775, 115, '#D9DB98', 5)
    create_rect(780, 115, '#D5DB15', 5)
    create_rect(785, 115, '#D8DD3C', 5)
    create_rect(790, 115, '#A5C67B', 5)
    create_rect(795, 115, '#D5DB15', 5)
    create_rect(800, 115, '#325111', 5)
    create_rect(805, 115, '#659138', 5)
    # 120
    create_rect(770, 120, '#659138', 5)
    create_rect(775, 120, '#A99A59', 5)
    create_rect(780, 120, '#D5DB15', 5)
    create_rect(785, 120, '#D5DB15', 5)
    create_rect(790, 120, '#967D21', 5)
    create_rect(795, 120, '#67A824', 5)
    create_rect(800, 120, '#467116', 5)
    create_rect(805, 120, '#659138', 5)
    # 125
    create_rect(770, 125, '#659138', 5)
    create_rect(775, 125, '#B19326', 5)
    create_rect(780, 125, '#A99A59', 5)
    create_rect(785, 125, '#D8DD3C', 5)
    create_rect(790, 125, '#67A824', 5)
    create_rect(795, 125, '#467116', 5)
    create_rect(800, 125, '#325111', 5)
    create_rect(805, 125, '#7FA257', 5)
    # 130
    create_rect(775, 130, '#659138', 5)
    create_rect(780, 130, '#A4B687', 5)
    create_rect(785, 130, '#566F38', 5)
    create_rect(790, 130, '#467116', 5)
    create_rect(795, 130, '#467116', 5)
    create_rect(800, 130, '#659138', 5)
    # 135
    create_rect(780, 135, '#7FA257', 5)
    create_rect(785, 135, '#A4BB85', 5)
    create_rect(790, 135, '#7FA257', 5)
    create_rect(795, 135, '#93B071', 5)


def create_blue_planet():
    # outline
    for i in range(100, 130, 5):
        create_rect(i, 60, PLANET_1_OUTLINE, 5)
        create_rect(i, 145, PLANET_1_OUTLINE, 5)
    for i in range(90, 120, 5):
        create_rect(70, i, PLANET_1_OUTLINE, 5)
        create_rect(155, i, PLANET_1_OUTLINE, 5)
    # 65
    create_rect(90, 65, PLANET_1_OUTLINE, 5)
    create_rect(95, 65, PLANET_1_OUTLINE, 5)
    create_rect(100, 65, '#A6DEF0', 5)
    create_rect(105, 65, '#A6DEF0', 5)
    create_rect(110, 65, '#1383F2', 5)
    create_rect(115, 65, '#A6DEF0', 5)
    create_rect(120, 65, '#3483CF', 5)
    create_rect(125, 65, '#3483CF', 5)
    create_rect(130, 65, PLANET_1_OUTLINE, 5)
    create_rect(135, 65, PLANET_1_OUTLINE, 5)
    # 70
    create_rect(85, 70, PLANET_1_OUTLINE, 5)
    create_rect(90, 70, '#A6DEF0', 5)
    create_rect(95, 70, '#A6DEF0', 5)
    create_rect(100, 70, '#27659F', 5)
    create_rect(105, 70, '#27659F', 5)
    create_rect(110, 70, '#27659F', 5)
    create_rect(115, 70, '#3483CF', 5)
    create_rect(120, 70, '#9228BE', 5)
    create_rect(125, 70, '#3483CF', 5)
    create_rect(130, 70, '#3483CF', 5)
    create_rect(135, 70, '#3483CF', 5)
    create_rect(140, 70, PLANET_1_OUTLINE, 5)
    # 75
    create_rect(80, 75, PLANET_1_OUTLINE, 5)
    create_rect(85, 75, '#A6DEF0', 5)
    create_rect(90, 75, '#A6DEF0', 5)
    create_rect(95, 75, '#27659F', 5)
    create_rect(100, 75, '#A6DEF0', 5)
    create_rect(105, 75, '#1383F2', 5)
    create_rect(110, 75, '#9228BE', 5)
    create_rect(115, 75, '#9228BE', 5)
    create_rect(120, 75, '#9228BE', 5)
    create_rect(125, 75, '#9228BE', 5)
    create_rect(130, 75, '#3483CF', 5)
    create_rect(135, 75, '#9228BE', 5)
    create_rect(140, 75, '#3483CF', 5)
    create_rect(145, 75, PLANET_1_OUTLINE, 5)
    # 80
    create_rect(75, 80, PLANET_1_OUTLINE, 5)
    create_rect(80, 80, '#A6DEF0', 5)
    create_rect(85, 80, '#A6DEF0', 5)
    create_rect(90, 80, '#27659F', 5)
    create_rect(95, 80, '#1383F2', 5)
    create_rect(100, 80, '#5A19D6', 5)
    create_rect(105, 80, '#2372BE', 5)
    create_rect(110, 80, '#27659F', 5)
    create_rect(115, 80, '#9228BE', 5)
    create_rect(120, 80, '#9228BE', 5)
    create_rect(125, 80, '#9228BE', 5)
    create_rect(130, 80, '#9228BE', 5)
    create_rect(135, 80, '#1E3B9F', 5)
    create_rect(140, 80, '#0E5DA8', 5)
    create_rect(145, 80, '#3483CF', 5)
    create_rect(150, 80, PLANET_1_OUTLINE, 5)
    # 85
    create_rect(75, 85, PLANET_1_OUTLINE, 5)
    create_rect(80, 85, '#A6DEF0', 5)
    create_rect(85, 85, '#1383F2', 5)
    create_rect(90, 85, '#27659F', 5)
    create_rect(95, 85, '#5A19D6', 5)
    create_rect(100, 85, '#5A19D6', 5)
    create_rect(105, 85, '#27659F', 5)
    create_rect(110, 85, '#BD6CE3', 5)
    create_rect(115, 85, '#BD6CE3', 5)
    create_rect(120, 85, '#9228BE', 5)
    create_rect(125, 85, '#9228BE', 5)
    create_rect(130, 85, '#9228BE', 5)
    create_rect(135, 85, '#1E3B9F', 5)
    create_rect(140, 85, '#0E5DA8', 5)
    create_rect(145, 85, '#3483CF', 5)
    create_rect(150, 85, PLANET_1_OUTLINE, 5)
    # 90
    create_rect(75, 90, '#A6DEF0', 5)
    create_rect(80, 90, '#1383F2', 5)
    create_rect(85, 90, '#27659F', 5)
    create_rect(90, 90, '#5A19D6', 5)
    create_rect(95, 90, '#5A19D6', 5)
    create_rect(100, 90, '#1383F2', 5)
    create_rect(105, 90, '#1383F2', 5)
    create_rect(110, 90, '#BD6CE3', 5)
    create_rect(115, 90, '#1383F2', 5)
    create_rect(120, 90, '#BD6CE3', 5)
    create_rect(125, 90, '#14BBDE', 5)
    create_rect(130, 90, '#9228BE', 5)
    create_rect(135, 90, '#9228BE', 5)
    create_rect(140, 90, '#1E3B9F', 5)
    create_rect(145, 90, '#1B3489', 5)
    create_rect(150, 90, '#0E1E49', 5)
    # 95
    create_rect(75, 95, '#A6DEF0', 5)
    create_rect(80, 95, '#2372BE', 5)
    create_rect(85, 95, '#A6DEF0', 5)
    create_rect(90, 95, '#5A19D6', 5)
    create_rect(95, 95, '#5A19D6', 5)
    create_rect(100, 95, '#1383F2', 5)
    create_rect(105, 95, '#BD6CE3', 5)
    create_rect(110, 95, '#1383F2', 5)
    create_rect(115, 95, '#14BBDE', 5)
    create_rect(120, 95, '#1383F2', 5)
    create_rect(125, 95, '#9228BE', 5)
    create_rect(130, 95, '#14BBDE', 5)
    create_rect(135, 95, '#14BBDE', 5)
    create_rect(140, 95, '#1E3B9F', 5)
    create_rect(145, 95, '#1B3489', 5)
    create_rect(150, 95, '#0E1E49', 5)
    # 100
    create_rect(75, 100, '#4A9CEB', 5)
    create_rect(80, 100, '#2372BE', 5)
    create_rect(85, 100, '#2372BE', 5)
    create_rect(90, 100, '#5A19D6', 5)
    create_rect(95, 100, '#5A19D6', 5)
    create_rect(100, 100, '#5A19D6', 5)
    create_rect(105, 100, '#14BBDE', 5)
    create_rect(110, 100, '#9A4EBE', 5)
    create_rect(115, 100, '#1383F2', 5)
    create_rect(120, 100, '#14BBDE', 5)
    create_rect(125, 100, '#9228BE', 5)
    create_rect(130, 100, '#14BBDE', 5)
    create_rect(135, 100, '#9228BE', 5)
    create_rect(140, 100, '#1E3B9F', 5)
    create_rect(145, 100, '#162E7E', 5)
    create_rect(150, 100, '#162E7E', 5)
    # 105
    create_rect(75, 105, '#1B84EB', 5)
    create_rect(80, 105, '#1B84EB', 5)
    create_rect(85, 105, '#5A19D6', 5)
    create_rect(90, 105, '#5A19D6', 5)
    create_rect(95, 105, '#5A19D6', 5)
    create_rect(100, 105, '#1383F2', 5)
    create_rect(105, 105, '#14BBDE', 5)
    create_rect(110, 105, '#9A4EBE', 5)
    create_rect(115, 105, '#9A4EBE', 5)
    create_rect(120, 105, '#1178DB', 5)
    create_rect(125, 105, '#14BBDE', 5)
    create_rect(130, 105, '#14BBDE', 5)
    create_rect(135, 105, '#9A4EBE', 5)
    create_rect(140, 105, '#1E3B9F', 5)
    create_rect(145, 105, '#162E7E', 5)
    create_rect(150, 105, '#0E1E49', 5)
    # 110
    create_rect(75, 110, '#1B84EB', 5)
    create_rect(80, 110, '#2372BE', 5)
    create_rect(85, 110, '#5A19D6', 5)
    create_rect(90, 110, '#1C65DB', 5)
    create_rect(95, 110, '#5A19D6', 5)
    create_rect(100, 110, '#5A19D6', 5)
    create_rect(105, 110, '#14BBDE', 5)
    create_rect(110, 110, '#1383F2', 5)
    create_rect(115, 110, '#14BBDE', 5)
    create_rect(120, 110, '#14BBDE', 5)
    create_rect(125, 110, '#162E7E', 5)
    create_rect(130, 110, '#14BBDE', 5)
    create_rect(135, 110, '#0E5DA8', 5)
    create_rect(140, 110, '#1E3B9F', 5)
    create_rect(145, 110, '#162E7E', 5)
    create_rect(150, 110, '#1337B9', 5)
    # 115
    create_rect(75, 115, '#1B84EB', 5)
    create_rect(80, 115, '#2372BE', 5)
    create_rect(85, 115, '#27659F', 5)
    create_rect(90, 115, '#5B28BE', 5)
    create_rect(95, 115, '#1C65DB', 5)
    create_rect(100, 115, '#5A19D6', 5)
    create_rect(105, 115, '#1383F2', 5)
    create_rect(110, 115, '#14BBDE', 5)
    create_rect(115, 115, '#14BBDE', 5)
    create_rect(120, 115, '#14BBDE', 5)
    create_rect(125, 115, '#9A4EBE', 5)
    create_rect(130, 115, '#1E3B9F', 5)
    create_rect(135, 115, '#1E3B9F', 5)
    create_rect(140, 115, '#0E1E49', 5)
    create_rect(145, 115, '#162E7E', 5)
    create_rect(150, 115, '#1A2A5D', 5)
    # 120
    create_rect(75, 120, PLANET_1_OUTLINE, 5)
    create_rect(80, 120, '#3B5DD4', 5)
    create_rect(85, 120, '#2372BE', 5)
    create_rect(90, 120, '#27659F', 5)
    create_rect(95, 120, '#5B28BE', 5)
    create_rect(100, 120, '#1383F2', 5)
    create_rect(105, 120, '#5B28BE', 5)
    create_rect(110, 120, '#5B28BE', 5)
    create_rect(115, 120, '#14BBDE', 5)
    create_rect(120, 120, '#5B28BE', 5)
    create_rect(125, 120, '#1E3B9F', 5)
    create_rect(130, 120, '#0E1E49', 5)
    create_rect(135, 120, '#1E3B9F', 5)
    create_rect(140, 120, '#162E7E', 5)
    create_rect(145, 120, '#0E1E49', 5)
    create_rect(150, 120, PLANET_1_OUTLINE, 5)
    # 125
    create_rect(75, 125, PLANET_1_OUTLINE, 5)
    create_rect(80, 125, '#1539B9', 5)
    create_rect(85, 125, '#3B5DD4', 5)
    create_rect(90, 125, '#2372BE', 5)
    create_rect(95, 125, '#1383F2', 5)
    create_rect(100, 125, '#5B28BE', 5)
    create_rect(105, 125, '#5B28BE', 5)
    create_rect(110, 125, '#162E7E', 5)
    create_rect(115, 125, '#1E3B9F', 5)
    create_rect(120, 125, '#1E3B9F', 5)
    create_rect(125, 125, '#1A2A5D', 5)
    create_rect(130, 125, '#1E3B9F', 5)
    create_rect(135, 125, '#0E1E49', 5)
    create_rect(140, 125, '#162E7E', 5)
    create_rect(145, 125, '#1A2A5D', 5)
    create_rect(150, 125, PLANET_1_OUTLINE, 5)
    # 130
    create_rect(80, 130, PLANET_1_OUTLINE, 5)
    create_rect(85, 130, '#1539B9', 5)
    create_rect(90, 130, '#3B5DD4', 5)
    create_rect(95, 130, '#2372BE', 5)
    create_rect(100, 130, '#5B28BE', 5)
    create_rect(105, 130, '#5B28BE', 5)
    create_rect(110, 130, '#5B28BE', 5)
    create_rect(115, 130, '#1E3B9F', 5)
    create_rect(120, 130, '#1A2A5D', 5)
    create_rect(125, 130, '#1E3B9F', 5)
    create_rect(130, 130, '#162E7E', 5)
    create_rect(135, 130, '#162E7E', 5)
    create_rect(140, 130, '#1337B9', 5)
    create_rect(145, 130, PLANET_1_OUTLINE, 5)
    # 135
    create_rect(85, 135, PLANET_1_OUTLINE, 5)
    create_rect(90, 135, '#1539B9', 5)
    create_rect(95, 135, '#1539B9', 5)
    create_rect(100, 135, '#1131A1', 5)
    create_rect(105, 135, '#1E3B9F', 5)
    create_rect(110, 135, '#162E7E', 5)
    create_rect(115, 135, '#1133AA', 5)
    create_rect(120, 135, '#1133AA', 5)
    create_rect(125, 135, '#0E1E49', 5)
    create_rect(130, 135, '#1337B9', 5)
    create_rect(135, 135, '#0E1E49', 5)
    create_rect(140, 135, PLANET_1_OUTLINE, 5)
    # 140
    create_rect(90, 140, PLANET_1_OUTLINE, 5)
    create_rect(95, 140, PLANET_1_OUTLINE, 5)
    create_rect(100, 140, '#162E7E', 5)
    create_rect(105, 140, '#162E7E', 5)
    create_rect(110, 140, '#1131A1', 5)
    create_rect(115, 140, '#1131A1', 5)
    create_rect(120, 140, '#1A2A5D', 5)
    create_rect(125, 140, '#1133AA', 5)
    create_rect(130, 140, PLANET_1_OUTLINE, 5)
    create_rect(135, 140, PLANET_1_OUTLINE, 5)


def create_red_planet():
    # outline
    for i in range(170, 200, 5):
        create_rect(i, 260, PLANET_2_OUTLINE, 5)
        create_rect(i, 260 + 65, PLANET_2_OUTLINE, 5)
    for i in range(280, 310, 5):
        create_rect(150, i, PLANET_2_OUTLINE, 5)
        create_rect(215, i, PLANET_2_OUTLINE, 5)
    # 265
    create_rect(165, 265, PLANET_2_OUTLINE, 5)
    create_rect(160, 265, PLANET_2_OUTLINE, 5)
    create_rect(170, 265, PLANET_2_LIGHT, 5)
    create_rect(175, 265, PLANET_2_LIGHT, 5)
    create_rect(180, 265, PLANET_2_LIGHT, 5)
    create_rect(185, 265, PLANET_2_MID, 5)
    create_rect(190, 265, PLANET_2_MID, 5)
    create_rect(195, 265, PLANET_2_MID, 5)
    create_rect(200, 265, PLANET_2_OUTLINE, 5)
    create_rect(205, 265, PLANET_2_OUTLINE, 5)
    # 270
    create_rect(155, 270, PLANET_2_OUTLINE, 5)
    create_rect(160, 270, PLANET_2_LIGHT_1, 5)
    create_rect(165, 270, PLANET_2_LIGHT, 5)
    create_rect(170, 270, PLANET_2_LIGHT, 5)
    create_rect(175, 270, PLANET_2_MID_1, 5)
    create_rect(180, 270, PLANET_2_MID_2, 5)
    create_rect(185, 270, PLANET_2_MID_2, 5)
    create_rect(190, 270, PLANET_2_MID_2, 5)
    create_rect(195, 270, PLANET_2_MID_3, 5)
    create_rect(200, 270, PLANET_2_MID_3, 5)
    create_rect(205, 270, PLANET_2_MID_3, 5)
    create_rect(210, 270, PLANET_2_OUTLINE, 5)
    # 275
    create_rect(155, 275, PLANET_2_OUTLINE, 5)
    create_rect(160, 275, PLANET_2_LIGHT, 5)
    create_rect(165, 275, PLANET_2_LIGHT, 5)
    create_rect(170, 275, PLANET_2_MID_1, 5)
    create_rect(175, 275, PLANET_2_MID, 5)
    create_rect(180, 275, PLANET_2_DARK, 5)
    create_rect(185, 275, PLANET_2_DARK, 5)
    create_rect(190, 275, PLANET_2_MID_4, 5)
    create_rect(195, 275, PLANET_2_ORANGE, 5)
    create_rect(200, 275, PLANET_2_MID_3, 5)
    create_rect(205, 275, PLANET_2_DARK_1, 5)
    create_rect(210, 275, PLANET_2_OUTLINE, 5)
    # 280
    create_rect(155, 280, PLANET_2_LIGHT, 5)
    create_rect(160, 280, PLANET_2_LIGHT, 5)
    create_rect(165, 280, PLANET_2_MID_1, 5)
    create_rect(170, 280, PLANET_2_MID, 5)
    create_rect(175, 280, PLANET_2_MUD, 5)
    create_rect(180, 280, PLANET_2_DARK, 5)
    create_rect(185, 280, PLANET_2_GOLD, 5)
    create_rect(190, 280, PLANET_2_MID_4, 5)
    create_rect(195, 280, PLANET_2_MID_4, 5)
    create_rect(200, 280, PLANET_2_MID_3, 5)
    create_rect(205, 280, PLANET_2_DARK, 5)
    create_rect(210, 280, PLANET_2_DARK_1, 5)
    # 285
    create_rect(155, 285, PLANET_2_LIGHT, 5)
    create_rect(160, 285, PLANET_2_MID_1, 5)
    create_rect(165, 285, PLANET_2_MID, 5)
    create_rect(170, 285, PLANET_2_MUD, 5)
    create_rect(175, 285, PLANET_2_MID_4, 5)
    create_rect(180, 285, PLANET_2_GOLD, 5)
    create_rect(185, 285, PLANET_2_GOLD, 5)
    create_rect(190, 285, PLANET_2_GOLD, 5)
    create_rect(195, 285, PLANET_2_MID_4, 5)
    create_rect(200, 285, PLANET_2_MID_3, 5)
    create_rect(205, 285, PLANET_2_DARK, 5)
    create_rect(210, 285, PLANET_2_MAROON, 5)
    # 290
    create_rect(155, 290, PLANET_2_SALMON, 5)
    create_rect(160, 290, PLANET_2_MID_2, 5)
    create_rect(165, 290, PLANET_2_MID, 5)
    create_rect(170, 290, PLANET_2_MUD, 5)
    create_rect(175, 290, PLANET_2_MID_4, 5)
    create_rect(180, 290, PLANET_2_DARK, 5)
    create_rect(185, 290, PLANET_2_GOLD, 5)
    create_rect(190, 290, PLANET_2_MUD, 5)
    create_rect(195, 290, PLANET_2_MID_4, 5)
    create_rect(200, 290, PLANET_2_DARK_1, 5)
    create_rect(205, 290, PLANET_2_DARK_1, 5)
    create_rect(210, 290, PLANET_2_MID_4, 5)
    # 295
    create_rect(155, 295, PLANET_2_MID_2, 5)
    create_rect(160, 295, PLANET_2_MID_2, 5)
    create_rect(165, 295, PLANET_2_MID_2, 5)
    create_rect(170, 295, PLANET_2_MUD, 5)
    create_rect(175, 295, PLANET_2_MID_2, 5)
    create_rect(180, 295, PLANET_2_MID_4, 5)
    create_rect(185, 295, PLANET_2_LIGHT_2, 5)
    create_rect(190, 295, PLANET_2_LIGHT_2, 5)
    create_rect(195, 295, PLANET_2_MUD, 5)
    create_rect(200, 295, PLANET_2_DARK, 5)
    create_rect(205, 295, PLANET_2_MAROON, 5)
    create_rect(210, 295, PLANET_2_MAROON, 5)
    # 300
    create_rect(155, 300, PLANET_2_SALMON, 5)
    create_rect(160, 300, PLANET_2_MID_2, 5)
    create_rect(165, 300, PLANET_2_MID_2, 5)
    create_rect(170, 300, PLANET_2_MUD, 5)
    create_rect(175, 300, PLANET_2_MUD, 5)
    create_rect(180, 300, PLANET_2_MUD, 5)
    create_rect(185, 300, PLANET_2_MUD, 5)
    create_rect(190, 300, PLANET_2_MUD, 5)
    create_rect(195, 300, PLANET_2_MID, 5)
    create_rect(200, 300, PLANET_2_MID_4, 5)
    create_rect(205, 300, PLANET_2_MID, 5)
    create_rect(210, 300, PLANET_2_DARK_1, 5)
    # 305
    create_rect(155, 305, PLANET_2_MAROON, 5)
    create_rect(160, 305, PLANET_2_DARK, 5)
    create_rect(165, 305, PLANET_2_MID_2, 5)
    create_rect(170, 305, PLANET_2_MID_2, 5)
    create_rect(175, 305, PLANET_2_MUD, 5)
    create_rect(180, 305, PLANET_2_MUD, 5)
    create_rect(185, 305, PLANET_2_DARK, 5)
    create_rect(190, 305, PLANET_2_DARK, 5)
    create_rect(195, 305, PLANET_2_DARK, 5)
    create_rect(200, 305, PLANET_2_DARK, 5)
    create_rect(205, 305, PLANET_2_MAROON, 5)
    create_rect(210, 305, PLANET_2_MAROON, 5)
    # 310
    create_rect(155, 310, PLANET_2_OUTLINE, 5)
    create_rect(160, 310, PLANET_2_DARK, 5)
    create_rect(165, 310, PLANET_2_DARK, 5)
    create_rect(170, 310, PLANET_2_MID_1, 5)
    create_rect(175, 310, PLANET_2_MID_3, 5)
    create_rect(180, 310, PLANET_2_DARK, 5)
    create_rect(185, 310, PLANET_2_MUD, 5)
    create_rect(190, 310, PLANET_2_DARK, 5)
    create_rect(195, 310, PLANET_2_DARK, 5)
    create_rect(200, 310, PLANET_2_DARK, 5)
    create_rect(205, 310, PLANET_2_MAROON, 5)
    create_rect(210, 310, PLANET_2_OUTLINE, 5)
    # 315
    create_rect(155, 315, PLANET_2_OUTLINE, 5)
    create_rect(160, 315, PLANET_2_DARK, 5)
    create_rect(165, 315, PLANET_2_MID_1, 5)
    create_rect(170, 315, PLANET_2_MID_1, 5)
    create_rect(175, 315, PLANET_2_MID_2, 5)
    create_rect(180, 315, PLANET_2_MAROON, 5)
    create_rect(185, 315, PLANET_2_MAROON, 5)
    create_rect(190, 315, PLANET_2_MAROON, 5)
    create_rect(195, 315, PLANET_2_MAROON, 5)
    create_rect(200, 315, PLANET_2_MAROON, 5)
    create_rect(205, 315, PLANET_2_MAROON, 5)
    create_rect(210, 315, PLANET_2_OUTLINE, 5)
    # 320
    create_rect(160, 320, PLANET_2_OUTLINE, 5)
    create_rect(165, 320, PLANET_2_OUTLINE, 5)
    create_rect(170, 320, PLANET_2_DARK, 5)
    create_rect(175, 320, PLANET_2_MAROON, 5)
    create_rect(180, 320, PLANET_2_MAROON, 5)
    create_rect(185, 320, PLANET_2_MAROON, 5)
    create_rect(190, 320, PLANET_2_MAROON, 5)
    create_rect(195, 320, PLANET_2_DARK_1, 5)
    create_rect(200, 320, PLANET_2_OUTLINE, 5)
    create_rect(205, 320, PLANET_2_OUTLINE, 5)


def create_rect(x, y, color, px_size=PIXEL_SIZE):
    rect = GRect(px_size, px_size)
    rect.filled = True
    rect.color = color
    rect.fill_color = color
    window.add(rect, x, y)


def create_lines(gap=PIXEL_SIZE):
    for x in range(600, 1000, gap):
        line_x = GLine(x, 0, x, window.height)
        line_x.color = 'lightgrey'
        window.add(line_x)
    for y in range(0, 300, gap):
        line_y = GLine(0, y, window.width, y)
        line_y.color = 'lightgrey'
        window.add(line_y)


if __name__ == '__main__':
    main()
