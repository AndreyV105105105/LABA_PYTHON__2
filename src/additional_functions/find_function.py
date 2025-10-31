import logging


from src.auxilary_functions.ls import ls
from src.auxilary_functions.cd import cd
from src.auxilary_functions.cat import cat
from src.auxilary_functions.cp import cp
from src.auxilary_functions.mv import mv
from src.auxilary_functions.rm import rm


def find_command(user_message):
    """Функция для обработки команд введённых пользователем"""
    if user_message: # Проверяем, что не пустая строка
        try:
            if user_message[0] == 'ls':
                ls(user_message[1:])
            elif user_message[0] == 'cd':
                cd(user_message[1:])
            elif user_message[0] == 'cat':
                cat(user_message[1:])
            elif user_message[0] == 'cp':
                cp(user_message[1:])
            elif user_message[0] == 'mv':
                mv(user_message[1:])
            elif user_message[0] == 'rm':
                rm(user_message[1:])
            else:
                print('Введена неизвестная команда')
                return False

        except Exception as err:
            logging.error(err)
            return False
    else:
        return True