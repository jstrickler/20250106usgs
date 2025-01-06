from argparse import ArgumentParser
import logging
from logging.config import dictConfig
import yaml


# set up -d option to script
parser = ArgumentParser(description="Logging config demo")
parser.add_argument("-d", dest="debug", action="store_true", help="show debug messages")
args = parser.parse_args()

with open('logging_config.yaml') as yaml_in:
    config = yaml.load(yaml_in, yaml.SafeLoader)

dictConfig(config)


if args.debug:
    root = logging.getLogger()
    # print(root.handlers)
    root.setLevel(logging.DEBUG)  # change level of file handler

logging.info("script begins")
logging.debug("configuration from a dictionary")
logging.error("Whoa -- this is not good")
logging.critical("Dude, we're doomed")
logging.info("script ends")
