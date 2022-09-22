import challenges4

# TESTCASES
# ========================================== #

# test cases for challenges in challenges4.py
def test_double_char():
    assert(challenges4.double_char("String") == "SSttrriinngg")
    assert(challenges4.double_char("Hello World!") == "HHeelllloo  WWoorrlldd!!")
    assert(challenges4.double_char("1234!_ ") == "11223344!!__  ")