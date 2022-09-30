import dna_mRNA

# TESTCASES
# ========================================== #

# test get_mRNA
def test_mRNA_sequence():
    assert(len(dna_mRNA.get_mRNA(dna_mRNA.get_DNA_sequence(5))) == 5)
    assert(len(dna_mRNA.get_mRNA(dna_mRNA.get_DNA_sequence(15))) == 15)
