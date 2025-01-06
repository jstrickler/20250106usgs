from argparse import ArgumentParser
import logging
from logging.config import dictConfig

# set up -d option to script
parser = ArgumentParser(description="Logging config demo")
parser.add_argument("-d", dest="debug", action="store_true", help="show debug messages")
args = parser.parse_args()

CONFIG = {
    "version": 1,  # required
    "loggers": {
        "root": {  # root can also be directly configured
            "level": 'ERROR',
            "handlers": ["console", "file"],  # handler IDs from this file
        },
    },
    "formatters": {
        "minimal": {
            "format": '%(name)s %(message)s'
        },
        "full": {
            "format": '%(asctime)s %(levelname)-10s %(name)-10s %(message)s',
            "datefmt": "%x %X",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",  # handler must be a string
            "formatter": "minimal",  # formatter ID from this file
            "level": "ERROR",    # translated to logging.ERROR
            "stream": "ext://sys.stderr",  # default is sys.stderr
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "full",
            "filename": "../LOGS/dictconfig.log",
            "level": "DEBUG",
        },
    },
}

dictConfig(CONFIG)


if args.debug:
    root = logging.getLogger()
    # print(root.handlers)
    root.setLevel(logging.DEBUG)  # change level of file handler

logging.info("script begins")
logging.debug("configuration from a dictionary")
logging.error("Whoa -- this is not good")
logging.critical("Dude, we're doomed")
logging.info("script ends")
