import logging
import shutil

from fabric.decorators import task
from fabric.operations import local
import os.path
import settings

SOURCE_CODE_DIR = "src"
PACKAGE_NAME = "core"

VIRTUAL_ENV_DIR = "venv"

RESULTS_DIR = settings.RESULTS_DIR

TEST_RESULTS_DIR = 'test_results'

TEST_RESULTS_FILE = TEST_RESULTS_DIR + '/test_results.xml'

COVERAGE_FILE = TEST_RESULTS_DIR + '/coverage.xml'

PYTHON_PATH = '/usr/bin/python2.7'


def init():
    logging.basicConfig(level=logging.DEBUG)
    if not venv_exists():
        create_virtual_environment()
    install_requirements()


@task
def install():
    init()


@task
def clean():
    "Removes files the project can generate when being run."
    local("find . -name '*.pyc' -delete")
    local("find . -name '*~' -delete")
    shutil.rmtree(RESULTS_DIR, ignore_errors=True)
    shutil.rmtree(TEST_RESULTS_DIR, ignore_errors=True)
    if os.path.exists('.coverage'):
        os.remove('.coverage')

    if venv_exists():
        shutil.rmtree(VIRTUAL_ENV_DIR, ignore_errors=True)


def create_dir(name):
    if not os.path.exists(name):
        os.makedirs(name)


# Runs a command under the virtual environment
def localVenv(command):
    local(" . " + VIRTUAL_ENV_DIR + "/bin/activate && "
          "export PYTHONPATH=" + SOURCE_CODE_DIR + " && "
          + command)


def create_virtual_environment():
    if not os.path.exists(VIRTUAL_ENV_DIR):
        local("virtualenv --python=" + PYTHON_PATH + " --no-site-packages " + VIRTUAL_ENV_DIR)


def venv_exists():
    return os.path.exists(VIRTUAL_ENV_DIR)


def install_requirements():
    localVenv('pip install python-dateutil')
    #localVenv('pip3 install -r requirements.txt')


@task(default=True)
def tests(filter=""):
    init()
    "Runs all tests. Use syntax 'fab tests:package.module.test_function' to run a specific test."
    localVenv("nosetests -v --nocapture --nologcapture --logging-filter=DEBUG " + filter)


@task
def coverage():
    init()
    if os.path.exists(TEST_RESULTS_DIR):
        shutil.rmtree(TEST_RESULTS_DIR)
    os.mkdir(TEST_RESULTS_DIR)
        
    "Produces a test results and code coverage report."
    localVenv("nosetests" + 
              " -v " + 
              " --cover-package=" + SOURCE_CODE_DIR + 
              " --cover-erase " + 
              " --cover-branches" + 
              " --with-xunit" + 
              " --xunit-file=" + TEST_RESULTS_FILE + 
              " --with-xcoverage" + 
              " --cover-xml-file=" + COVERAGE_FILE)
    
    os.rename('coverage.xml', COVERAGE_FILE)


@task
def shell():
    init()
    "Starts a Python shell loaded from the virtual environment used by the project."
    localVenv('python')


@task
def commit():
    clean()
    local("git add -u && git add * && git commit -m 'Auto-update.'")


@task
def run():
    localVenv("python jonny.py")
    

@task
def compress():
    clean()
    
    levels = os.getcwd().split('/')
    project_dir = levels[len(levels) - 1]
    
    os.chdir('../')
    
    zip_file = project_dir + '.zip'
        
    if os.path.exists(zip_file):
        os.remove(zip_file)
        
    local("zip -r " + project_dir + ".zip " + project_dir)


@task
def count():
    clean()
    local("find . -name '*.py' | xargs wc -l")
