import coin_flip

# TESTCASES
# ========================================== #

# test cases for coin flip.
def test_coin_flip():
    c = coin_flip.coin_flip(5)
    assertValue = c[0] + c[1]
    assert(assertValue == 5)
    c = coin_flip.coin_flip(1000)
    assertValue = c[0] + c[1]
    assert(assertValue == 1000)
