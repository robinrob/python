import os
import string
import logging

env = os.environ

APP_NAME = 'archiver'

LOGGING_LEVEL = logging.INFO

LOG_DIR = os.path.join(os.path.abspath(os.sep), 'var', 'log', 'cr-case-email-archiving')

LOGGING_FORMAT = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')