import logging
import os
from pathlib import Path
import shutil

from src.additional_functions.is_directory_protected import is_path_protected


def command_rm(paths, recurs_version=None):
    """
    Реализует функциональность команды rm (удаление файлов и директорий).
Args:
        paths: Список путей для удаления
        recurs_version: Флаг рекурсивного удаления директорий

    Returns:
        bool: True если все операции успешны, False в случае ошибки
    """
    try:
        # Преобразуем пути в абсолютные
        paths = list(map(lambda x: Path(x).resolve(), paths))

        # Обрабатываем каждый путь отдельно
        for path in paths:
            rem_path = path

            # Проверка существования пути
            if not rem_path.exists():
                print(f"Не существует такого пути: '{str(rem_path)}'")
                logging.error(f"cannot stat '{str(rem_path)}': No such file or directory")
                continue

            try:
                # Удаление файла
                if rem_path.is_file():
                    os.remove(str(rem_path))

                # Удаление директории
                elif rem_path.is_dir():
                    # Проверка флага рекурсивного удаления
                    if not recurs_version:
                        print(f"Неуказан -r для удаления директории'{rem_path}'")
                        logging.error(f"-r not specified; omitting directory '{rem_path}'")
                        continue

                    # Запрос подтверждения для удаления директории
                    choice = None
                    while choice != 'y' and choice != 'n':
                        print(f'Ты уверен, что хочешь удалить директорию {str(rem_path)}?')
                        choice = input('y/n ')

                    if choice == 'n':
                        continue  # Пользователь отказался от удаления
                    else:
                        # Проверка защиты пути от удаления
                        if is_path_protected(rem_path):
                            print('Эту директорию запрещено удалять')
                            continue
                        else:
                            # Рекурсивное удаление директории со всем содержимым
                            shutil.rmtree(rem_path)

            except Exception as err:
                logging.error(err)
                return False

        return True

    except Exception as err:
        logging.error(err)
        return False