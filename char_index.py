'''
Given a word, write a function that returns the first index and the last index of a character.

Examples
char_index("hello", "l") ➞ [2, 3]
# The first "l" has index 2, the last "l" has index 3.

char_index("circumlocution", "c") ➞ [0, 8]
# The first "c" has index 0, the last "c" has index 8.

char_index("happy", "h") ➞ [0, 0]
# Only one "h" exists, so the first and last index is 0.

char_index("happy", "e") ➞ None
# "e" does not exist in "happy", so we return undefined.

Notes
-- If the character does not exist in the word, return None.
-- If only one instance of the character exists, the first and last index will be the same.
-- Check the Resources tab for hints.

'''
def char_index(str, c):
    if (str.count(c) >= 1):
        # return first and second index
        return [str.find(c), str.rindex(c)] 
    return None
    
print(char_index("hello", "l")) # [2, 3]
# The first "l" has index 2, the last "l" has index 3.

print(char_index("circumlocution", "c")) # [0, 8]
# The first "c" has index 0, the last "c" has index 8.

print(char_index("happy", "h")) # [0, 0]
# Only one "h" exists, so the first and last index is 0.

print(char_index("happy", "e")) # None
# "e" does not exist in "happy", so we return undefined.
