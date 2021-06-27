class Application(object):
    def __init__(self, app_name):
        self._application_name = f'{app_name}'

    def start(self):
        """
        Start WeatherMaster :
            - Enter s to input data
            - Enter q to quit WeatherMaster
        """
        print('===============================================')
        print(f'Thanks for using stanCode "{self._application_name}"!')
        print('===============================================')
        while True:
            print('> Enter s to start')
            print('> Enter q to quit')
            action = input('> ')
            if action == 's' or action == 'S':
                self._start_up()
            if action == 'q' or action == 'Q':
                print('=====================')
                print('Have a good day, bye~')
                print('=====================')
                break

    def _start_up(self):
        print('Application Start Up')