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