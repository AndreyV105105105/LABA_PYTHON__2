import logging


def setup_logging():
    """
    Базовая функция для настройки логирования.
    Настраивает базовую конфигурацию логирования:
    - Уровень: INFO
    - Файл: shell.log
    - Режим: перезапись ('w')
    - Формат: дата-время, уровень, сообщение
    """
    logging.basicConfig(level=logging.INFO, filename="shell.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")