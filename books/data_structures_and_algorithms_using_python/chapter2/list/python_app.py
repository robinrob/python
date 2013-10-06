import argparse

import termcolor

parser = argparse.ArgumentParser(description='Run Python App.')

parser.add_argument('msg', metavar='msg', type=str,
                    help='message to show')

args = parser.parse_args();

print(termcolor.colored(args.msg, 'green'))