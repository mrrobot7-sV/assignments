import reverser

# TESTCASES
# ========================================== #

# test cases for reverse (The "Reverser", i.e. https://edabit.com/challenge/9hQogtkbZSSJ8tYsG)
def test_double_char():
    assert(reverser.reverse("Hello World") == "DLROw OLLEh")
    assert(reverser.reverse("ReVeRsE") == "eSrEvEr")
    assert(reverser.reverse("Radar") == "RADAr")