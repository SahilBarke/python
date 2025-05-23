import logging
import logging.config
import os

def setup_logging(config_file='logging.conf'):
    if os.path.exists(config_file):
        logging.config.fileConfig(config_file)
        logger = logging.getLogger(__name__)
        logger.info("Logging has been configured.")
    else:
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
        logger.warning(f"Logging configuration file '{config_file}' not found. Using basic configuration.")

if __name__ == "__main__":
    setup_logging("Python Logging/logging.conf")
    logger = logging.getLogger("sampleLogger")
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")
