import sys
import subprocess
import logging

from fabric.decorators import task

PYTHONBREW_DIR = "~/.pythonbrew"

SRC_DIR = './'

PYTHON_VER = '3.2'

@task
def install():
    logging.basicConfig(level=logging.DEBUG)
    install_python()
    install_requirements()


@task
def install_python():
    subprocess.call("pythonbrew install " + PYTHON_VER, shell=True)
    subprocess.call("pythonbrew install 2.7", shell=True)
    subprocess.call("pythonbrew use " + PYTHON_VER, shell=True)


@task
def install_requirements():
    subprocess.call(PYTHONBREW_DIR + "/bin/pip3.2 install -r requirements.txt", shell=True)
    subprocess.call("pythonbrew use 2.7", shell=True)
    

@task
def clean():
    subprocess.call("find . -name '*.pyc' -delete", shell=True)
    subprocess.call("find . -name '*~' -delete", shell=True)


@task(args='')
def run(args):
    subprocess.call("pythonbrew py -p " + PYTHON_VER + " life.py " + args, shell=True)