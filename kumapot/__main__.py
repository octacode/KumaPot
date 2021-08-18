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

logger = logging.getLogger(__name__)

# TODO: To replace with Docopt
# config_filepath = '/etc/kumapot.ini'
config_filepath = 'kumapot.ini'

config = configparser.ConfigParser()
config.read(config_filepath)
ports = config.get('default', 'ports', raw=True, fallback='22,80,443,8080,8888,9999,3306')
log_filepath = config.get('default', 'logfile', raw=True, fallback='/var/log/nanopot.log')

logger.info('[*] Ports %s' % ports)
logger.info('[*] Logfile %s' % log_filepath)
ports_list = []
try:
    ports_list = ports.split(',')
except Exception as e:
    logger.error('[-] Error parsing  ports: %s \n Exiting Program', ports)

HoneyPot(ports_list, log_filepath)

