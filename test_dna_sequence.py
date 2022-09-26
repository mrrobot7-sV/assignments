import dna_sequence

# TESTCASES
# ========================================== #

# test get_DNA_sequence
def test_dna_sequence():
    assert(len(dna_sequence.get_DNA_sequence(5)) == 5)
    assert(len(dna_sequence.get_DNA_sequence(15)) == 15)
