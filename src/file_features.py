import logging
import os
import stat
from datetime import datetime
from pathlib import Path


def get_file_permissions(file_path):
    """Функция для получения информации о разрешениях файла
    На винде нормально не работает, потому что у неё какой-то свой формат разрешений, а не как на unix системах rwx"""
    try:
        file_stat = os.stat(file_path)
        file_permissions = stat.filemode(file_stat.st_mode)
        return file_permissions
    except Exception as err:
        logging.error(err)
        return False


def get_file_size(file_path):
    """Функция для получения информации о размере файла/директории"""
    try:
        file_path = Path(file_path)
        file_size = file_path.stat().st_size
        return str(file_size)
    except Exception as err:
        logging.error(err)
        return False


def get_file_time(file_path):
    """Функция для получения информации о последнем времени изменения"""
    try:
        file_path = Path(file_path)
        file_time = str(datetime.fromtimestamp(os.path.getmtime(file_path))).split()
        file_time = f'{file_time[0]} {file_time[1][0:5]}'
        return file_time
    except Exception as err:
        logging.error(err)
        return False



