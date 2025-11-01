import logging
import os
import shlex
from src.additional_functions.find_function import find_command


def run():
    """
    Основной цикл выполнения shell-программы.
    Обрабатывает пользовательский ввод, логирует команды и управляет
    жизненным циклом приложения.
    """
    try:
        logging.info('START PROGRAM')
        print("Чтобы выйти введи: 'exit'")

        # Главный цикл shell
        while True:
            try:
                # Отображаем текущую рабочую директорию
                working_directory = os.getcwd()
                user_message = input(f'{working_directory}$ ')
                logging.info(f'USER MESSAGE: {user_message}')

                # Проверяем команду выхода
                if user_message.lower() == 'exit':
                    break

                # Разбиваем введенную строку на токены (с поддержкой кавычек)
                user_message = shlex.split(user_message)

                # Передаем команду на обработку
                find_command(user_message)

            except Exception as err:
                print(err)
                logging.error(err)

        logging.info('END PROGRAM')

    except KeyboardInterrupt:
        # Обрабатываем прерывание от клавиатуры (Ctrl+C)
        logging.info('END PROGRAM')
    except Exception as err:
        logging.error(err)