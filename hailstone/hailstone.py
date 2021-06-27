"""
File: hailstone.py
Author: Wade Chao
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter.
"""
from Application import Application


class HailStone(Application):
    __APP_NAME = 'HailStone Calculator'
    __num = 1
    __steps = 0

    def __init__(self):
        super().__init__(self.__APP_NAME)

    def _start_up(self):
        self.__num = self.__get_correct_input()
        self.__hailstone_calculator()
        self.__print_ans()
        self.__reset()

    def __hailstone_calculator(self):
        """
        If __num is not 1, determine which action to take depends on __num is odd or even
        """
        while self.__num != 1:
            self.__steps += 1
            if self.__num % 2 == 0:
                self.__take_half()
            else:
                self.__times_three_plus_one()

    def __take_half(self):
        """
        __num divided by 2
        """
        print(f'{self.__num} is even, so I take half: {self.__num / 2}')
        self.__num /= 2

    def __times_three_plus_one(self):
        """
        __num times 3 then plus 1
        """
        print(f'{self.__num} is even, so I make 3n+1: {3 * self.__num + 1}')
        self.__num = 3 * self.__num + 1

    def __print_ans(self):
        """
        Print how many steps the calculation took
        """
        print('=========================================')
        print(f'It took {self.__steps} steps to reach 1.')
        print('=========================================')

    @staticmethod
    def __get_correct_input():
        """
        To make sure the input is a number
        :return: user input number
        """
        while True:
            temp = input('Enter a Number:')
            try:
                return int(temp)
            except ValueError:
                print('The input is not valid')

    def __reset(self):
        self.__num = 1
        self.__steps = 0


def main():
    HailStone().start()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
