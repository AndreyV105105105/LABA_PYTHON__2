import logging

from src.file_commands.ls_command import command_ls
from src.file_commands.cd_command import command_cd


def find_necessary_command(user_message):
    """Функция для обработки команд введённых пользователем"""
    if user_message: # Проверяем, что не пустая строка

        """Обработка команды ls
        В зависимости от введённых пользователем доп. аргументов по разному вызываем функцию"""
        try:
            """Обрабатываем функцию ls"""
            if user_message[0] == 'ls':
                directory_paths = None
                full_version = False
                """Обрабатываем аргументы функции"""
                for ls_path in user_message[1:]:
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
                            ls_answers.append(ls_answer) # для каждого аргумента вызываем ф-ию
                else:
                    ls_answer = command_ls(directory_paths, full_version)
                    ls_answers.append(ls_answer) # если аргумент 1

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

            elif user_message[0] == 'cd':
                directory_path = None
                for cd_path in user_message[1:]:
                    if directory_path is None:
                        directory_path = cd_path
                    else:
                        logging.error('too many arguments')
                        print('Ты ввёл слишком много аргументов')
                        continue
                command_cd(directory_path)


            elif user_message[0] == 'cat':
                pass
            elif user_message[0] == 'cp':
                pass
            elif user_message[0] == 'mv':
                pass
            elif user_message[0] == 'rm':
                pass
            else:
                print('Введена неизвестная команда')
                return False

        except Exception as err:
            logging.error(err)
            return False
    else:
        return True