import sys
import subprocess
import warnings

from fabric.decorators import task

@task(args='')
def run(args):
    #args = ""
    #for i in range(2, len(sys.argv)):
    #    args += sys.argv[i] + " "

    subprocess.call("pythonbrew use 3.3.1", shell=True)
    subprocess.call("pythonbrew py -p 3.3.1 life.py " + args, shell=True)
