import logging
from pathlib import Path
import shutil


def command_cp(paths, recurs_version=None):
    """
    Реализация команды cp для копирования файлов и директорий

    Args:
        paths: список путей к исходным файлам/директориям и целевому пути
        recurs_version: флаг рекурсивного копирования для директорий (-r)

    Returns:
        bool: True если копирование выполнено успешно, False в случае ошибки
    """
    try:
        # Преобразуем все пути в абсолютные
        paths = list(map(lambda x: Path(x).resolve(), paths))

        # Проверка минимального количества аргументов
        if len(paths) == 1:
            print('Ты не ввёл путь назначения')
            logging.error(f"missing destination file operand after '{str(paths[0])}'")
            return False

        # Обработка копирования одного источника в одно назначение
        elif len(paths) == 2:
            # Проверка существования исходного пути
            if not paths[0].exists():
                print(f"Не существует такого пути: '{str(paths[0])}'")
                logging.error(f"cannot stat '{str(paths[0])}': No such file or directory")
                return False

            # Проверка существования целевой директории (если указана как директория)
            if not paths[1].exists() and paths[1].is_dir():
                print(f"Не существует такой директории: '{str(paths[1])}'")
                logging.error(f"cannot stat '{str(paths[1])}': No such directory")
                return False

            # Защита от копирования в самого себя
            if paths[0] == paths[1]:
                print('Нельзя скопировать в самого себя')
                logging.error(f"cannot copy a directory, '{str(paths[0])}', into itself, '{str(paths[0])}/"
                              f"{str(paths[0])}'")
                return False

            try:
                destination_path = paths[1]
                dispatch_path = paths[0]

                # Копирование файла
                if dispatch_path.is_file():
                    shutil.copy2(dispatch_path, destination_path)
                    return True

                # Копирование директории
                elif dispatch_path.is_dir():
                    if not recurs_version:
                        print(f"Неуказан -r для копирования директории'{dispatch_path}'")
                        logging.error(f"-r not specified; omitting directory '{dispatch_path}'")
                        return False
                    shutil.copytree(dispatch_path, destination_path)
                    return True

            except Exception as err:
                logging.error(err)

        # Обработка копирования нескольких источников в одну директорию
        else:
            destination_path = paths[-1]

            # Проверка существования целевой директории
            if not destination_path.exists():
                print(f"Не существует такого пути: '{str(destination_path)}'")
                logging.error(f"cannot stat '{str(destination_path)}': No such directory")
                return False

            if not destination_path.is_dir():
                print(f"Папка назначения - не директория'")
                logging.error(f"destination_path '{str(destination_path)}': Not directory")
                return False

            # Копирование каждого исходного пути
            for path in paths[:-1]:
                dispatch_path = path
                if not dispatch_path.exists():
                    print(f"Не существует такого пути: '{str(dispatch_path)}'")
                    logging.error(f"cannot stat '{str(dispatch_path)}': No such file or directory")
                    continue

                try:
                    # Копирование файла
                    if dispatch_path.is_file():
                        shutil.copy2(dispatch_path, destination_path)

                    # Копирование директории
                    elif dispatch_path.is_dir():
                        if not recurs_version:
                            print(f"Неуказан -r для копирования директории'{dispatch_path}'")
                            logging.error(f"-r not specified; omitting directory '{dispatch_path}'")
                            continue
                        shutil.copytree(dispatch_path, destination_path)

                except Exception as err:
                    logging.error(err)
                    return False

            return True

    except Exception as err:
        logging.error(err)
        return False