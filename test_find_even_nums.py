import find_even_nums

# TESTCASES
# ========================================== #

# test cases for find_even_nums (Even Number Generator, i.e. https://edabit.com/challenge/eJLwXpuaffjFnzENN)
def test_find_even_nums():
    assert(find_even_nums.find_even_nums(10) == [2, 4, 6, 8, 10])
    assert(find_even_nums.find_even_nums(8) == [2, 4, 6, 8])
    assert(find_even_nums.find_even_nums(4) == [2, 4])
    assert(find_even_nums.find_even_nums(2) == [2])    
    assert(find_even_nums.find_even_nums(1) == [])    