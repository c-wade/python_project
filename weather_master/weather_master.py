"""
File: weather_master.py
Author: Wade Chao
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
"""
from Application import Application


class WeatherMaster(Application):

	def __init__(self):
		self.__APP_NAME = 'Weather Master 4.0'
		super().__init__(self.__APP_NAME)
		self.__QUIT_COMMAND = -100
		self.__LOW_TEMPERATURE_ALARM = 16
		self.__highest = -float('inf')
		self.__lowest = float('inf')
		self.__total = 0
		self.__steps = 0
		self.__cold_days = 0

	def _start_up(self):
		self.__set_temperatures()
		self.__reset()

	def __set_temperatures(self):
		"""
		Set data, get the highest/lowest value and calculate the total and steps
		"""
		while True:
			temp = self.__get_correct_input()
			if temp != self.__QUIT_COMMAND:
				self.__total += temp
				self.__steps += 1
				if temp > self.__highest:
					self.__highest = temp
				if temp < self.__lowest:
					self.__lowest = temp
				if temp < self.__LOW_TEMPERATURE_ALARM:
					self.__cold_days += 1
			else:
				self.__print_ans()
				break

	def __print_ans(self):
		"""
		pre-condition: data are set and user enter __QUIT_COMMAND
		post-condition: print the answer of the calculation
		"""
		if self.__steps == 0:
			print('============================')
			print('No temperatures were entered')
			print('============================')
		else:
			print('============================')
			print(f'Highest temperature: {self.__highest}')
			print(f'Lowest temperature: {self.__lowest}')
			print(f'Average: {self.__total / self.__steps}')
			print(f'{self.__cold_days} cold day(s)')
			print('===============================')

	def __reset(self):
		"""
		Reset all record and get ready for another calculation
		"""
		self.__highest = -float('inf')
		self.__lowest = float('inf')
		self.__total = 0
		self.__steps = 0
		self.__cold_days = 0

	def __get_correct_input(self):
		"""
		To make sure the input is a number
		:return: user input number
		"""
		while True:
			temp = input(f'Next Temperature: (or {self.__QUIT_COMMAND} to quit)? ')
			try:
				return int(temp)
			except ValueError:
				print('The input is not valid')


def main():
	WeatherMaster().start()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
