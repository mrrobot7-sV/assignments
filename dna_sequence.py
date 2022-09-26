import random

'''
-- En een extra: Schrijf een functie die een DNA sequentie teruggeeft, die als argument de lengte neemt, en de sequentie teruggeeft
-- Cytosine (C), Guanine (G), Adenine (A) en Thimine (T), waarmee het idee is om ze in willekeurige volgorde een [x] lengte string van te maken
'''

def get_DNA_sequence(l):
    dna_bases = ["C", "G", "A", "T"]
    result = ''
    for x in range(0,l):
        result += random.choice(dna_bases)
    return result
    
print(get_DNA_sequence(5))
print(get_DNA_sequence(15))
