import sqlite3
import os
#from config import DATABASE_FILE_PATH

dirname = os.path.dirname(__file__)

#connection = sqlite3.connect(DATABASE_FILE_PATH)
#print(os.path.join(dirname, "..", "data", "database.sqlite"))
connection = sqlite3.connect(os.path.join(dirname, "data", "database.sqlite"))
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection