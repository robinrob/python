#!/usr/bin/env python3

import argparse
import subprocess

import termcolor

parser = argparse.ArgumentParser(description='Create new Python app')

parser.add_argument('destination', metavar='dest', type=str,
                    help='destination of new Python app')

args = parser.parse_args();

print(termcolor.colored("Creating new Python app at: " + args.destination, "green"))
subprocess.call("fab new:destination=" + args.destination, shell=True)