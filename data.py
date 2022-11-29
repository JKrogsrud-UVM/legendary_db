import sqlite3
import pandas as pd

"""
data.py will be responsible for functions that create the database and SQL statements that directly
interact with the database.
"""

"""
Data is pulled from another source so cleaning it to a format that fits my database
will occur from time to time.
"""
def clean_data():
    # Repeatedly call helper function clean_line on every line of characters.csv


def clean_line(line):
    # every line of the .csv file looks like
    # character name, team affiliation, strength, instinct, covert, tech, ranged, set

"""
load_database should start a connection with the database (creating it if there is none)
"""
def create_database():
    con = sqlite3.connect("legendary.db")  # initiates the database and creates it if not loaded
    cur = con.cursor()
