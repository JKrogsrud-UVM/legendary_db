import sqlite3
import pandas as pd
import csv
import re

SET_DICT = {'SW2': 'Secret Wars Volume 2',
            'CA': 'Captain America 75th Anniversary',
            'WWH': 'World War Hulk',
            'DC': 'Dark City',
            'LN': 'Legendary Noir',
            'AM': 'Ant-Man',
            'SW1': 'Secret Wars Volume 2',
            'XM': 'X-Men',
            'PtTR': 'Paint the Town Red',
            'B': 'Base',
            'DP': 'Deadpool',
            'V': 'Villains',
            'CW': 'Civil War',
            'VNM': 'Venom',
            'GotG': 'Guardians of the Galaxy',
            'FI': 'Fear Itself',
            'C': 'Champions',
            'SH': 'Spider-Man Homecoming',
            'F4': 'Fantastic 4',
            'D': 'Dimensions'}

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
    with open('../characters.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            # Clean_line and store in database
            print(row)

def clean_list(line):
    # every line of the .csv file looks like:
    # [name, team affiliation, common card #1 classes, common card #2 classes, uncommon card classes, rare card classes]
    # The line received will be of the form of a list:
    # [character name, team affiliation, strength, instinct, covert, tech, ranged, set]

    cleaned_list = []

    # index 0 is name
    cleaned_list.append(line[0])

    # index 1 is team affiliation
    cleaned_list.append(line[1])

    # the next four indices will either be a single word, or multiple separated by either a / or []
    # We need to create a set of the unique words (hero classes)

    classes = []

    for card in line[2:-2]:
        # check if a / is present
        class_split = re.split('/|\[|\]', card)
        for h_class in class_split:
            # Ignore any empty strings
            if len(h_class) > 0:
                if h_class not in classes:
                    classes.append(h_class)

    if 'Strength' in classes:
        cleaned_list.append(True)
    else:
        cleaned_list.append(False)

    if 'Instinct' in classes:
        cleaned_list.append(True)
    else:
        cleaned_list.append(False)

    if 'Covert' in classes:
        cleaned_list.append(True)
    else:
        cleaned_list.append(False)

    if 'Tech' in classes:
        cleaned_list.append(True)
    else:
        cleaned_list.append(False)

    if 'Range' in classes:
        cleaned_list.append(True)
    else:
        cleaned_list.append(False)

    classes.append(SET_DICT[card[-1]])

    return cleaned_list

"""
load_database should start a connection with the database (creating it if there is none)
"""
def create_database():
    con = sqlite3.connect("legendary.db")  # initiates the database and creates it if not loaded
    cur = con.cursor()
