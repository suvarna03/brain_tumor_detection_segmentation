from src.brain_tumor_detection.logging.logger import logger
from src.brain_tumor_detection.exception.exception import BrainTumorException
import sys

if __name__ == "__main__":
    logger.info("Application started")

    try:
        a = 1 / 0
    except Exception as e:
        logger.error("Error occurred")
        raise BrainTumorException(e, sys)
