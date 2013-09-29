#!/usr/bin/python3

import os.path
import logging
import shutil
import subprocess

PYTHONBREW_DIR = "~/.pythonbrew"

SRC_DIR = './'

PYTHON_VER = '3.2'

def install():
    clean()
    logging.basicConfig(level=logging.DEBUG)
    install_python()
    install_requirements()


def clean():
    "Removes files the project can generate when being run."
    #subprocess.call("find . -name '*.pyc' -delete")
    #subprocess.call("find . -name '*~' -delete")

    if venv_exists():
        shutil.rmtree(PYTHONBREW_DIR, ignore_errors=True)


def install_python():
    subprocess.call("pythonbrew install " + PYTHON_VER, shell=True)
    subprocess.call("pythonbrew install 2.7", shell=True)
    subprocess.call("pythonbrew use " + PYTHON_VER, shell=True)


def venv_exists():
    return os.path.exists(PYTHONBREW_DIR)


def install_requirements():
    subprocess.call(PYTHONBREW_DIR + "/bin/pip3.2 install -r requirements.txt", shell=True)
    subprocess.call("pythonbrew use 2.7", shell=True)
    subprocess.call(PYTHONBREW_DIR + "/pythons/Python-2.7/bin/pip install fabric", shell=True)
    

install()