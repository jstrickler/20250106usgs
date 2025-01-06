# only one connection and one cursor will be created

import sqlite3

db_connection = sqlite3.connect(':memory:')

db_cursor = db_connection.cursor()

