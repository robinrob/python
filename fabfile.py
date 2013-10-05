import subprocess
import logging
import os

from fabric.decorators import task

# Configurable parameters
PYTHONBREW_DIR = "~/.pythonbrew"

SRC_DIR = './'

PYTHON3 = '3.2'

# Do not change this - used in initial installation
PYTHON_APP = "python_app.py"

@task
def install():
    if os.path.exists(PYTHON_APP):
        cwd_name = os.getcwd().split(os.sep)[-1]
        os.rename(PYTHON_APP, cwd_name + '.py')

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


@task
def run(app=PYTHON_APP, args="Hello\!"):
    subprocess.call("pythonbrew py -p " + PYTHON3 + " " + app + " " + args, shell=True)


@task
def count():
    clean()
    subprocess.call("find . -name '*.py' | xargs wc -l", shell=True)


@task
def commit(message="Auto-update."):
    clean()
    subprocess.call("git add *.py", shell=True)
    subprocess.call("git add -u", shell=True)
    subprocess.call("git add README.md", shell=True)
    subprocess.call("git add requirements.txt", shell=True)
    subprocess.call("git commit -m '" + message + "'", shell=True)
    

@task
def push(branch="master"):
    commit()
    pull(branch)
    subprocess.call("git push origin " + branch, shell=True)
    
    
@task
def pull(branch="master"):
    subprocess.call("git pull origin " + branch, shell=True)


@task
def readme():
    subprocess.call("less README.md", shell=True)