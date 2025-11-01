import logging
from src.file_commands.cd_command import command_cd


def cd(user_message):
    """
    Обрабатывает команду cd из пользовательского ввода.
    Args:
        user_message: Список аргументов команды (только один путь ожидается)
    Returns:
        bool: Всегда возвращает True
    """
    directory_path = None

    # Обрабатываем аргументы - ожидаем только один путь
    for cd_path in user_message:
        if directory_path is None:
            directory_path = cd_path
        else:
            # Предупреждаем о слишком многих аргументах
            logging.error('too many arguments')
            print('Ты ввёл слишком много аргументов')
            continue

    command_cd(directory_path)
    return True