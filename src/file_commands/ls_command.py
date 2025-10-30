import logging
from pathlib import Path
from src.file_features import get_file_size, get_file_time, get_file_permissions
import os

def command_ls(directory_path=None, full_version=False):
    try:
        """Если директория пустая, то обрабатываем ту, в которой находимся"""
        if directory_path:
            directory_path = Path(directory_path).resolve()
        else:
            directory_path = Path(os.getcwd()).resolve()

        """Если введённый пользователем путь - не папка"""
        if not directory_path.is_dir():
            if directory_path.exists():
                """Если введённый пользователем путь - файл"""
                if directory_path.is_file():
                    if full_version:
                        file_path = str(directory_path)
                        file_size = get_file_size(file_path)
                        file_time = get_file_time(file_path)
                        file_permissions = get_file_permissions(file_path)
                        if file_size and file_time and file_permissions:
                          return [f'{file_size:10} {file_time} {file_permissions} {Path(file_path).name}']
                        else:
                            return False
                    else:
                        return [str(directory_path.name)]

                else:
                    logging.error(f"cannot access {str(directory_path)}: No such file or directory")
                    print('Введённый вами путь - не файл или директория')
                    return False
            else:
                logging.error(f"ls: cannot access {str(directory_path)}: No such file or directory")
                print('Введённый вами путь не существует')
                return False


        if full_version:
            """Создание списка содержимого папки, если пользователь вводил -l"""
            incomplete_files = list(map(str, directory_path.iterdir()))
            files = []
            for file_path in incomplete_files:
                file_size = get_file_size(file_path)
                file_time = get_file_time(file_path)
                file_permissions = get_file_permissions(file_path)
                if file_size and file_time and file_permissions:
                    files.append(f'{file_size:10} {file_time} {file_permissions} {Path(file_path).name}')
                else:
                    return False


        else:
            """Создание списка содержимого папки, если пользователь НЕ вводил -l"""
            incomplete_files = list(map(str, directory_path.iterdir()))
            files = []
            for file_path in incomplete_files:
                files.append(f'{Path(file_path).name}')

        """возвращаем содержимое папки в виде списка строк/списка списков строк"""
        return files
    except Exception as err:
        logging.error(err)
        return False
