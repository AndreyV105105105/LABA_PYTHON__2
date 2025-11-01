import logging
from pathlib import Path


def is_path_protected(path):
    """
    Проверяет, является ли путь защищенным от определенных операций.
    Защищенные пути включают корневую директорию, родительскую директорию,
    текущую директорию и рабочую директорию.
    Args:
        path: Путь для проверки
    Returns:
        bool: True если путь защищен, False если нет или произошла ошибка
    """
    # Нормализуем входной параметр до Path объекта
    if type(path) == str:
        path = Path(path).resolve()

    # Список защищенных путей
    protected_paths = [
        Path('/').resolve(),  # Корневая директория
        Path('..').resolve(),  # Родительская директория
        Path('.'),  # Текущая директория
        Path.cwd()  # Рабочая директория
    ]

    try:
        if path in protected_paths:
            return True

        return False
    except Exception as err:
        logging.error(err)
        return False