import logging

def setup_logger():
    logger = logging.getLogger("bot_logger")
    handler = logging.FileHandler("logs.txt", encoding="utf-8")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

logger = setup_logger()

def log_info(message):
    logger.info(message)

def log_error(message):
    logger.error(message)
