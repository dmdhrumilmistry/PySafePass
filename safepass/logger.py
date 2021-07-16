import logging


logging.basicConfig(filename='SafePass.log', encoding='utf-8', level=logging.DEBUG)


def info(log:str):
    logging.info(log)


def warning(log:str):
    logging.warning(log)


def error(log:str):
    logging.error(log)

