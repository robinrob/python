#!/usr/bin/env python
import traceback
import sys
from termcolor import colored


#print colored(dir(traceback), 'green')

# output = dir(traceback)
# print colored(output, 'green')

def do_it():
    try:
        robin
    except NameError as e:
        # traceback.print_stack()
        # traceback.print_exc()
        # traceback.print_exception(NameError, e, traceback)
        trace = traceback.format_exc()
        print "trace: " + trace
        pass
        
        
do_it()