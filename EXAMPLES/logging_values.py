import logging

logging.basicConfig(
    filename='../LOGS/values.log',
    level=logging.INFO,
)

for animal in 'bear', 'moose', 'boa constrictor', 'wombat':
    logging.error("I am a %s", animal)

for value in range(1, 6):
    logging.info("Value is %d", value)

