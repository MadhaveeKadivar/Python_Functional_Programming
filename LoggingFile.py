import logging
# Logging

def func():
    logging.basicConfig(filename = 'file.log',format = '%(asctime)s | %(levelname)s | %(lineno)d: %(message)s')
    logger = logging.getLogger("root_logger")
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    log_format = '%(message)s'
    console_handler.setFormatter(logging.Formatter(log_format))
    logger.addHandler(console_handler)
    return logger
