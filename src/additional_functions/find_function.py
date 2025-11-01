import logging

from src.auxiliary_functions.ls import ls
from src.auxiliary_functions.cd import cd
from src.auxiliary_functions.cat import cat
from src.auxiliary_functions.cp import cp
from src.auxiliary_functions.mv import mv
from src.auxiliary_functions.rm import rm


def find_command(user_message):
    """
    Функция-маршрутизатор для обработки команд, введенных пользователем.

    Определяет какую команду вызвать на основе первого аргумента
    и передает управление соответствующему обработчику.

    Args:
        user_message: Список токенов введенной команды
    Returns:
        bool: False если команда неизвестна или произошла ошибка, иначе True
    """
    # Проверяем, что не пустая строка
    if user_message:
        try:
            # Определяем команду и вызываем соответствующий обработчик
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