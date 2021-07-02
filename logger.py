import logging

# Gets or creates a logger

logging.basicConfig(filename='SafePass.log', encoding='utf-8', level=logging.DEBUG)
# logger.basicConfig(filename='Safepass.log')


def info(log:str):
    logging.info(log)


def warning(log:str):
    logging.warning(log)


def error(log:str):
    logging.error(log)


#logger.critical('Fatal error. Cannot continue')