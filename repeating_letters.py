
# Repeating Letters
# ========================================== #

'''

Create a function that takes a string and returns a string in which each character 
is repeated once.

EXAMPLES

-- double_char("String") ➞ "SSttrriinngg"

-- double_char("Hello World!") ➞ "HHeelllloo  WWoorrlldd!!"

-- double_char("1234!_ ") ➞ "11223344!!__  "

NOTES
All test cases contain valid strings. Don't worry about spaces, special characters 
or numbers. They're all considered valid characters.

'''

def double_char(str):
    result = []
    for s in str:
        result.extend([s, s])
    return ''.join(result)

def main():
    print(double_char("String"))
    print(double_char("Hello World!"))
    print(double_char("1234!_ "))

if __name__ == "__main__":
    main()