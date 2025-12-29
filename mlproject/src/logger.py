import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

LOG_FILE=f"app_{datetime.now().strftime('%Y_%m_%d')}.log"
logs_path=os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok=True) 

log_file_path=os.path.join(logs_path,LOG_FILE)   


logging.basicConfig(
    filename=log_file_path,
    format="[%(lineno)d] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


if __name__ == "__main__":
    logger=logging.getLogger()
    logger.info("Logging has started")
    logger.error("This is an error message")