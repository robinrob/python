import subprocess
import logging
import os
import shutil

from fabric.decorators import task
f
DEFAULT_BRANCH = "master"


@task
def commit(message="Auto-update."):
    add()
    status()
    subprocess.call("git commit -m '" + message + "'", shell=True)


@task
def add():
    clean()
    subprocess.call("git add .", shell=True)
    subprocess.call("git add .gitignore", shell=True)
    subprocess.call("git add -u", shell=True)
    subprocess.call("git add README.md --ignore-errors", shell=True)
    subprocess.call("git add requirements.txt --ignore-errors", shell=True)


@task
def push(branch=DEFAULT_BRANCH):
    subprocess.call("git push origin " + branch, shell=True)
    
    
@task
def pull(branch=DEFAULT_BRANCH):
    subprocess.call("git pull origin " + branch, shell=True)


@task
def save(message="Auto-update", branch=DEFAULT_BRANCH):
    commit(message)
    pull(branch)
    push(branch)
    

def wrap_quotes(s):
    return "'" + s + "'"


@task
def test():
    subprocess.call("nosetests", shell=True)


@task
def count():
    clean()
    subprocess.call("find . -name '*.py' | xargs wc -l", shell=True)