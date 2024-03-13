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
