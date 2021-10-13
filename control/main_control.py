import os


class MainController:
    @staticmethod
    def clear():
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            _ = os.system('cls')

    @staticmethod
    def exit_program():
        pass