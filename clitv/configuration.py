import configparser
import os

config = configparser.RawConfigParser()
config.read(['/etc/clitv', os.path.expanduser('~/.clitvrc')])

def sources():
    return {str(sec): dict(config[str(sec)]) for sec in config.sections()[1:]}
