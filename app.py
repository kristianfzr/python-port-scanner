import pyfiglet
import sys
import socket
from datetime import datetime
import argparse

parser = argparse.ArgumentParser(description='A cli port scanner')
parser.add_argument(
    'hostname', help='The target hostname for the scan. e.g: www.example.com')
parser.add_argument('--ports', nargs='+', type=int, help='A list of custom ports to scan.')
args = parser.parse_args()

ascii_banner = pyfiglet.figlet_format('CLI PORT SCANNER')
print(ascii_banner)

target = socket.gethostbyname(args.hostname)

print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))

# This function makes the socket ipv4 connection to the target(hostname) for the ports given.
def socket_connection(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    
    result = s.connect_ex((target, port))
    if result == 0:
        print('Port {} is open'.format(port))
    s.close()

try:
    if not args.ports:
        for port in range(1, 65535):
            socket_connection(target, port)
    else:
        for port in args.ports:
            socket_connection(target, port)
            
except KeyboardInterrupt:
    print("\n Exiting Program!")
except socket.gaierror:
    print("\n Hosntame Could Not Be Resolved!")
except socket.error:
    print("\n Server not responding!")
    sys.exit()