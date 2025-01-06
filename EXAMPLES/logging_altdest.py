import sys
from getpass import getpass
import logging
import logging.handlers

logger = logging.getLogger()  # get logger
logger.setLevel(logging.DEBUG)  # minimum log level

if sys.platform == 'win32':
    eventlog_handler = logging.handlers.NTEventLogHandler("Python Log Test")  # create NT event log handler
    logger.addHandler(eventlog_handler)  # install NT event handler
else:
    syslog_handler = logging.handlers.SysLogHandler()  # create syslog handler
    logger.addHandler(syslog_handler)  # install syslog handler

smtp_password = getpass("SMTP Password: ")

# note -- use your own SMTP server...
email_handler = logging.handlers.SMTPHandler(
    ("smtp2go.com", 2525),
    'LOGGER@pythonclass.com',
    ['jstrickler@gmail.com'],
    'Alternate Destination Log Demo',
    ('pythonclass', smtp_password),
)  # create email handler

logger.addHandler(email_handler)  # install email handler

logger.debug('this is debug')  # goes to all handlers
logger.critical('this is critical')  # goes to all handlers
logger.warning('this is a warning')  # goes to all handlers
