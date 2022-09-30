import char_index

# TESTCASES
# ========================================== #

# test cases for char_index (First and Last Index)
def test_char_index():
    assert(char_index.char_index("hello", "l") == [2, 3]) 
    assert(char_index.char_index("circumlocution", "c") == [0, 8]) 
    assert(char_index.char_index("happy", "h") == [0, 0]) 
    assert(char_index.char_index("happy", "y") == [4, 4]) 
    assert(char_index.char_index("happy", "e") == None) 
    assert(char_index.char_index("dfs dfsfsdfds dfs d", "e") == None) 
