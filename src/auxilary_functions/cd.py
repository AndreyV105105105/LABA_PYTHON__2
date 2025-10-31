import logging

from src.file_commands.cd_command import command_cd

def cd(user_message):
    directory_path = None
    for cd_path in user_message:
        if directory_path is None:
            directory_path = cd_path
        else:
            logging.error('too many arguments')
            print('Ты ввёл слишком много аргументов')
            continue
    command_cd(directory_path)
    return True