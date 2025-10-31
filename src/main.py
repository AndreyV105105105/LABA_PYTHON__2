import logging
from src.loggins import setup_logging
from src.additional_functions.run import run



def main():
    try:
        setup_logging()
        run()
    except Exception as err:
        logging.error(err)
            
if __name__ == "__main__":
    main()
