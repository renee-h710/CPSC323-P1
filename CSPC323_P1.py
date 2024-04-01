def lexical_analyzer(filename):
    try:
        with open(filename, 'r') as file:
            input_text = file.read()
            tokens = tokenize(input_text)
            for token, token_type in tokens:
                print(f'"{token}" = {token_type}')
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

def tokenize(input_text):
    tokens = []  # holds the tokens
    keywords = {'if', 'return'}
    operators = {'>', '=', '+', '-', '*', '/'}
    separators = {'(', ')', '{', '}', ';'}
    i = 0
    while i < len(input_text):
        current_char = input_text[i]
        # Skip whitespace
        if current_char.isspace():
            i += 1
            continue
        # Skip comments
        if current_char == '/':
            if i + 1 < len(input_text) and input_text[i + 1] == '/':
                i += 2
                while i < len(input_text) and input_text[i] != '\n':
                    i += 1
                continue
            elif i + 1 < len(input_text) and input_text[i + 1] == '*':
                i += 2
                while i < len(input_text) - 1 and not (input_text[i] == '*' and input_text[i + 1] == '/'):
                    i += 1
                i += 2
                continue
        # Identifier or keyword
        if current_char.isalpha() or current_char == '_':
            identifier = current_char
            i += 1
            while i < len(input_text) and (input_text[i].isalnum() or input_text[i] == '_'):
                identifier += input_text[i]
                i += 1
            if identifier in keywords:
                tokens.append((identifier, 'keyword'))
            else:
                tokens.append((identifier, 'identifier'))
            continue
        # Integer
        if current_char.isdigit():
            num = current_char
            i += 1
            while i < len(input_text) and input_text[i].isdigit():
                num += input_text[i]
                i += 1
            tokens.append((num, 'integer'))
            continue
        # Operators
        if current_char in operators:
            tokens.append((current_char, 'operator'))
            i += 1
            continue
        # Separators
        if current_char in separators:
            tokens.append((current_char, 'separator'))
            i += 1
            continue
        # Invalid character
        print(f"Error: Invalid character '{current_char}'")
        i += 1
    return tokens

filename = "input.txt"  # replace with the actual file name
lexical_analyzer(filename)