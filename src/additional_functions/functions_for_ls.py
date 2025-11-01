import logging
import os
import stat
from datetime import datetime
from pathlib import Path


def get_file_permissions(file_path):
    """
    Функция для получения информации о разрешениях файла в формате Unix (rwx).
    Note:
        На Windows нормально не работает, потому что у неё свой формат разрешений,
        а не как на Unix системах rwx.
    Args:
        file_path: Путь к файлу
    Returns:
        str or bool: Строка с разрешениями или False в случае ошибки
    """
    try:
        file_stat = os.stat(file_path)
        file_permissions = stat.filemode(file_stat.st_mode)
        return file_permissions
    except Exception as err:
        logging.error(err)
        return False


def get_file_size(file_path):
    """
    Функция для получения информации о размере файла/директории.
    Args:
        file_path : Путь к файлу/директории
    Returns:
        str or bool: Размер файла в виде строки или False в случае ошибки
    """
    try:
        file_path = Path(file_path)
        file_size = file_path.stat().st_size
        return str(file_size)
    except Exception as err:
        logging.error(err)
        return False


def get_file_time(file_path):
    """
    Функция для получения информации о времени последнего изменения.
    Args:
        file_path: Путь к файлу/директории
    Returns:
        str or bool: Время изменения в формате 'YYYY-MM-DD HH:MM' или False в случае ошибки
    """
    try:
        file_path = Path(file_path)
        # Получаем время модификации и форматируем его
        file_time = str(datetime.fromtimestamp(os.path.getmtime(file_path))).split()
        file_time = f'{file_time[0]} {file_time[1][0:5]}'  # Обрезаем лишнее
        return file_time
    except Exception as err:
        logging.error(err)
        return False