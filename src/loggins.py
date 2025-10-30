import logging
"""базовая функция для логирования"""
def setup_logging():
    logging.basicConfig(level=logging.INFO, filename="shell.log", filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")
