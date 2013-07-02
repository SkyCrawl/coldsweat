# -*- coding: utf-8 -*-
'''
Coldsweat - A Fever clone

Copyright (c) 2013— Andrea Peltrin
Portions are copyright (c) 2013 Rui Carmo
License: MIT (see LICENSE.md for details)
'''

__author__ = 'Andrea Peltrin and Rui Carmo'
__version__ = (0, 6, 0, '')
__license__ = 'MIT'

from os import path
from ConfigParser import RawConfigParser
import logging

VERSION_STRING = '%d.%d.%d%s' % __version__
DEFAULT_USER_AGENT = 'Coldsweat/%s Feed Fetcher <http://lab.passiomatic.com/coldsweat/>' % VERSION_STRING

# Figure out installation directory. This has 
#  to work for the fetcher script too
installation_dir, _ = path.split(path.dirname(path.abspath(__file__)))

# def load_config(filename):
#     
#     # Defaults to bootstrap system
#     config = SafeConfigParser(defaults={
#         'engine': 'sqlite', 
#         'filename': path.join(installation_dir, 'data/coldsweat.db'), 
#         'error_threshold': 100,
#         'user_agent': DEFAULT_USER_AGENT,
#         'min_interval': 60*15,
#         'max_history': 7,        
#         'filename': path.join(installation_dir, 'coldsweat.log'),
#         'level': 'DEBUG',
#         'format': '%(asctime)s %(levelname)s: %(message)s',
#         'datefmt': '%Y-%m-%d %H:%M:%S',
#     })
# 
#     config.read(filename)    
#     return config
#config = load_config(path.join(installation_dir, 'etc/config'))

# Set up configuration settings
config = RawConfigParser()
#@@TODO: Check environ var first for config path
# os.environ('COLDSWEAT_CONFIG_PATH')
config.read(path.join(installation_dir, 'etc/config'))


logging.basicConfig(
    filename    = config.get('log', 'filename'),
    level       = getattr(logging, config.get('log', 'level')),
    format      = config.get('log', 'format'),
    datefmt     = config.get('log', 'datefmt'),
)
                  
logging.getLogger("peewee").setLevel(logging.INFO)
logging.getLogger("requests").setLevel(logging.WARN)

# Shared logger instance
log = logging.getLogger()