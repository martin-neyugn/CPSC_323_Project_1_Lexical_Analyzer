# Pseudocode:
# Function: lexer
#
# Input: input_scode.txt (in C/C++/Java/Python)
# Output: Document named "output" That is separated into two columns
#         One column for tokens and another for lexemes
#
# function named "lexer" that takes the input of txtDoc
#     for eachWord in txtDoc
#         print eachWord on "Lexeme" column
#         print eachWord's appropriate token
from curses.ascii import isalpha, isdigit


def lexer(input_scode):

    lexemes = input_scode.split()
    print(lexemes)

    for word in lexemes:
        for char in word:
            if isalpha(char):
                print(char)
            elif isdigit(char):
                print(char)


testCode = ("while (i>lower) s = 22.00")
lexer(testCode)
