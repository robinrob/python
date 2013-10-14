import subprocess
import logging

from fabric.decorators import task

PYTHONBREW_DIR = "~/.pythonbrew"
PYTHON_APP = "python_app.py"

SRC_DIR = './'

PYTHON_VER = '3.2'

@task
def install():
    logging.basicConfig(level=logging.DEBUG)
    install_python()
    install_requirements()


@task
def install_python():
    subprocess.call("pythonbrew install 2.7", shell=True)
    subprocess.call("pythonbrew install " + PYTHON_VER, shell=True)


@task
def install_requirements():
    subprocess.call("pythonbrew use " + PYTHON_VER, shell=True)
    subprocess.call("pip install -r requirements.txt", shell=True)
    

@task
def clean():
    subprocess.call("find . -name '*.pyc' -delete", shell=True)
    subprocess.call("find . -name '*~' -delete", shell=True)
    subprocess.call("find . -name '__pycache__' -delete", shell=True)


@task(args="")
def run(args):
    subprocess.call("pythonbrew py -p " + PYTHON_VER + " " + PYTHON_APP + " " + args, shell=True)


@task
def count():
    clean()
    subprocess.call("find . -name '*.py' | xargs wc -l", shell=True)


@task(message="")
def commit(message="Auto-update."):
    clean()
    subprocess.call("git add *.py", shell=True)
    subprocess.call("git add -u", shell=True)
    subprocess.call("git add README.md", shell=True)
    subprocess.call("git add requirements.txt", shell=True)
    subprocess.call("git commit -m '" + message + "'", shell=True)
    subprocess.call("git push origin develop", shell=True)