import logging
from pathlib import Path

def is_path_protected(path):
    if type(path) == str:
        path = Path(path).resolve()
    protected_paths = [Path('/').resolve(), Path('..').resolve(), Path('.'), Path.cwd()]
    try:
        if path in protected_paths:
            return True

        return False
    except Exception as err:
        logging.error(err)
        return False