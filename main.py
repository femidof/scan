from pyfiglet import Figlet
import argparse
import time
import sys


parser = argparse.ArgumentParser(
                    prog='uscan',
                    description='Super Scanner',
                    epilog='Made with curiosity and love. Do not use for bad purpose')


# parser.add_argument('filename')           # positional argument
parser.add_argument('-v', '--verbose',
                    action='store_true')
parser.add_argument('-i', '--internal',
                    action='store_true')
parser.add_argument('-e', '--external',
                    action='store_true')



args = parser.parse_args()
print(args)

f = Figlet(font='block')
print(f.renderText('Ultimate Scanner'))





def detect_ip():
    pass

def detect_network_class():
    pass


def run_external_scan():
    pass

def run_internal_scan():
    pass

def write_scan():
    pass

def print_scan():
    pass

def verbose_print():
    pass