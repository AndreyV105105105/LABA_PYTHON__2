import logging
import os
import shlex
from src.additional_functions.find_function import find_command


def run():
    try:
        logging.info('START PROGRAM')
        while True:
            try:
                working_directory = os.getcwd()
                user_message = input(f'{working_directory}$ ')
                logging.info(f'USER MESSAGE: {user_message}')

                if user_message.lower() == 'exit':
                    break

                user_message = shlex.split(user_message)

                find_command(user_message)
            except Exception as err:
                print(err)
                logging.error(err)

        logging.info('END PROGRAM')
    except KeyboardInterrupt:
        logging.info('END PROGRAM')
    except Exception as err:
        logging.error(err)