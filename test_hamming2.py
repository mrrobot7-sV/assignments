import hamming2

# TESTCASES
# ========================================== #

# test hamming distance for hamming2 boundary conditions
def test_hamming2_boundaries():
    assert(hamming2.hamming_distance("abcde", "bcdef") == 5)
    assert(hamming2.hamming_distance("abcde", "abcde") == 0)
    assert(hamming2.hamming_distance("strong", "strung") == 1) 
    assert(hamming2.hamming_distance("strstrong", "strstrong1234567") == 7) 
    assert(hamming2.hamming_distance("strstrung", "strstrong1234567") == 8) 
    assert(hamming2.hamming_distance("strstrong", "1234567strstrong") == 16)
    assert(hamming2.hamming_distance("strstrong", "str456789rstrong") == 13)