import logging

logging.basicConfig(
    filename='../LOGS/levels.log',
    level=logging.WARNING,
) # setup logging

logging.warning('This message will be logged') # message will be output
logging.debug('This message will NOT be logged') # message will NOT be output
logging.error('This message will be logged') # message will be output
