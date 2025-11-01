import logging
from src.file_commands.cp_command import command_cp


def cp(user_message):
    """
    Обрабатывает команду cp из пользовательского ввода.
    Args:
        user_message: Список аргументов команды (пути и флаги)
    Returns:
        bool: Всегда возвращает True
    """
    paths = None
    recurs_version = False

    # Обрабатываем аргументы функции
    for cp_path in user_message:
        if cp_path == '-r':
            # Устанавливаем флаг рекурсивного копирования
            recurs_version = True
        else:
            if paths is None:
                paths = [cp_path]
            else:
                paths.append(cp_path)

    if paths is not None:
        command_cp(paths, recurs_version)
    else:
        print('Ты не ввёл аргументы')
        logging.error('missing file operand')

    return True