import logging
from pathlib import Path

def command_cat(directory_path):
    try:
        cat_path = Path(directory_path).resolve()
        if cat_path.exists():
            if cat_path.is_file():
                cat_answer = cat_path.read_text()
                return cat_answer
            else:
                logging.error(f"cannot access {str(cat_path)}: No such file")
                print('Введённый вами путь - не файл')
                return False
        else:
            logging.error(f"ls: cannot access {str(cat_path)}: No such file")
            print('Введённый вами путь не существует')
            return False

    except Exception as err:
        logging.error(err)
        return False
