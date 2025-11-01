
from src.file_commands.ls_command import command_ls


def ls(user_message):
    """
    Обрабатывает команду ls из пользовательского ввода.
    Args:
        user_message: Список аргументов команды (пути и флаги)
    Returns:
        bool: Всегда возвращает True
    """
    directory_paths = None
    full_version = False

    # Обрабатываем аргументы функции
    for ls_path in user_message:
        if ls_path == '-l':
            # Устанавливаем флаг подробного вывода
            full_version = True
        else:
            if directory_paths is None:
                directory_paths = [ls_path]
            else:
                directory_paths.append(ls_path)

    ls_answers = []
    if directory_paths is not None:
        # Обрабатываем каждый переданный путь
        for directory_path in directory_paths:
            ls_answer = command_ls(directory_path, full_version)
            if ls_answer:
                ls_answers.append(ls_answer)  # для каждого аргумента вызываем ф-ию
    else:
        # Если аргументов нет - выводим содержимое текущей директории
        ls_answer = command_ls(directory_paths, full_version)
        ls_answers.append(ls_answer)  # если аргумент l

    # Выводим результат
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