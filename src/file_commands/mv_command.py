import logging
from pathlib import Path
import shutil


def command_mv(paths):
    """
    Реализует функциональность команды mv (перемещение/переименование файлов и директорий).
    Args:
        paths: Список путей, где последний элемент - путь назначения,
                     а предыдущие - источники для перемещения

    Returns:
        bool: True если операция успешна, False в случае ошибки
    """
    try:
        # Делаем все пути абсолютными
        paths = list(map(lambda x: Path(x).resolve(), paths))

        # Обработка случая с одним путем (не указан destination)
        if len(paths) == 1:
            print('Ты не ввёл путь назначения')
            logging.error(f"missing destination file operand after '{str(paths[0])}'")
            return False

        # Обработка случая с двумя путями (источник и назначение)
        elif len(paths) == 2:
            # Проверка существования исходного пути
            if not paths[0].exists():
                print(f"Не существует такого пути: '{str(paths[0])}'")
                logging.error(f"cannot stat '{str(paths[0])}': No such file or directory")
                return False

            # Проверка существования целевого пути (если это директория)
            if not paths[1].exists() and paths[1].is_dir():
                print(f"Не существует такой директории: '{str(paths[1])}'")
                logging.error(f"cannot stat '{str(paths[1])}': No such directory")
                return False

            # Защита от перемещения в самого себя
            if paths[0] == paths[1]:
                print('Нельзя переместить в самого себя')
                logging.error(f"cannot move a directory, '{str(paths[0])}', into itself, '{str(paths[0])}/"
                              f"{str(paths[0])}'")
                return False

            try:
                destination_path = paths[1]
                dispatch_path = paths[0]

                # Проверка: нельзя переместить директорию в файл
                if destination_path.is_file() and dispatch_path.is_dir():
                    print('Нельзя переместить директорию в файл')
                    logging.error(f"cannot move a directory, '{str(paths[0])}', into file, '{str(paths[0])}'")
                    return False

                # Выполняем перемещение
                shutil.move(dispatch_path, destination_path)
                return True

            except Exception as err:
                logging.error(err)

        # Обработка случая с несколькими источниками и одним назначением
        else:
            destination_path = paths[-1]

            # Проверка существования целевой директории
            if not destination_path.exists():
                print(f"Не существует такого пути: '{str(destination_path)}'")
                logging.error(f"cannot stat '{str(destination_path)}': No such directory")
                return False

            # Проверка, что цель - действительно директория
            if not destination_path.is_dir():
                print(f"Папка назначения - не директория'")
                logging.error(f"destination_path '{str(destination_path)}': Not directory")
                return False

            # Перемещаем все исходные пути в целевую директорию
            for path in paths[:-1]:
                dispatch_path = path
                if not dispatch_path.exists():
                    print(f"Не существует такого пути: '{str(dispatch_path)}'")
                    logging.error(f"cannot stat '{str(dispatch_path)}': No such file or directory")
                    continue
                try:
                    shutil.move(dispatch_path, destination_path)
                except Exception as err:
                    logging.error(err)
                    return False
            return True

    except Exception as err:
        logging.error(err)
        return False