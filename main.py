from pyfiglet import Figlet
import argparse
import time
import sys
import datetime
import FindMyIP as ip
from enum import Enum



class IPAddressClass(Enum):
    A = 'Class A'
    B = 'Class B'
    C = 'Class C'
    Invalid = 'Invalid IP address'


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


def check_internet_connectivity()->bool:
    return ip.internet()


def get_priv_ip():
    local_ip = ip.internal()
    return local_ip

def detect_priv_network_class(ip_address):
    # Split the IP address into octets
    octets = ip_address.split('.')

    # Ensure the IP address has 4 octets
    if len(octets) != 4:
        return IPAddressClass.Invalid

    # Convert the first octet to an integer
    first_octet = int(octets[0])

    # Check the range of the first octet to determine the class
    if 1 <= first_octet <= 126:
        return IPAddressClass.A
    elif 128 <= first_octet <= 191:
        return IPAddressClass.B
    elif 192 <= first_octet <= 223:
        return IPAddressClass.C
    else:
        return IPAddressClass.Invalid

def get_external_ip_address():
    ex_address = ip.external()
    return ex_address

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
