#!/usr/bin/python3

import sys
from optparse import OptionParser

from csv_sorter import CSVSorter

if len(sys.argv) is 1:
    sys.argv.append('--help')

parser = OptionParser()
parser.add_option("-f", "--file", dest="file",
                  help="specify CSV file", metavar="<file>")
parser.add_option("-c", "--column", dest="column",
                  help="specify column to sort by", metavar="<column index>")

(options, args) = parser.parse_args()


def validate_options(the_options):
    required_options = "--file --column"

    if the_options.file and the_options.column:
        return True
    else:
        print("Must provide the required options: " + required_options)
        exit(0)

validate_options(options)

CSVSorter(str(options.file)).by_col(int(options.column)).print_all()


