import logging
from pathlib import Path
import os


def command_cd(directory_path):
    try:
        cd_path = None
        if directory_path is None:
            os.chdir(os.path.expanduser('~'))
            return True
        if directory_path == '~' or directory_path.startswith('~/'):
            if directory_path == '~':
                os.chdir(os.path.expanduser('~'))
                return True
            else:
                home_directory = os.path.expanduser('~')
                cd_path= Path(f'{home_directory}/{directory_path[2:]}')
        if cd_path is None:
            cd_path = Path(directory_path).resolve()

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
