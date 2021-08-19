"""
KumaPot.

Simple TCP Logger

Usage:
    kumapot [<config_filepath>]

Options:
    [<config_filepath>]   Path to Configuration options .ini file
    -h --help   Show this screen
"""

import configparser
import logging

from kumapot import HoneyPot

# TODO: To replace with Docopt
# config_filepath = '/etc/kumapot.example.ini'
config_filepath = 'kumapot.example.ini'

config = configparser.ConfigParser()
config.read(config_filepath)
ports = config.get('default', 'ports', raw=True, fallback='22,80,443,8080,8888,9999,3306')
log_filepath = config.get('default', 'logfile', raw=True, fallback='/var/log/nanopot.log')

ports_list = []
try:
    ports_list = ports.split(',')
except Exception as e:
    print('[-] Error parsing  ports: %s \n Exiting Program', ports)

honeypot = HoneyPot(ports_list, log_filepath)
honeypot.run()
