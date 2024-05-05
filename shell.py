from lexer import Lexer

while True:
    text = input("BaiyyoScript: ")
    tokenizer = Lexer(text)
    tokens = tokenizer.tokenize()
    
    print(tokens)