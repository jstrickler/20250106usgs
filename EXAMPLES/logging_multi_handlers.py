import logging

screen_handler = logging.StreamHandler()
screen_handler.setLevel(logging.ERROR)

file_handler = logging.FileHandler("../LOGS/multihandlers.log")
file_handler.setLevel(logging.INFO)

logging.basicConfig(
    handlers=[screen_handler, file_handler],
)

logging.info("starting multi handler demo")
logging.warning("this is a warning")
logging.error("I lost my hat")
logging.critical("we are out of coffee")
logging.info("ending multi handler demo")
