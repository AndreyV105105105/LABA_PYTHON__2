import logging
from src.file_commands.mv_command import command_mv


def mv(user_message):
    paths = None
    """Обрабатываем аргументы функции"""
    for mv_path in user_message:
        if paths is None:
            paths = [mv_path]
        else:
            paths.append(mv_path)
    if paths is not None:
        command_mv(paths)
    else:
        print('Ты не ввёл аргументы')
        logging.error('missing file operand')
    return True