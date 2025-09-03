from loguru import logger

logger.add("log.log", mode="w")
logger.info("Logging has started *************************************")
