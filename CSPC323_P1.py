
#TODO deal with comments, whitespace, actually try the shit

keywords = {'if', 'return'}
operators = {'>', '=', '+', '-', '*', '/', '<'}
separators = {'(', ')', '{', '}', ';'}
whitespace = {' '}  #not used currently but prob will need it later


#yoinked this section for a prev assignment
def lexical_analyzer(filename):
    try:
        with open(filename, 'r') as file:
            input_text = file.read()
            tokens = tokenize(input_text)
            for token, token_type in tokens:
                print(f'"{token}" = {token_type}')
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

if __name__ == "__main__":
    filename = "CPSC323P1_input.txt"  #replace the file name for the file name
    lexical_analyzer(filename)
  

def tokenize(input_text):
    tokens = []          #holds the shit
    i = 0  
    
    while i < len(input_text):  
        
        current_char = input_text[i]  
        
        if current_char in operators:
            tokens.append((current_char, 'operator'))
            i += 1
            continue
        
        if current_char in separators:
            tokens.append((current_char, 'separator'))
            i += 1
            continue
        
        if current_char.isdigit():
            num = current_char
            i += 1
            tokens.append((num, 'integer'))
            continue
        
        if current_char.isalpha(): 
            identifier = current_char
            i += 1
            if identifier in keywords:
                tokens.append((identifier, 'keyword'))
            else:
                tokens.append((identifier, 'identifier'))
            continue
       
    
    return tokens
