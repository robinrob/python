import subprocess
import logging
import os

from fabric.decorators import task

# Configurable parameters
PYTHONBREW_DIR = "~/.pythonbrew"

SRC_DIR = './'

PYTHON3 = '3.3.1'

# Do not change this - used in initial installation
DEFAULT_PYTHON_APP = "pyapp.py"

@task
def install():
    if not has_been_installed():
        os.rename(DEFAULT_PYTHON_APP, app_py())

    logging.basicConfig(level=logging.DEBUG)
    install_python()
    install_requirements()


def has_been_installed():
    return os.path.exists(app_py())


def app_name():
    return os.getcwd().split(os.sep)[-1]


def app_py():
    return app_name() + '.py'


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
def run(args="\'Hello from " + app_name() + "!\'"):
    if not has_been_installed():
        install()

    subprocess.call("pythonbrew py -p " + PYTHON3 + " " + app_py() + " " + args, shell=True)


@task
def count():
    clean()
    subprocess.call("find . -name '*.py' | xargs wc -l", shell=True)


@task
def commit(message="Auto-update."):
    clean()
    subprocess.call("git add *.py", shell=True)
    subprocess.call("git add -u", shell=True)
    subprocess.call("git add README.md --ignore-errors", shell=True)
    subprocess.call("git add requirements.txt --ignore-errors", shell=True)
    subprocess.call("git commit -m '" + message + "'", shell=True)
    

@task
def push(branch="master"):
    subprocess.call("git push origin " + branch, shell=True)
    
    
@task
def pull(branch="master"):
    subprocess.call("git pull origin " + branch, shell=True)
    
    
@task
def status():
    subprocess.call("git status", shell=True)
    
    
@task
def log():
    subprocess.call("git log", shell=True)


@task
def deploy(message='', branch="master"):
    commit(message)
    status()
    pull(branch)
    push(branch)


@task
def readme():
    subprocess.call("less README.md", shell=True)