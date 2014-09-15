#!/usr/bin/env python

from logger import Logger

log = Logger()

try:
    a

except Exception as e:
    log.error(e)