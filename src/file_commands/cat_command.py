import logging
from pathlib import Path


def command_cat(directory_path):
    """
    Реализация команды cat (вывод содержимого файла).
    Args:
        directory_path: Путь к файлу, содержимое которого нужно отобразить
    Returns:
        str or bool: Содержимое файла в случае успеха, False в случае ошибки
    """
    try:
        # Преобразуем путь в абсолютный
        cat_path = Path(directory_path).resolve()

        # Проверяем существование пути
        if cat_path.exists():
            if cat_path.is_file():
                # Читаем и возвращаем содержимое файла
                cat_answer = cat_path.read_text()
                return cat_answer
            else:
                # Путь существует, но это не файл
                logging.error(f"cannot access {str(cat_path)}: No such file")
                print('Введённый вами путь - не файл')
                return False
        else:
            # Путь не существует
            logging.error(f"ls: cannot access {str(cat_path)}: No such file")
            print('Введённый вами путь не существует')
            return False

    except Exception as err:
        # Логируем любые неожиданные ошибки
        logging.error(err)
        return False