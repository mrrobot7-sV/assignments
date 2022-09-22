import repeating_letters

# TESTCASES
# ========================================== #

# test cases for double_char (Repeating Letters)
def test_double_char():
    assert(repeating_letters.double_char("String") == "SSttrriinngg")
    assert(repeating_letters.double_char("Hello World!") == "HHeelllloo  WWoorrlldd!!")
    assert(repeating_letters.double_char("1234!_ ") == "11223344!!__  ")