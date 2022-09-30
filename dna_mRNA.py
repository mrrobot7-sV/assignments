import random

'''
-- DNA generator maken met gebruik van de random module en vervolgens deze DNA string vertalen naar MRNA
'''

def get_DNA_sequence(l):
    dna_bases = ["C", "G", "A", "T"]
    result = ''
    for x in range(0,l):
        result += random.choice(dna_bases)
    return result

def get_mRNA(dna):
    # TODO: When a DNA string is invalid an exception should
    #       be raised.
    mRNA = {"C":"G", "G":"C", "A":"U", "T":"A"}
    result = ''
    for x in dna:
        result += mRNA[x]
    return result 
    
dna = get_DNA_sequence(5)
print(f"DNA sequence '{dna}' to mRNA output = {get_mRNA(dna)}")
dna = get_DNA_sequence(25)
print(f"DNA sequence '{dna}' to mRNA output = {get_mRNA(dna)}")