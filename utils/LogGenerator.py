import logging
from config.settings import TestSettings


class LogGenerator:

    @staticmethod
    def log_generator():
        logger = logging.getLogger()
        file_handler = logging.FileHandler(filename=TestSettings.LOG_PATH, mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger
