import logging
from src.loggins import setup_logging
from src.additional_functions.run import run


def main():
    """
    Главная функция приложения.

    Инициализирует систему логирования и запускает основной цикл программы.
    """
    try:
        # Настраиваем логирование
        setup_logging()
        # Запускаем основной цикл программы
        run()
    except Exception as err:
        logging.error(err)


if __name__ == "__main__":
    main()