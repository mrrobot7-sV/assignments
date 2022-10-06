

import unmutating

# TESTCASES
# ========================================== #

# test cases for reverse (The "Reverser", i.e. https://edabit.com/challenge/9hQogtkbZSSJ8tYsG)
def test_change():
    assert(unmutating.change([3, 3, 3, 3, 3, 3, 3], 0) == [3, 3, 3, 3, 3, 3, 3])
    assert(unmutating.change([3, 3, 3, 3, 3, 3, 3], 0) == [3, 3, 3, 3, 3, 3, 3])
    assert(unmutating.change([3, 3, 3, 3, 3, 3, 3], 1) == [3, 2, 2, 2, 2, 2, 3])  
    assert(unmutating.change([3, 3, 3, 3, 3, 3, 3], 1) == [3, 2, 2, 2, 2, 2, 3])  
    assert(unmutating.change([3, 3, 3, 3, 3, 3, 3], 2) == [3, 2, 1, 1, 1, 2, 3])  
    assert(unmutating.change([3, 3, 3, 3, 3, 3, 3], 2) == [3, 2, 1, 1, 1, 2, 3])  
    assert(unmutating.change([3, 3, 3, 3, 3, 3, 3], 3) == [3, 2, 1, 0, 1, 2, 3])  
    assert(unmutating.change([3, 3, 3, 3, 3, 3, 3], 3) == [3, 2, 1, 0, 1, 2, 3])  