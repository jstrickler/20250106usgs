import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(name)s %(filename)s %(lineno)d %(message)s', # format log entry
    datefmt="%x %X",  # set date/time format
    filename='../LOGS/loggers.log',
    level=logging.INFO,
)

logger_one = logging.getLogger("Logger1") # unique logger names
logger_two = logging.getLogger("Logger2")

logger_one.info("this is information")  # use logger 1
logger_two.warning("this is a warning")  # use logger 2
logger_one.info("this is information")
logger_two.critical("this is critical")
