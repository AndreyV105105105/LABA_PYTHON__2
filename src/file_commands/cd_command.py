import logging
from pathlib import Path
import os


def command_cd(directory_path):
    """
    Реализация команды cd для смены текущей рабочей директории

    Args:
        directory_path: путь к целевой директории. Может быть None (переход в домашнюю директорию),
                       '~' (домашняя директория), '~/path' (относительный путь от домашней директории)
                       или обычный путь

    Returns:
        bool: True если переход выполнен успешно, False в случае ошибки
    """
    try:
        cd_path = None

        # Если путь не указан, переходим в домашнюю директорию
        if directory_path is None:
            os.chdir(os.path.expanduser('~'))
            return True

        # Обрабатываем специальные пути с ~
        if directory_path == '~' or directory_path.startswith('~/'):
            if directory_path == '~':
                os.chdir(os.path.expanduser('~'))
                return True
            else:
                # Комбинируем домашнюю директорию с указанным путем
                home_directory = os.path.expanduser('~')
                cd_path = Path(f'{home_directory}/{directory_path[2:]}')

        # Если путь не обработан ранее, используем как обычный путь
        if cd_path is None:
            cd_path = Path(directory_path).resolve()

        # Проверяем существование пути
        if cd_path.exists():
            if cd_path.is_dir():
                os.chdir(str(cd_path))
                return True
            else:
                logging.error(f"cannot access {str(directory_path)}: No such directory")
                print('Введённый вами путь - не директория')
                return False
        else:
            logging.error(f"ls: cannot access {str(cd_path)}: No such directory")
            print('Введённый вами путь не существует')
            return False

    except Exception as err:
        logging.error(err)
        return False