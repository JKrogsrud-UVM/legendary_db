import sqlite3
import pandas as pd

"""
data.py will be responsible for functions that create the database and SQL statements that directly
interact with the database.
"""

"""
load_database should start a connection with the database (creating it if there is none)
"""
def load_database():
    con = sqlite3.connect("legendary.db")  # initiates the database and creates it if not loaded
    cur = con.cursor()
