import logging

# these will print to STDERR
logging.warning("I've got a bad feeling about this...")
logging.error("This is BAD")

# these won't print because default level is logging.WARNING
logging.info("The shortest president was James Madison")
logging.debug("I'm here!")

