import subprocess
import logging

from fabric.decorators import task

PYTHONBREW_DIR = "~/.pythonbrew"
PYTHON_APP = "matrix.py"

SRC_DIR = './'

PYTHON2 = '2.7'
PYTHON3 = '3.2'

@task
def install():
    logging.basicConfig(level=logging.DEBUG)
    install_python()
    install_requirements()


def install_python():
    subprocess.call("pythonbrew install " + PYTHON3, shell=True)
    

def use_python(version):
    subprocess.call("pythonbrew use " + version, shell=True)
        

def install_requirements():
    use_python(PYTHON3)
    subprocess.call("pip install -r requirements.txt", shell=True)
    

@task
def clean():
    subprocess.call("find . -name '*.pyc' -delete", shell=True)
    subprocess.call("find . -name '*~' -delete", shell=True)
    subprocess.call("find . -name '__pycache__' -delete", shell=True)


@task
def test():
    subprocess.call("nosetests", shell=True)


@task(args="")
def run(app=PYTHON_APP, args=""):
    subprocess.call("pythonbrew py -p " + PYTHON3 + " " + PYTHON_APP + " " + args, shell=True)


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


@task
def readme():
    subprocess.call("less README.md", shell=True)