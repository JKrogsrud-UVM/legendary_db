from db.data import clean_list
from db.data import create_tables
from db.data import load_characters
from db.data import load_adversaries
from db.data import load_mastermind
from db.data import load_scheme
import os
import sqlite3

def test_data_one():
    assert True

"""
tests basic functionality
input: ["Agent X-13","SHIELD","Range","Tech","Covert","Instinct","CA"]
output: ["Agent X-13","SHIELD",False,True,True,True,True,"Captain America 75th Anniversary"]
"""
def test_clean_line_one():
    assert clean_list(["Agent X-13", "SHIELD", "Range", "Tech", "Covert", "Instinct", "CA"]) == \
                    ["Agent X-13", "SHIELD", False, True, True, True, True, "Captain America 75th Anniversary"]


"""
tests edge case when slashes are used for split cards
input: ["Agent Venom", "Spider Friends", "Tech", "Instinct/Strength", "Instinct", "Strength", "SW2"]
output: ["Agent Venom", "Spider Friends", True, True, False, True, False, "Secret Wars Volume 2"]
"""
def test_clean_line_two():
    assert clean_list(["Agent Venom", "Spider Friends", "Tech", "Instinct/Strength", "Instinct", "Strength", "SW2"]) == \
                        ["Agent Venom", "Spider Friends", True, True, False, True, False, "Secret Wars Volume 2"]


"""
tests edge case when []'s are used for transform cards
input: ["Amadeus Cho", "Champions", "Instinct", "Tech [Strength]", "Tech", "Tech", "WWH"]
output: ["Amadeus Cho", "Champions", True, True, False, True, False, "World War Hulk"]
"""
def test_clean_line_three():
    assert clean_list(["Amadeus Cho", "Champions", "Instinct", "Tech [Strength]", "Tech", "Tech", "WWH"]) == \
           ["Amadeus Cho", "Champions", True, True, False, True, False, "World War Hulk"]


"""
tests case where a name has a comma
input: ["Joe Fixit, Grey Hulk", "Crime Syndicate", "Strength", "Covert", "Strength [Instinct]", "Covert", "WWH"]
output: ["Joe Fixit, Grey Hulk", "Crime Syndicate", True, True, True, False, False, "World War Hulk"]
"""
def test_clean_line_four():
    assert clean_list(["Joe Fixit, Grey Hulk", "Crime Syndicate", "Strength", "Covert", "Strength [Instinct]", "Covert", "WWH"]) == \
           ["Joe Fixit, Grey Hulk", "Crime Syndicate", True, True, True, False, False, "World War Hulk"]

"""
tests whether the Tables have been created by checking their table names exist in sqlite_master
output: 5
"""
def test_create_tables_one():
    create_tables("legendary.db")
    con = sqlite3.connect("legendary.db")
    cur = con.cursor()
    result = cur.execute("""SELECT name
                            FROM sqlite_master
                            WHERE type ='table' AND name NOT LIKE 'sqlite_%';""")
    check = result.fetchall()
    assert check == [('character',), ('adversary',), ('henchmen',), ('mastermind',), ('scheme',)]

"""
Test a basic SELECT statement to verify characters have been inserted correctly

"""
def test_load_characters_one():
    fname = os.path.join(os.path.dirname(__file__), 'characters.csv')
    load_characters("legendary.db", fname)
    con = sqlite3.connect("legendary.db")
    cur = con.cursor()

    select_statement = """
                        SELECT *
                        FROM character 
                        WHERE character.name = 'Angel';"""

    result = cur.execute(select_statement).fetchall()
    con.close()
    assert result == [('Angel', 'X-Men', 1, 1, 1, 0, 0, 'Dark City'), ]

"""
Tests a search with name that will have multiple results
"""
def test_load_characters_two():
    fname = os.path.join(os.path.dirname(__file__), 'characters.csv')
    load_characters("legendary.db", fname)
    con = sqlite3.connect("legendary.db")
    cur = con.cursor()

    select_statement = """
                        SELECT *
                        FROM character 
                        WHERE character.name = 'Venom';"""

    result = cur.execute(select_statement).fetchall()
    con.close()
    assert result == [('Venom','Venomverse',1,1,0,0,0,'Venom'),('Venom','Sinister Six',1,1,0,0,0,'Villains'),]

"""
Tests basic adversary loading
"""
def test_load_adversary_one():
    fname = os.path.join(os.path.dirname(__file__), "adversaries.csv")
    load_adversaries("legendary.db", fname)
    con = sqlite3.connect("legendary.db")
    cur = con.cursor()

    select_statement = """
                        SELECT *
                        FROM adversary 
                        WHERE adversary.name = 'Code Red';"""

    result = cur.execute(select_statement).fetchall()
    con.close()
    assert result == [('Code Red', 'World War Hulk'),]

"""
Tests basic henchmen loading 
"""
def test_load_henchmen_one():
    fname = os.path.join(os.path.dirname(__file__), "henchmen.csv")
    load_adversaries("legendary.db", fname)
    con = sqlite3.connect("legendary.db")
    cur = con.cursor()

    select_statement = """
                        SELECT *
                        FROM henchmen 
                        WHERE adversary.name = 'Phalanx';"""

    result = cur.execute(select_statement).fetchall()
    con.close()
    assert result == [('Phalanx', 'Dark City'),]

"""
Tests basic mastermind loading
"""
def test_load_mastermind_one():
    fname = os.path.join(os.path.dirname(__file__), "masterminds.csv")
    load_mastermind("legendary.db", fname)
    con = sqlite3.connect("legendary.db")
    cur = con.cursor()

    select_statement = """
                        SELECT *
                        FROM mastermind 
                        WHERE mastermind.name = 'Dr. Doom';"""

    result = cur.execute(select_statement).fetchall()
    con.close()
    assert result == [('Dr. Doom', 'Base'),]

"""
Tests basic scheme loading
"""
def test_load_scheme_one():
    fname = os.path.join(os.path.dirname(__file__), "schemes.csv")
    load_scheme("legendary.db", fname)
    con = sqlite3.connect("legendary.db")
    cur = con.cursor()

    select_statement = """
                        SELECT *
                        FROM scheme 
                        WHERE scheme.name = 'The Traitor';"""

    result = cur.execute(select_statement).fetchall()
    con.close()
    assert result == [('The Traitor', 'Fear Itself'),]

test_clean_line_one()
test_clean_line_two()
test_clean_line_three()
test_clean_line_four()

test_create_tables_one()

test_load_characters_one()
test_load_characters_two()

test_load_adversary_one()

test_load_mastermind_one()

test_load_scheme_one()
