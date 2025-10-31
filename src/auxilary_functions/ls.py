import logging
from src.file_commands.ls_command import command_ls

"""Обрабатываем функцию ls"""
def ls(user_message):
    directory_paths = None
    full_version = False
    """Обрабатываем аргументы функции"""
    for ls_path in user_message:
        if ls_path == '-l':
            full_version = True
        else:
            if directory_paths is None:
                directory_paths = [ls_path]
            else:
                directory_paths.append(ls_path)

    ls_answers = []
    if directory_paths is not None:
        for directory_path in directory_paths:
            ls_answer = command_ls(directory_path, full_version)
            if ls_answer:
                ls_answers.append(ls_answer)  # для каждого аргумента вызываем ф-ию
    else:
        ls_answer = command_ls(directory_paths, full_version)
        ls_answers.append(ls_answer)  # если аргумент 1

    """Выводим результат"""
    if ls_answers:
        if full_version:
            for path in ls_answers:
                for file in path:
                    print(file)
                print()
        else:
            for path in ls_answers:
                for file in path:
                    print(file)
                print()
    return True
