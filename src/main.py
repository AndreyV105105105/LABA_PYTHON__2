import logging
import shlex
from pathlib import Path
from src.loggins import setup_logging
from src.necessary_functions import find_necessary_command



def main():
    setup_logging()
    try:
        logging.info('START PROGRAM')
        while True:
            user_message = input(f'{Path.cwd()} ') # FIX
            logging.info(f'USER MESSAGE: {user_message}')

            if user_message.lower() == 'exit':
                break

            user_message = shlex.split(user_message)

            find_necessary_command(user_message)

        logging.info('END PROGRAM')
    except KeyboardInterrupt:
        logging.info('END PROGRAM')
    except Exception as err:
        logging.error(err)
            
if __name__ == "__main__":
    main()
