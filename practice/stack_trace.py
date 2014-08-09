#!/usr/bin/env python
import traceback
import sys
from termcolor import colored


#print colored(dir(traceback), 'green')

output = dir(traceback)
print colored(output, 'green')

traceback.print_stack()
