import logging
import traceback
import settings
from datetime import datetime

logger = logging.getLogger(settings.APP_NAME)
logger.setLevel(logging.INFO)

timestamp = datetime.today(). strftime('%Y_%m_%d_%H_%M_%S')
file_handler = logging.FileHandler(settings.LOG_DIR + '/' + timestamp + '.txt')
file_handler.setLevel(level=settings.LOGGING_LEVEL)
file_handler.setFormatter(settings.LOGGING_FORMAT)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setLevel(level=settings.LOGGING_LEVEL)
console_handler.setFormatter(settings.LOGGING_FORMAT)
logger.addHandler(console_handler)

class Logger:

    def __init__(self):
        self.logger = logging.getLogger(settings.APP_NAME)


    def error(self, e, msg=''):
        self.logger.exception('' + msg + ' ' + traceback.format_exc())


    def info(self, msg=''):
        self.logger.info('' + msg)


    def debug(self, msg=''):
        self.logger.debug('' + msg)


    def logger(self):
        return self.logger