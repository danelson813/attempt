from loguru import logger
from datetime import datetime


def timing(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        logger.info(
            f"Function {func.__name__} took "
            f"{round((end_time - start_time).total_seconds(), 3)} seconds to run."
        )
        return result

    return wrapper


def log(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Starting {func.__name__} function...")
        result = func(*args, **kwargs)
        logger.info(f"Finished {func.__name__} function.")
        return result

    return wrapper
