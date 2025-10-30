import logging
import os
from pathlib import Path
# import shlex
from src.loggins import setup_logging
from src.necessary_functions import find_necessary_command



def main():
    setup_logging()
    try:
        logging.info('START PROGRAM')
        while True:
            try:
                working_directory = os.getcwd()
                user_message = input(f'{working_directory} ')
                logging.info(f'USER MESSAGE: {user_message}')

                if user_message.lower() == 'exit':
                    break

                user_message = user_message.split()

                find_necessary_command(user_message)
            except Exception as err:
                logging.error(err)

        logging.info('END PROGRAM')
    except KeyboardInterrupt:
        logging.info('END PROGRAM')
    except Exception as err:
        logging.error(err)
            
if __name__ == "__main__":
    main()
