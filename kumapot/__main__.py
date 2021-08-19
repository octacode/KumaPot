"""
KumaPot.

Simple TCP Logger

Usage:
    python -m kumapot <config_filepath>

Sample:
    python -m kumapot kumapot.example.ini

Options:
    [<config_filepath>]   Path to Configuration options .ini file
    -h --help   Show this screen
"""

import configparser
import sys

from kumapot import HoneyPot

if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help'] :
    print(__doc__)
    sys.exit(1)


# TODO: To replace with Docopt
# config_filepath = '/etc/kumapot.example.ini'
config_filepath = sys.argv[1]
config = configparser.ConfigParser()
config.read(config_filepath)
ports = config.get('default', 'ports', raw=True, fallback='22,80,443,8080,8888,9999,3306')
host = config.get('default', 'host', raw=True, fallback='0.0.0.0')
log_filepath = config.get('default', 'logfile', raw=True, fallback='/var/log/nanopot.log')

ports_list = []
try:
    ports_list = ports.split(',')
except Exception as e:
    print('[-] Error parsing  ports: %s \n Exiting Program', ports)

honeypot = HoneyPot(ports_list, log_filepath, host)
honeypot.run()
