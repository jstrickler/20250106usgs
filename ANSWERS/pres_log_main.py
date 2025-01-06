import logging
from president_log import President

logging.basicConfig(
    filename="presidents.log",
    level=logging.INFO,
)

logging.info("starting pres_log_main.py")
for term in 1, 16, 26, 42, 37, 49, 8.9, -3:
    try:
        p = President(term)
    except ValueError as err:
        print(err)
    except Exception as err:
        print(err)
    else:
        print(f"{p.first_name} {p.last_name}")
        print()
logging.info("ending pres_log_main.py")
