import re

def lexical_analyzer(filename):
    # Regular expressions to identify lexemes
    keywords = {'if', 'return'}
    operators = {'>', '=', '+', '-', '*', '/', '<'}
    separators = {'(', ')', '{', '}', ';'}
    whitespace = {' '}
    
    # Open the input file
    try:
        with open(filename, 'r') as file:
            input_text = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return

    # Remove comments
    input_text = re.sub(r'\/\/.*', '', input_text)

    # Tokenize the input
    for word in re.findall(r'[a-zA-Z0-9]+|[><=+\-*/();{}]', input_text):
        if word in keywords:
            print("'" + word + "'" + " = keyword")
        elif word in operators:
            print("'" + word + "'" + " = operator")
        elif word in separators:
            print("'" + word + "'" + " = seperator")
        elif word not in whitespace:
            if word.isalpha():
                print("'" + word + "'" + " = identifier")
            else:
                print("'" + word + "'" + " = integer")
    

# Call the lexical_analyzer function with the filename
lexical_analyzer('input.txt')
