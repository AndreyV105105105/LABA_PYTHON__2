import logging
from pathlib import Path
from src.additional_functions.functions_for_ls import get_file_size, get_file_time, get_file_permissions
import os


def command_ls(directory_path=None, full_version=False):
    """
    Реализация команды ls для отображения содержимого директории

    Args:
        directory_path: путь к директории для отображения. Если None - текущая директория
        full_version: флаг подробного отображения (-l)

    Returns:
        list: список строк с информацией о файлах/директориях или False в случае ошибки
    """
    try:
        # Преобразуем путь в абсолютный
        if directory_path:
            directory_path = Path(directory_path).resolve()
        else:
            directory_path = Path(os.getcwd()).resolve()

        # Обработка случая, когда путь ведет не к директории
        if not directory_path.is_dir():
            if directory_path.exists():
                # Если путь ведет к файлу - обрабатываем как одиночный файл
                if directory_path.is_file():
                    if full_version:
                        # Подробная информация о файле
                        file_path = str(directory_path)
                        file_size = get_file_size(file_path)
                        file_time = get_file_time(file_path)
                        file_permissions = get_file_permissions(file_path)
                        if file_size and file_time and file_permissions:
                            return [f'{file_size:10} {file_time} {file_permissions} {Path(file_path).name}']
                        else:
                            return False
                    else:
                        # Просто имя файла
                        return [str(directory_path.name)]

                else:
                    # Путь существует, но не является ни файлом ни директорией
                    logging.error(f"cannot access {str(directory_path)}: No such file or directory")
                    print('Введённый вами путь - не файл или директория')
                    return False
            else:
                # Путь не существует
                logging.error(f"ls: cannot access {str(directory_path)}: No such file or directory")
                print('Введённый вами путь не существует')
                return False

        # Подробный вывод с опцией -l
        if full_version:
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

        # Простой вывод (только имена)
        else:
            incomplete_files = list(map(str, directory_path.iterdir()))
            files = []
            for file_path in incomplete_files:
                files.append(f'{Path(file_path).name}')

        return files

    except Exception as err:
        logging.error(err)
        return False