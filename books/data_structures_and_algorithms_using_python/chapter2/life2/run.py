#!/usr/bin/python

import sys
import subprocess

args = ""
for i in range(1, len(sys.argv)):
    args += sys.argv[i] + " "

subprocess.call("pythonbrew py life.py " + args, shell=True)