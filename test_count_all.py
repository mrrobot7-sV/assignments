import count_all

# TESTCASES
# ========================================== #

# test cases for count_all (Count the Letters and Digits)
def test_count_all():
    assert(count_all.count_all("Hello World") == { "LETTERS":  10, "DIGITS": 0 }) # { "LETTERS":  10, "DIGITS": 0 }
    assert(count_all.count_all("H3ll0 Wor1d") == { "LETTERS":  7, "DIGITS": 3 }) # { "LETTERS":  7, "DIGITS": 3 }
    assert(count_all.count_all("149990") == { "LETTERS": 0, "DIGITS": 6 }) # { "LETTERS": 0, "DIGITS": 6 }