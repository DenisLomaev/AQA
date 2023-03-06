import logging


def my_log():
    logging.basicConfig(format="%(asctime)-15s %(message)s", filemode="w")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler("./generator_requests.log")
    fh.setLevel(logging.INFO)
    logger.addHandler(fh)
    return logger
