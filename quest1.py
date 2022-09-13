# Zoek het antwoord in deze mengelmoes van Dicts/Lists, en wat het pad daar naar toe is
Zoektocht = {'dict' : {'dict' : {'dict' : {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}, 'list': ["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}, 'list': ["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'dict' : {'Deze': "Het antwoord", 'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}, 'list': ["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'Deze': "Het andwo0rdt", 'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Deze': "Het andw00rd", 'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}}}}}, 'list': ["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'dict' : {'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}, 'list': [["bla", 15, "asdf51sf", "Hallo", ["bla", 15, "asdf51sf", "Hallo"]]], 'ding': "aaaaaaaa", 'Nog een': 15, 'nou nog eentje dan': {'Deze': "Het andwoord", 'Niet deze': "Geen antwoord", 'Ook niet deze': 0, 'Nope': "Nee"}}}

'''
Implementation steps that were taken:

1. Get JSON string
2. Search through JSON-string to find index of "Het antwoord"
3. Create the path by getting the substring, using the previous found index
'''
quest = Zoektocht

import json

jstr = json.dumps(quest)

def search_str(str):
    index = jstr.find(str)
    if index != -1:
        return jstr[0:index+len(str)]
    return print(f"Could not find {str}")

sstr = "Het antwoord"        
path = search_str(sstr)
print(f"Path to '{sstr}' = {path}\n")