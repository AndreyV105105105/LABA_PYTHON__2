import logging
import os
from pathlib import Path
import shutil

from src.additional_functions.is_directory_protected import is_path_protected


def command_rm(paths, recurs_version=None):
    try:
        paths = list(map(lambda x: Path(x).resolve(), paths))
        for path in paths:
            rem_path = path
            if not rem_path.exists():
                print(f"Не существует такого пути: '{str(rem_path)}'")
                logging.error(f"cannot stat '{str(rem_path)}': No such file or directory")
                continue
            try:
                if rem_path.is_file():
                    os.remove(str(rem_path))
                elif rem_path.is_dir():
                    if not recurs_version:
                        print(f"Неуказан -r для удаления директории'{rem_path}'")
                        logging.error(f"-r not specified; omitting directory '{rem_path}'")
                        continue
                    choice = None
                    while choice != 'y' and choice != 'n':
                        print(f'Ты уверен, что хочешь удалить директорию {str(rem_path)}?')
                        choice = input('y/n ')
                    if choice == 'n':
                        continue
                    else:
                        if is_path_protected(rem_path):
                            print('Эту директорию запрещено удалять')
                            continue
                        else:
                            shutil.rmtree(rem_path)

            except Exception as err:
                logging.error(err)
                return False
        return True
    except Exception as err:
        logging.error(err)
        return False