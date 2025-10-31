import logging
from src.file_commands.cat_command import command_cat

def cat(user_message):
    directory_paths = None
    """Обрабатываем аргументы функции"""
    for cat_path in user_message[1:]:
        if directory_paths is None:
            directory_paths = [cat_path]
        else:
            directory_paths.append(cat_path)

    cat_path_answers = []
    if directory_paths is not None:
        for directory_path in directory_paths:
            cat_answer = command_cat(directory_path)
            if cat_answer:
                cat_path_answers.append(cat_answer)  # для каждого аргумента вызываем ф-ию
    else:
        print('Ты не ввёл аргументы')
        logging.error('no many arguments')

    """Выводим результат"""
    if cat_path_answers:
        for path in cat_path_answers:
            print(path)

    return True