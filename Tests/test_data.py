def test_data_one():
    assert True

"""
tests basic functionality
input: "Agent X-13,SHIELD,Range,Tech,Covert,Instinct,CA"
output: "Agent X-13,SHIELD,false,true,true,true,true,Captain America 75th Anniversary
"""
def test_clean_line_one():
    assert clean_line("Agent X-13,SHIELD,Range,Tech,Covert,Instinct,CA") == \
                    "Agent X-13,SHIELD,false,true,true,true,true,Captain America 75th Anniversary"


"""
tests edge case when slashes are used for split cards
input: "Agent Venom,Spider Friends,Tech,Instinct/Strength,Instinct,Strength,SW2"
output: "Agent Venom,Spider Friends,true,true,false,true,false,Secret Wars Volume 2"
"""
def test_clean_line_two():
    assert clean_line("Agent Venom,Spider Friends,Tech,Instinct/Strength,Instinct,Strength,SW2") == \
                        "Agent Venom,Spider Friends,true,true,false,true,false,Secret Wars Volume 2"


"""
tests edge case when []'s are used for transform cards
input: "Amadeus Cho,Champions,Instinct,Tech [Strength],Tech,Tech,WWH"
output: "Amadeus Cho,Champions,true,true,false,true,false,World War Hulk"
"""
def test_clean_line_three():
    assert clean_line("Amadeus Cho,Champions,Instinct,Tech [Strength],Tech,Tech,WWH") == \
           "Amadeus Cho,Champions,true,true,false,true,false,World War Hulk"


"""
tests case where a name has a comma
input: "Joe Fixit, Grey Hulk",Crime Syndicate,Strength,Covert,Strength [Instinct],Covert,WWH"
output: "Joe Fixit: Grey Hulk,Crime Syndicate,true,true,true,false,false,World War Hulk"
"""
def test_clean_line_four():
    assert clean_line('"Joe Fixit, Grey Hulk",Crime Syndicate,Strength,Covert,Strength [Instinct],Covert,WWH') == \
           "Joe Fixit: Grey Hulk,Crime Syndicate,true,true,true,false,false,World War Hulk"